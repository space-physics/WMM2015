[![Build Status](https://travis-ci.com/scivision/WMM2015.svg?branch=master)](https://travis-ci.com/scivision/WMM2015)
[![Coverage Status](https://coveralls.io/repos/github/scivision/WMM2015/badge.svg?branch=master)](https://coveralls.io/github/scivision/WMM2015?branch=master)
[![Build status](https://ci.appveyor.com/api/projects/status/a1xae6d5b5ek65p7?svg=true)](https://ci.appveyor.com/project/scivision/wmm2015)
[![Python versions (PyPI)](https://img.shields.io/pypi/pyversions/pyWMM2015.svg)](https://pypi.python.org/pypi/pyWMM2015)
[![Distribution format (PyPI)](https://img.shields.io/pypi/format/pyWMM2015.svg)](https://pypi.python.org/pypi/pyWMM2015)
[![Downloads](http://pepy.tech/badge/wmm2015)](http://pepy.tech/project/wmm2015)


# WMM2015                                                          

 WMM2015 World Magnetic Model\...in simple, object-oriented Python. 
 
 ![image](tests/incldecl.png) 

## Install

To get the cutting-edge development version, `git clone` and then: 
```sh
python -m pip install -e . 
```
Otherwise, for the latest release from PyPi: 
```sh
python -m pip install wmm2015   
```

## Usage
an example script
```sh
python RunWMM2015.py
```

as a Python module:
```python
import wmm2015

mag = wmm2015.wmm(glat, glon, alt_km, yeardec)
```

## Reference


If you only want the plain C program, you can do:

```sh
cd bin
cmake ../src
cmake --build .
./wmm
```


-   WMM2015 [inclination map](https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2015/WMM2015_I_MERC.pdf)
-   WMM2015 [declination map](https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2015/WMM2015_D_MERC.pdf)
