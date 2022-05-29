from setuptools import setup, Extension

module = Extension('simple_add', sources=['simple_cython.pyx'])

setup(
    name='cythonTest',
    version='1.0',
    author='jetbrains',
    ext_modules=[module]
)