#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='DataWow',
    version='0.1.0',
    description='HTTP RESTFul for calling DataWow APIs',
    url='https://datawow.io',
    author='Datawow.io',
    author_email='info@datawow.io',
    license='MIT',
    packages=['datawow'],
    include_package_data=True,
    install_requires=['requests', 'mock >= 2.0.0'],
    test_suite='datawow.test',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
