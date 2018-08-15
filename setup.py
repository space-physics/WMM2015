#!/usr/bin/env python
import subprocess
from setuptools import setup
import os

setup()

if os.name == 'nt':
    subprocess.check_call(['cmake', '-G', 'MinGW Makefiles',
                           '-DCMAKE_SH="CMAKE_SH-NOTFOUND', '../src'], cwd='bin')
else:
    subprocess.check_call(['cmake', '../src'], cwd='bin')

subprocess.check_call(['cmake', '--build', '.'], cwd='bin')
