#!/usr/bin/env python3
from os import name, path
from sys import version
import setuptools

req_pkgs = [
    'bs4',
    'requests',
    'wheel'
]


with open("README.md","r") as f:
    long_description = f.read()

setuptools.setup(
    name = "wiki",
    version = "0.0.1",
    author = "x@xx.gov",
    author_email = "x@xx.gov",
    description = "xxxxxxxxx",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/xxx/xxxx",
    packages = setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'wiki=wiki.wiki:arguments',
        ]
    },
    python_requires='>=3.*',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        ],
    install_requires=req_pkgs,
    setup_requires=req_pkgs,
)
