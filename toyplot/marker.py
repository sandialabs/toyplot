# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for managing markers (shapes used to highlight datums in plots and text).
"""

from __future__ import absolute_import

import toyplot.style

class Marker(object):
    """Represents the complete specification of a marker's appearance."""
    def __init__(self, shape=None, label=None, mstyle=None, lstyle=None, angle=None):
        self.shape = shape
        self.label = label
        self.mstyle = mstyle
        self.lstyle = lstyle
        self.angle = angle

    def __add__(self, other):
        return self.to_html() + other

    def __radd__(self, other):
        return other + self.to_html()

    def __repr__(self):
        return self.to_html()

    def to_html(self):
        """Convert a marker specification to HTML markup that can be embedded with regular text."""
        return """<marker shape="%s"%s mstyle="%s" lstyle="%s"%s/>""" % (
            self.shape,
            " label='%s'" % self.label if self.label else "",
            toyplot.style.to_css(self.mstyle),
            toyplot.style.to_css(self.lstyle),
            " angle='%s'" % self.angle if self.angle else "",
            )

    def to_dict(self):
        """Convert a marker specification to a Python dictionary for compatibility with the HTML backend."""
        return {
            "shape": self.shape,
            "label": self.label,
            "mstyle": self.mstyle,
            "lstyle": self.lstyle,
            "angle": self.angle,
        }

def from_html(html):
    """Convert a parsed xml.etree.ElementTree representation of a marker to a :class:`toyplot.marker.Marker` object."""
    return Marker(
        shape=html.get("shape"),
        label=html.get("label", ""),
        mstyle=toyplot.style.parse(html.get("mstyle", "")),
        lstyle=toyplot.style.parse(html.get("lstyle", "")),
        angle=html.get("angle", 0),
        )
