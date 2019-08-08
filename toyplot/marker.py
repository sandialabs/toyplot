# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for managing markers (shapes used to highlight datums in plots and text).
"""


import copy
import xml.sax.saxutils

import numpy

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
        return self._angle

    @property
    def label(self):
        return self._label

    @property
    def lstyle(self):
        return self._lstyle

    def __add__(self, other):
        if isinstance(other, str):
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

    def __format__(self, format_spec):
        return self.to_html()

    def to_html(self):
        """Convert a marker specification to HTML markup that can be embedded in rich text."""
        return """<marker%s%s%s%s%s%s/>""" % (
            " shape='%s'"% xml.sax.saxutils.escape(self._shape) if self._shape else "",
            " mstyle='%s'" % toyplot.style.to_css(self._mstyle) if self._mstyle else "",
            " size='%s'"% self._size if self._size else "",
            " angle='%s'" % self._angle if self._angle else "",
            " label='%s'" % xml.sax.saxutils.escape(self._label) if self._label else "",
            " lstyle='%s'" % toyplot.style.to_css(self._lstyle) if self._lstyle else "",
            )

    def intersect(self, p):
        """Compute the intersection between this marker's border and a line segment.

        Parameters
        ----------
        p: :class:`numpy.ndarray` with shape (2), required
            Relative coordinates of a line segment originating at the center of this marker.

        Returns
        -------
        dp: :class:`numpy.ndarray` with shape (2)
            Relative coordinates of the intersection with this marker's border.
        """
        if self._size:
            if self._shape in ["o", "oo", "o|", "o/", "o-", "o\\", "o+", "ox", "o*"]:
                p /= numpy.linalg.norm(p)
                p *= self._size / 2
                return p
            if self._shape in ["s"]:
                u = numpy.max(numpy.abs(p))
                p /= u
                p *= self._size / 2
                return p
            if self._shape and self._shape[0] == "r":
                width, height = self._shape[1:].split("x")
                width = float(width)
                height = float(height)

                ap = numpy.abs(p)
                if ap[1]:
                    if ap[0] / ap[1] > width / height:
                        p = p / ap[0] * self._size * width / 2
                    else:
                        p = p / ap[1] * self._size * height / 2
                else:
                    p = p / ap[0] * self._size * width / 2
                return p

        return numpy.zeros((2,))


def create(shape=None, mstyle=None, size=None, angle=None, label=None, lstyle=None):
    """Factory function for creating instances of :class:`toyplot.marker.Marker`."""
    return Marker(shape=shape, mstyle=mstyle, size=size, angle=angle, label=label, lstyle=lstyle)


def convert(value):
    """Construct an instance of :class:`toyplot.marker.Marker` from alternative representations."""
    if value is None:
        return value
    if isinstance(value, Marker):
        return value
    if isinstance(value, str):
        return Marker(shape=value, mstyle=None, size=None, angle=None, label=None, lstyle=None)
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
