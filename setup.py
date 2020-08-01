#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='folklore',
    version='0.2.0',
    description='An elegant thrift service development framework',
    long_description=open("README.rst").read(),
    author='maralla',
    author_email="maralla.ai@gmail.com",
    packages=find_packages(),
    package_data={'': ['LICENSE', 'README.rst']},
    url='https://github.com/maralla/folklore',
    install_requires=[
        'folklore-config',
        'folklore-thrift',
        'thriftpy>=0.3.9',
        'gevent>=1.2.1',
    ],
)
