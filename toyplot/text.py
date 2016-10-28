# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functions for manipulating text."""

from __future__ import division

import sys
import xml.etree.ElementTree as xml

import numpy

import toyplot.broadcast
import toyplot.require
import toyplot.transform
import toyplot.units


def extents(text, angle, style):
    """Compute (inexact) extents for a text string, based on the given coordinates and style.
    """
    text = toyplot.require.string_vector(text)
    lengths = numpy.array([len(string) for string in text])

    font_size = toyplot.units.convert(style["font-size"], target="px")
    anchor_shift = toyplot.units.convert(
        style.get(
            "-toyplot-anchor-shift",
            "0px"),
        target="px",
        reference=font_size)
    text_anchor = style["text-anchor"]
    baseline_shift = toyplot.units.convert(
        style.get("baseline-shift", "0px"), target="px", reference=font_size)
    alignment_baseline = style["alignment-baseline"]

    x = toyplot.broadcast.scalar(anchor_shift, text.shape)
    y = toyplot.broadcast.scalar(-baseline_shift, text.shape)

    # Because we don't have any metrics for the font, assume that the average
    # character width and height match the font size.
    width = font_size * lengths
    height = font_size

    # Compute left/right extents relative to the text anchor.
    if text_anchor == "start":
        left = x
        right = x + width
    elif text_anchor == "middle":
        left = x - width / 2
        right = x + width / 2
    elif text_anchor == "end":
        left = x - width
        right = x
    else:
        raise ValueError("Unknown text-anchor value: %s" % text_anchor)

    # Compute top/bottom extents relative to the text baseline.
    if alignment_baseline == "hanging":
        top = y
        bottom = y + height
    elif alignment_baseline == "middle" or alignment_baseline == "central":
        top = y - height / 2
        bottom = y + height / 2
    elif alignment_baseline == "alphabetic":
        top = y - height
        bottom = y
    else:
        raise ValueError(
            "Unknown alignment-baseline value: %s" % alignment_baseline)

    # Compute axis-aligned extents regardless of the text rotation angle.
    corner1 = numpy.column_stack((left, -top))
    corner2 = numpy.column_stack((right, -top))
    corner3 = numpy.column_stack((right, -bottom))
    corner4 = numpy.column_stack((left, -bottom))

    for index, theta in enumerate(angle):
        transformation = toyplot.transform.rotation(theta)
        corner1[index] = corner1[index] * transformation
        corner2[index] = corner2[index] * transformation
        corner3[index] = corner3[index] * transformation
        corner4[index] = corner4[index] * transformation

    left = numpy.minimum(corner1.T[0], numpy.minimum(
        corner2.T[0], numpy.minimum(corner3.T[0], corner4.T[0])))
    right = numpy.maximum(corner1.T[0], numpy.maximum(
        corner2.T[0], numpy.maximum(corner3.T[0], corner4.T[0])))
    top = -numpy.maximum(corner1.T[1],
                         numpy.maximum(corner2.T[1],
                                       numpy.maximum(corner3.T[1],
                                                     corner4.T[1])))
    bottom = - \
        numpy.minimum(corner1.T[1], numpy.minimum(
            corner2.T[1], numpy.minimum(corner3.T[1], corner4.T[1])))

    return (left, right, top, bottom)


class Box(object):
    def __init__(self):
        self.children = []

    def __repr__(self):
        return "<toyplot.text.Box>"

class BlockBox(Box):
    def __init__(self):
        Box.__init__(self)

    def __repr__(self):
        return "<toyplot.text.BlockBox>"

class InlineBox(Box):
    def __init__(self):
        Box.__init__(self)

    def __repr__(self):
        return "<toyplot.text.InlineBox>"

class Newline(InlineBox):
    def __init__(self):
        InlineBox.__init__(self)

    def __repr__(self):
        return "<toyplot.text.Newline>"

class TextBox(InlineBox):
    def __init__(self, text):
        InlineBox.__init__(self)
        self._text = text

    def __repr__(self):
        return "<toyplot.text.TextBox '%s'>" % self._text


def layout(string):
    def cascade_styles(node):
        for child in node:
            cascade_styles(child)

    def block_wrap(box):
        if isinstance(box, BlockBox):
            return box
        wrapper = BlockBox()
        wrapper.children.append(box)
        return wrapper

    def inline_wrap(box):
        if isinstance(box, InlineBox):
            return box
        wrapper = InlineBox()
        wrapper.children.append(box)
        return wrapper

    def build_formatting_model(node):
        print node

        if node.tag in ["body", "p"]:
            box = BlockBox()
        elif node.tag in ["b", "code", "i", "em", "small", "span", "strong", "sub", "sup"]:
            box = InlineBox() # pylint: disable=redefined-variable-type
        elif node.tag == "br":
            box = Newline() # pylint: disable=redefined-variable-type
        else:
            raise ValueError("Unknown tag: %s" % node.tag)

        if node.text:
            box.children.append(TextBox(node.text))
        for child in node:
            box.children.append(build_formatting_model(child))
            if child.tail:
                box.children.append(TextBox(child.tail))

        block_context = numpy.any([isinstance(child, BlockBox) for child in box.children])
        if block_context:
            box.children = [block_wrap(child) for child in box.children]
        else:
            box.children = [inline_wrap(child) for child in box.children]

        return box

    def compute_layout(box):
        for child in box.children:
            compute_layout(child)

    dom = xml.fromstring(("<body>" + string + "</body>").encode("utf-8"))
    cascade_styles(dom)

    box = build_formatting_model(dom)
    compute_layout(box)

    return box

def dump(box, stream=None, level=0, indent="  "):
    if stream is None:
        stream = sys.stdout
    stream.write(indent * level)
    stream.write("%r\n" % box)
    for child in box.children:
        dump(child, stream, level+1, indent)

