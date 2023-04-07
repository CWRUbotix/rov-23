#!/usr/bin/env python
import sys
from setuptools import setup, find_packages  # This setup relies on setuptools since distutils is insufficient and badly hacked code

version = '0.1'
author = 'Pascal Wolf'
author_email = 'wolf@physik.uni-bonn.de'

with open('requirements.txt') as f:
    required = f.read().splitlines()

# Make dict to pass to setup
setup_kwargs = {'name': 'TCA9555',
                'version': version,
                'description': 'Module for interfacing TCA9555 16-bit I2C GPIO expander via Raspberry Pi',
                'url': 'https://github.com/leloup314/TCA9555',
                'license': 'MIT License',
                'long_description': '',
                'author': author,
                'maintainer': author,
                'author_email': author_email,
                'maintainer_email': author_email,
                'packages': find_packages(),
                'setup_requires': ['setuptools'],
                'install_requires': required,
                'include_package_data': True,  # accept all data files and directories matched by MANIFEST.in or found in source control
                'package_data': {'': ['README.*', 'VERSION'], 'docs': ['*'], 'examples': ['*']},
                'keywords': ['GPIO', 'Expander', 'TCA9555', 'Texas Instruments', 'I2C', 'Raspberry Pi'],
                'platforms': 'any'
                }

# Setup
setup(**setup_kwargs)
