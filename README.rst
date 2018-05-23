.. image:: https://travis-ci.com/scivision/pyWMM2015.svg?branch=master
    :target: https://travis-ci.com/scivision/pyWMM2015
    
.. image:: https://coveralls.io/repos/github/scivision/pyWMM2015/badge.svg?branch=master
    :target: https://coveralls.io/github/scivision/pyWMM2015?branch=master

.. image:: https://img.shields.io/pypi/pyversions/pyWMM2015.svg
  :target: https://pypi.python.org/pypi/pyWMM2015
  :alt: Python versions (PyPI)

.. image::  https://img.shields.io/pypi/format/pyWMM2015.svg
  :target: https://pypi.python.org/pypi/pyWMM2015
  :alt: Distribution format (PyPI)

========
pyWMM2015
========
WMM2015 World Magnetic Model...in simple, object-oriented Python.

:Author Python API: Michael Hirsch, Ph.D.

.. image:: tests/incldecl.png


Install
=======
To get the cutting-edge development version, ``git clone`` and then::

    python -m pip install -e .

Otherwise, for the latest release from PyPi::

    python -m pip install pyWMM2015

Run Example
===========

::

    python RunWMM2015.py

Reference
=========
If you only want the plain C program, you can do:

.. code:: bash

    cd bin
    cmake ../src
    make
    ./wmm


References
-----------


* WMM2015 `inclination map <https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2015/WMM2015_I_MERC.pdf>`_
* WMM2015 `declination map <https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2015/WMM2015_D_MERC.pdf>`_
