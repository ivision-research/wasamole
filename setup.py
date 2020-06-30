# -*- coding: utf-8 -*-

# This seutp file was shamelessly taken from
# "The Hitchiker's Guide to Python".
#
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='wasamole',
    version='0.5.0',
    description='A tasty framework for WebAssembly Software Analysis',
    long_description_content_type="text/markdown",
    long_description=readme,
    author="Carve Systems, LLC.",
    author_email='meadori@carvesystems.com',
    url='https://github.com/CarveSystems/wasamole',
    license='MIT License',
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Utilities",
        "Topic :: Software Development :: Assemblers",
        "Topic :: Software Development :: Disassemblers",
        "Topic :: Software Development :: Interpreters"
    ],
    scripts=['bin/wasm-objdump'],
    python_requires='>=3.7',
)
