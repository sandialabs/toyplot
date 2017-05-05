# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for managing markers (shapes used to highlight datums in plots and text).
"""

from __future__ import absolute_import

import copy

import toyplot.compatibility
import toyplot.style

class Marker(object):
    """Represents the complete specification of a marker's appearance."""
    def __init__(self, shape, mstyle, size, angle, label, lstyle):
        self._shape = shape
        self._mstyle = mstyle
        self._size = size
        self._angle = angle
        self._label = label
        self._lstyle = lstyle

    @property
    def shape(self):
        return self._shape

    @property
    def mstyle(self):
        return self._mstyle

    @property
    def size(self):
        return self._size

    @property
    def angle(self):
        return self._angle if self._angle else 0

    @property
    def label(self):
        return self._label

    @property
    def lstyle(self):
        return self._lstyle

    def __add__(self, other):
        if isinstance(other, toyplot.compatibility.string_type):
            return self.to_html() + other
        elif isinstance(other, toyplot.marker.Marker):
            result = copy.deepcopy(self)
            if other._shape is not None:
                result._shape = other._shape
            result._mstyle = toyplot.style.combine(result.mstyle, other._mstyle)
            if other._size is not None:
                result._size = other._size
            if other._angle is not None:
                result._angle = other._angle
            if other._label is not None:
                result._label = other._label
            result._lstyle = toyplot.style.combine(result.lstyle, other._lstyle)
            return result
        else:
            raise ValueError("Can't add toyplot.marker.Marker and %r" % other) # pragma: no cover

    def __eq__(self, other):
        return self._shape == other._shape and self._mstyle == other._mstyle and self._shape == other._shape and self._angle == other._angle and self._label == other._label and self._lstyle == other._lstyle

    def __hash__(self):
        return hash((self._shape, self._mstyle, self._size, self._angle, self._label, self._lstyle))

    def __radd__(self, other):
        return other + self.to_html()

    def __repr__(self):
        return self.to_html()

    def to_html(self):
        """Convert a marker specification to HTML markup that can be embedded in rich text."""
        return """<marker%s%s%s%s%s%s/>""" % (
            " shape='%s'"% self._shape if self._shape else "",
            " mstyle='%s'" % toyplot.style.to_css(self._mstyle) if self._mstyle else "",
            " size='%s'"% self._size if self._size else "",
            " angle='%s'" % self._angle if self._angle else "",
            " label='%s'" % self._label if self._label else "",
            " lstyle='%s'" % toyplot.style.to_css(self._lstyle) if self._lstyle else "",
            )


def create(shape=None, mstyle=None, size=None, angle=None, label=None, lstyle=None):
    """Factory function for creating instances of :class:`toyplot.marker.Marker`."""
    return Marker(shape=shape, mstyle=mstyle, size=size, angle=angle, label=label, lstyle=lstyle)


def convert(value):
    """Construct an instance of :class:`toyplot.marker.Marker` from alternative representations."""
    if value is None:
        return value
    if isinstance(value, Marker):
        return value
    if isinstance(value, toyplot.compatibility.string_type):
        return Marker(shape=value, mstyle=None, size=None, angle=None, label=None, lstyle=None)
    if isinstance(value, dict):
        toyplot.log.warning("dict marker specifications are deprecated, use an instance of toyplot.marker.Marker instead.")
        return Marker(
            shape=value.get("shape", None),
            mstyle=value.get("mstyle", None),
            size=value.get("size", None),
            angle=value.get("angle", None),
            label=value.get("label", None),
            lstyle=value.get("lstyle", None),
            )
    raise ValueError("Can't convert %r to toyplot.marker.Marker." % value) # pragma: no cover


def from_html(html):
    """Convert a parsed xml.etree.ElementTree representation of a marker to a :class:`toyplot.marker.Marker` object."""
    size = html.get("size", None)
    if size is not None:
        size = float(size)

    angle = html.get("angle", None)
    if angle is not None:
        angle = float(angle)

    return Marker(
        shape=html.get("shape", None),
        mstyle=toyplot.style.parse(html.get("mstyle", "")),
        size=size,
        angle=angle,
        label=html.get("label", None),
        lstyle=toyplot.style.parse(html.get("lstyle", "")),
        )
