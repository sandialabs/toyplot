# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

"""Toyplot has been implemented to work equally well in Python 2 and Python 3,
without the use of code-modification tools like `2to3`.  The
`toyplot.compatibility` module contains code to facilitate this.
"""
try:
    string_type = basestring
except:  # pragma: no cover
    string_type = str

try:
    basestring
    unicode_type = unicode
except:  # pragma: no cover
    unicode_type = str

try:
    bytes_type = bytes
except:  # pragma: no cover
    bytes_type = str
