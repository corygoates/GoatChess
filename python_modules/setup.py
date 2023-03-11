"""GoatChess: Python modules for playing chess."""

from setuptools import setup
import os
import sys

setup(name = 'GoatChess',
    version = '0.0.1',
    description = "GoatChess Python modules.",
    url = 'https://github.com/corygoates/GoatChess',
    author = 'corygoates',
    author_email = 'cory.goates@gmail.com',
    install_requires = ['numpy>=1.18', 'scipy>=1.4', 'pytest', 'matplotlib'],
    python_requires ='>=3.6.0',
    license = 'MIT',
    packages = ['goat_chess'],
    zip_safe = False)
