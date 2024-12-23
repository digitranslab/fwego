#!/usr/bin/env python
import os

from setuptools import find_packages, setup

PROJECT_DIR = os.path.dirname(__file__)


setup(
    name="changelog",
    url="https://fwego.io",
    author="Digitrans (Fwego)",
    author_email="developers@digi-trans.org",
    platforms=["linux"],
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
)
