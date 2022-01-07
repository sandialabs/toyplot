# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from setuptools import setup, find_packages
import re

setup(
    author="Timothy M. Shead",
    author_email="tshead@sandia.gov",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Environment :: Web Environment",
        "Framework :: IPython",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    description="A modern plotting toolkit supporting electronic publishing and reproducibility.",
    install_requires=[
        "arrow>=1.0",
        "custom_inherit",
        "multipledispatch",
        "numpy>=1.8.0",
        "pypng",
        "reportlab",
    ],
    long_description="""Toyplot is the kid-sized plotting toolkit for Python with grownup-sized goals:
  * Develop beautiful plots that embrace the unique capabilities of electronic publishing and support repoducibility.
  * Create the best possible data graphics "out-of-the-box", maximizing data ink and minimizing chartjunk.
  * Provide a clean, minimalist interface that scientists and engineers will love.

  See the Toyplot documentation at http://toyplot.readthedocs.io, and the Toyplot sources at http://github.com/sandialabs/toyplot""",
    maintainer="Timothy M. Shead",
    maintainer_email="tshead@sandia.gov",
    name="toyplot",
    packages=find_packages(),
    package_data = {"": ["*.csv"]},
    project_urls={
        "Chat": "https://github.com/sandialabs/toyplot/discussions",
        "Coverage": "https://coveralls.io/r/sandialabs/toyplot",
        "Documentation": "https://toyplot.readthedocs.io",
        "Issue Tracker": "https://github.com/sandialabs/toyplot/issues",
        "Regression Tests": "https://github.com/sandialabs/toyplot/actions",
        "Source": "https://github.com/sandialabs/toyplot",
    },
    url="http://toyplot.readthedocs.io",
    version=re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        open(
            "toyplot/__init__.py",
            "r").read(),
        re.M).group(1),
)
