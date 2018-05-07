# Author: Jacques Joubert
# Email: jacques@quantsportal.com

# File used to compile Cython functions
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('cython_loops.pyx'))
