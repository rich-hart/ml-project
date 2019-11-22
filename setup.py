#!/usr/bin/env python
from setuptools import setup

setup(
    name='TBD',
    install_requires=[
        'scipy',
        'gym-retro',
    ],
    packages=['academy'],
    package_dir={'academy': 'src/academy'},
    #package_data={'mypkg': ['data/*.dat']}i,
    test_suite="src.tests",
    zip_safe=False,
    tests_require=[
        'ipdb',
        'ipython',
    ],
)

