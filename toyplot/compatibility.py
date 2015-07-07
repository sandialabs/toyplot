# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

"""Toyplot has been implemented to work equally well in Python 2 and Python 3,
without the use of code-modification tools like `2to3`.  The
`toyplot.compatibility` module contains code to facilitate this.
"""

import distutils.version
import numpy

_numpy_version = distutils.version.StrictVersion(numpy.__version__)
_minimum_numpy_version = distutils.version.StrictVersion("1.7")
if _numpy_version < _minimum_numpy_version:
  raise Exception("numpy >= %s is required, found version %s" % (_minimum_numpy_version, _numpy_version))

try:
  string_type = basestring
except: # pragma: no cover
  string_type = str

try:
  basestring
  unicode_type = unicode
except:
  unicode_type = str

try:
  bytes_type = bytes
except: # pragma: no cover
  bytes_type = str

