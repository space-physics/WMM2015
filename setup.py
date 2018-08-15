#!/usr/bin/env python
import subprocess
from setuptools import setup

setup()

subprocess.check_call(['cmake', '../src'], cwd='bin')
subprocess.check_call(['cmake', '--build', '.'], cwd='bin')
