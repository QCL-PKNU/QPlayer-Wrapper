# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='qplayer-wrapper',
    version='0.1',
    description='QPlayer Wrapper for Python',
    long_description=readme,
    author='Nagyeong Choi',
    author_email='',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

