#!/usr/bin/env python3
from os import name, path
from sys import version
import setuptools

req_pkgs = [
    'bs4',
    'requests',
    'wheel'
]

setuptools.setup(
    name = "wiki",
    version = "0.0.1",
    url = "https://github.com/ixc7/wiki",
    packages = setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'wiki=wiki.wiki:arguments',
        ]
    },
    python_requires='>=3.*',
    install_requires=req_pkgs,
    setup_requires=req_pkgs,
)
