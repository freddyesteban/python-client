#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Setup script for ObjectRocket Python client."""
from setuptools import find_packages
from setuptools import setup

VERSION = ('0', '5', '2')
__version__ = '.'.join(VERSION)

with open('README.md') as f:
    readme = f.read()

with open('requirements/prod.txt') as f:
    requirements = f.read()

setup(
    author='ObjectRocket Engineering Team',
    author_email='anthony.dodd@rackspace.com',
    description='ObjectRocket Python Client',
    include_package_data=True,
    install_requires=requirements,
    long_description=readme,
    long_description_content_type='text/markdown',
    name='objectrocket',
    packages=find_packages(exclude=['tests*']),
    url='https://github.com/objectrocket/python-client/',
    version=__version__,
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: Database'
    )
)
