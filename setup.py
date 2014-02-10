#!/usr/bin/env python

from setuptools import setup

setup(name='pyplot_helper',
        version='1.0',
        description='A collection of scripts that facilitate the creation of fancy plots with matplotlib.',
        author='Johannes Schlatow',
        url='https://github.com/ValiValpas/pyplot_helper',
        license="MIT",
        packages=['pyplot_helper'],
        install_requires=['brewer2mpl', 'numpy', 'matplotlib']
        )
