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
    def __init__(self, style):
        self.style = style
        self.children = []
        self.content_width = None
        self.content_height = None

    def __repr__(self):
        return "<%s.%s %s %sx%s>" % (self.__module__, self.__class__.__name__, self.style, self.content_width, self.content_height)

class BlockBox(Box):
    def __init__(self, style):
        Box.__init__(self, style)

class InlineBox(Box):
    def __init__(self, style):
        Box.__init__(self, style)

class Newline(InlineBox):
    def __init__(self, style):
        InlineBox.__init__(self, style)

class TextBox(InlineBox):
    def __init__(self, text, style):
        InlineBox.__init__(self, style)
        self._text = text

    def __repr__(self):
        return "<%s.%s %s %sx%s '%s'>" % (self.__module__, self.__class__.__name__, self.style, self.content_width, self.content_height, self.text)

    @property
    def text(self):
        return self._text

def layout(string, style, fonts):
    def cascade_style(style, node):
        node.style = style
        for child in node:
            cascade_style(style, child)

    def block_wrap(box, style):
        if isinstance(box, BlockBox):
            return box
        wrapper = BlockBox(style)
        wrapper.children.append(box)
        return wrapper

    def inline_wrap(box, style):
        if isinstance(box, InlineBox):
            return box
        wrapper = InlineBox(style)
        wrapper.children.append(box)
        return wrapper

    def build_formatting_model(node):
        toyplot.log.debug(node)

        if node.tag in ["body", "p"]:
            box = BlockBox(node.style)
        elif node.tag in ["b", "code", "i", "em", "small", "span", "strong", "sub", "sup"]:
            box = InlineBox(node.style) # pylint: disable=redefined-variable-type
        elif node.tag == "br":
            #box = Newline(node.style) # pylint: disable=redefined-variable-type
            box = BlockBox(node.style)
        else:
            raise ValueError("Unknown tag: %s" % node.tag)

        if node.text:
            box.children.append(TextBox(node.text, node.style))
        for child in node:
            box.children.append(build_formatting_model(child))
            if child.tail:
                box.children.append(TextBox(child.tail, child.style))

        block_context = numpy.any([isinstance(child, BlockBox) for child in box.children])
        if block_context:
            box.children = [block_wrap(child, node.style) for child in box.children]
        else:
            box.children = [inline_wrap(child, node.style) for child in box.children]

        return box

    def compute_layout(fonts, box):
        for child in box.children:
            compute_layout(fonts, child)

        if isinstance(box, TextBox):
            font = fonts.font(box.style)
            box.content_width = font.width(box.text)
            box.content_height = font.ascent - font.descent
        else:
            block_context = numpy.any([isinstance(child, BlockBox) for child in box.children])
            if block_context:
                if box.children:
                    box.content_width = numpy.max([child.content_width for child in box.children])
                    box.content_height = numpy.sum([child.content_height for child in box.children])
                else:
                    box.content_width = 0
                    box.content_height = 0
            else: # Inline context
                if box.children:
                    box.content_width = numpy.sum([child.content_width for child in box.children])
                    box.content_height = numpy.max([child.content_height for child in box.children])
                else:
                    box.content_width = 0
                    box.content_height = 0

    dom = xml.fromstring(("<body>" + string + "</body>").encode("utf-8"))
    cascade_style(style, dom)
    box = build_formatting_model(dom)
    compute_layout(fonts, box)

    return box

def dump(box, stream=None, level=0, indent="  "):
    if stream is None:
        stream = sys.stdout
    stream.write(indent * level)
    stream.write("%r\n" % box)
    for child in box.children:
        dump(child, stream, level+1, indent)

