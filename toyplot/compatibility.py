# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Python 2/3 compatibility code.

Toyplot is designed to work equally well in Python 2 and Python 3 without the
need for code-modification tools like `2to3` or `six`.  This module is
simplifies writing portable code, and should not be needed by Toyplot
end-users.
"""

from __future__ import division

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
