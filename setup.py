#!/usr/bin/env python
from setuptools import setup, find_packages

import subprocess 

subprocess.call("jupyter nbconvert --to script ./src/*/*.ipynb".split())

setup(
    name='TBD',
    install_requires=[
        'scipy',
        'gym',
        'gym-retro',
        'pyglet==1.3.2',
        'matplotlib',
        'pandas',
#        'neo4j',
#        'django',
#        'djangorestframework',
#        'django_neomodel',
        'jupyter',
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

