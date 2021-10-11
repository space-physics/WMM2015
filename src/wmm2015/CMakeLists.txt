cmake_minimum_required(VERSION 3.14...3.21)

project(wmm20 LANGUAGES C)

include(CTest)

include(CheckSymbolExists)
check_symbol_exists(sqrt math.h NONEED_M)
if(NOT NONEED_M)
  set(CMAKE_REQUIRED_LIBRARIES m)
  check_symbol_exists(sqrt math.h NEED_M)
endif()

add_library(geo src/GeomagnetismLibrary.c)
set_target_properties(geo PROPERTIES POSITION_INDEPENDENT_CODE TRUE)
if(NEED_M)
  target_link_libraries(geo m)
endif()

add_library(wmm15 SHARED src/wmm_point_sub.c)
target_link_libraries(wmm15 PRIVATE geo)

# https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2020/WMM2020testvalues.pdf
add_executable(wmm_file src/wmm_file.c)
target_link_libraries(wmm_file geo)

add_test(NAME WMMfile
COMMAND $<TARGET_FILE:wmm_file> f ${CMAKE_CURRENT_SOURCE_DIR}/test_input.asc  ${CMAKE_CURRENT_BINARY_DIR}/test_output.asc
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)
set_tests_properties(WMMfile PROPERTIES
DISABLED $<BOOL:${APPLE}>
)
# wmm_file.c has bug from original authors on MacOS
