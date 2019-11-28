#!/usr/bin/env python
from setuptools import setup

setup(
    name='TBD',
    install_requires=[
        'scipy',
        'gym',
        'gym-retro',
        'pyglet==1.3.2',
        'matplotlib',
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

