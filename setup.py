# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from setuptools import setup, find_packages
import re

setup(
    name="toyplot",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Environment :: Web Environment",
        "Framework :: IPython",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    description="A modern plotting toolkit supporting electronic publishing and reproducibility.",
    install_requires=[
        "arrow",
        "colormath",
        "multipledispatch",
        "numpy>=1.8.0",
        "pypng",
        "reportlab",
    ],
    long_description="""Toyplot is the kid-sized plotting toolkit for Python with grownup-sized goals:
  * Develop beautiful interactive, animated plots that embrace the unique capabilities of electronic publishing and support repoducibility.
  * Create the best possible data graphics "out-of-the-box", maximizing data ink and minimizing chartjunk.
  * Provide a clean, minimalist interface that scientists and engineers will love.

  See the Toyplot documentation at http://toyplot.readthedocs.io, and the Toyplot sources at http://github.com/sandialabs/toyplot""",
    maintainer="Timothy M. Shead",
    maintainer_email="tshead@sandia.gov",
    url="http://toyplot.readthedocs.org",
    version=re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        open(
            "toyplot/__init__.py",
            "r").read(),
        re.M).group(1),
    packages=find_packages(),
)
