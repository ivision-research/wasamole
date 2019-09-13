# -*- coding: utf-8 -*-

# This seutp file was shamelessly taken from
# "The Hitchiker's Guide to Python".
#
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='wasamole',
    version='1.0.0',
    description='A tasty framework for WebAssembly Software Analysis',
    long_description=readme,
    author="Carve Systems, LLC.",
    author_email='meadori@carvesystems.com',
    url='https://github.com/CarveSystems/wasamole',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    scripts=['bin/wasm-objdump'],
    python_requires='>=3.7',
)
