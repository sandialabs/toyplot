# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from setuptools import setup, find_packages
setup(
  name = "toyplot",
  classifiers = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Environment :: Other Environment",
    "Environment :: Web Environment",
    "Framework :: IPython",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Programming Language :: Python :: 2",
    "Topic :: Scientific/Engineering :: Visualization",
    ],
  description = "A modern plotting toolkit supporting electronic publishing and reproducibility.",
  install_requires = ["numpy>=1.7", "colormath"],
  long_description = """Toyplot is the kid-sized plotting toolkit for Python with grownup-sized goals:
  * Develop beautiful interactive, animated plots that embrace the unique capabilities of electronic publishing and support repoducibility.
  * Create the best possible data graphics "out-of-the-box", maximizing data ink and minimizing chartjunk.
  * Provide a clean, minimalist interface that scientists and engineers will love.""",
  maintainer = "Timothy M. Shead",
  maintainer_email = "tshead@sandia.gov",
  url = "http://github.com/sandialabs/toyplot",
  version = "0.1.0",
  packages = find_packages(),
)
