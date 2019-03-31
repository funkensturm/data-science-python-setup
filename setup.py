#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io

from os.path import dirname
from os.path import join

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='data-science-project',
    version='0.1.0',
    license='MIT license',
    description='Data Science Project',
    long_description=read('README.md'),
    author='Manuel Wiedenmann',
    author_email='manuel@funkensturm.de',
    url='https://github.com/datasciencejob-de/data-science-python-setup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
)
