#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='TBD',
    install_requires=[
        'scipy',
        'gym',
        'gym-retro',
        'pyglet==1.3.2',
        'matplotlib',
        'neo4j',
        'pandas',
    ],
    packages=find_packages('src'),
    package_dir={'':'src'},
    test_suite="src.tests",
    zip_safe=False,
    tests_require=[
        'ipdb',
        'ipython',
    ],
)

