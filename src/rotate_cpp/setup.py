from setuptools import setup, Extension
from Cython.Build import cythonize

ext = Extension(
    name = "Solution_cpp",
    sources = ["Solution.pyx"],
    language = "c++"
)

setup(
    ext_modules = cythonize(ext, language_level = 3)
)