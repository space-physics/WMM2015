#!/usr/bin/env python
import subprocess
import shutil
from setuptools import setup
import os

setup()

meson = shutil.which("meson")
cmake = shutil.which("cmake")

if meson:
    subprocess.run(["meson", "setup", "build"])
    subprocess.run(["meson", "test", "-C", "build"])
elif cmake:
    cmd = [cmake, "-B", "build"]
    if os.name == "nt":
        cmd += ["-G", "MinGW Makefiles", "-DCMAKE_SH=CMAKE_SH-NOTFOUND"]
    subprocess.run(cmd)

    subprocess.run([cmake, "--build", "build", "--parallel"])
