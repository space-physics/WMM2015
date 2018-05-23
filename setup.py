#!/usr/bin/env python
install_requires = ['xarray','numpy','sciencedates']
tests_require=['pytest','nose','coveralls']

# %%
from setuptools import find_packages
from numpy.distutils.core import setup,Extension
#%% install
setup(name='pyWMM2015',
      packages=find_packages(),
      version='0.9.0',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyWMM2015',
      description='WMM2015 geomagnetic model with simple object-oriented Python interface',
      long_description=open('README.rst').read(),
	  install_requires=install_requires,
      ext_modules=[Extension(name='libwmm15',
                           sources=['src/wmm_point_sub.c'])],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Atmospheric Science',
          ],
      extras_require={'plot':['matplotlib'],
                       'tests':tests_require,},
      python_requires='>=3.5',
      tests_require=tests_require,
	  )
