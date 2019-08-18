project('wmm15', 'c',
  default_options : ['default_library=static', 'buildtype=release', 'warning_level=0'])

cc = meson.get_compiler('c')
if cc.get_id() != 'msvc'
  math_lib = cc.find_library('m')
else
  math_lib = []
endif

geo_lib = library('geo', 'src/GeomagnetismLibrary.c',
  dependencies: math_lib)

wmm15_lib = shared_library('wmm15', 'src/wmm_point_sub.c',
  link_with: geo_lib)

wmm_exe = executable('wmm', 'src/wmm_point.c',
  link_with: geo_lib)
