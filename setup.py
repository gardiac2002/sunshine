#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='sunshine',
      version='0.0.6',
      description='Sunshine - Selenium for Human Beings',
      author='Philipp Konrad',
      packages=find_packages(),
      install_requires=[
                'selenium',
                'six',
                'beautifulsoup4',])

