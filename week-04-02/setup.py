from setuptools import setup, Extension

module = Extension ('memoryview_show', sources=['memoryview_show.py'])

setup(
    name='cythonTest',
    version='1.0',
    author='jetbrains',
    ext_modules=[module]
)