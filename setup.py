from setuptools import setup, find_packages

# Author: Ryo Mitsuda
# Copyright (c) 2022 Ryo Mitsuda
# License: MIT License

from setuptools import setup
import trout

DESCRIPTION = "trout: "
NAME = 'trout'
AUTHOR = 'Ryo Mitsuda'
URL = 'https://github.com/ryomanden/trout'
LICENSE = 'MIT License'
DOWNLOAD_URL = 'https://github.com/ryomanden/trout'
VERSION = trout.__version__
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = [
    'numpy',
    ]

PACKAGES = find_packages()

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Natural Language :: Japanese',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Intended Audience :: Education',
]

with open('README.md', 'r') as fp:
    readme = fp.read()

setup(name=NAME,
      author=AUTHOR,
      maintainer=AUTHOR,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
    )