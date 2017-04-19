# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for managing markers (shapes used to highlight datums in plots and text).
"""

from __future__ import absolute_import

import toyplot.compatibility
import toyplot.style

class Marker(object):
    """Represents the complete specification of a marker's appearance."""
    def __init__(self, shape, label, mstyle, lstyle, angle):
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
        return """<marker shape="%s"%s%s%s%s/>""" % (
            self.shape,
            " label='%s'" % self.label if self.label else "",
            " mstyle='%s'" % toyplot.style.to_css(self.mstyle) if self.mstyle else "",
            " lstyle='%s'" % toyplot.style.to_css(self.lstyle) if self.lstyle else "",
            " angle='%s'" % self.angle if self.angle else "",
            )


def create(shape, label=None, mstyle=None, lstyle=None, angle=0):
    """Factory function for creating instances of :class:`toyplot.marker.Marker`."""
    return Marker(shape=shape, label=label, mstyle=mstyle, lstyle=lstyle, angle=angle)


def convert(value):
    """Construct an instance of :class:`toyplot.marker.Marker` from alternative representations."""
    if value is None:
        return value
    if isinstance(value, Marker):
        return value
    if isinstance(value, toyplot.compatibility.string_type):
        return Marker(shape=value, label=None, mstyle=None, lstyle=None, angle=0)
    if isinstance(value, dict):
        toyplot.log.warning("dict marker specifications are deprecated, use an instance of toyplot.marker.Marker instead.")
        return Marker(shape=value.get("shape", None), label=value.get("label", None), mstyle=value.get("mstyle", None), lstyle=value.get("lstyle", None), angle=value.get("angle", 0))
    raise ValueError("Can't convert %s to toyplot.marker.Marker." % value)


def from_html(html):
    """Convert a parsed xml.etree.ElementTree representation of a marker to a :class:`toyplot.marker.Marker` object."""
    return Marker(
        shape=html.get("shape"),
        label=html.get("label", ""),
        mstyle=toyplot.style.parse(html.get("mstyle", "")),
        lstyle=toyplot.style.parse(html.get("lstyle", "")),
        angle=float(html.get("angle", 0)),
        )
