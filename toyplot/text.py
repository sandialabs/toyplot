# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functions for manipulating text."""

from __future__ import division

import copy
import sys
import xml.etree.ElementTree as xml

import numpy

import toyplot.broadcast
import toyplot.require
import toyplot.style
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


class Page(object):
    """Container for one-or-more lines of text."""
    def __init__(self, style):
        self.style = style
        self.children = []


class Line(object):
    """Container for one line of text."""
    def __init__(self, style):
        self.style = style
        self.children = []


class Box(object):
    """Container for (optionally nested) text content."""
    def __init__(self, style):
        self.style = style
        self.children = []


class Newline(Box):
    """Newline inserted in a line of text."""
    def __init__(self, style):
        Box.__init__(self, style)


class TextBox(Box):
    """Box that contains text."""
    def __init__(self, text, style):
        Box.__init__(self, style)
        self.text = text


def layout(text, style, fonts):
    def cascade_styles(style, node):
        if "style" in node.attrib:
            node_style = toyplot.require.style(toyplot.style.parse(node.attrib["style"]), toyplot.require.style.text)
            style = toyplot.style.combine(style, node_style)
        else:
            style = copy.deepcopy(style)

        node.style = style
        #toyplot.log.debug("%s %s %r %r", node.tag, node.style, node.text, node.tail)
        for child in node:
            cascade_styles(style, child)

    def compute_styles(reference_font_size, node):
        font_size = node.style["font-size"]
        font_size = toyplot.units.convert(font_size, target="px", default="px", reference=reference_font_size)

        line_height = node.style["line-height"]
        if line_height == "normal":
            line_height = "120%"
        line_height = toyplot.units.convert(line_height, target="px", default="px", reference=font_size)

        node.style["font-size"] = font_size
        node.style["line-height"] = line_height

        #toyplot.log.debug("%s %s %r %r", node.tag, node.style, node.text, node.tail)
        for child in node:
            compute_styles(font_size, child)


    def build_formatting_model(node):
        def add_node(page, parent, node):
            toyplot.log.debug("build formatting model: %s", node)

            if node.tag in ["body"]:
                page = Page(node.style)
                page.children.append(Line(node.style))
                parent = page.children[-1]

                if node.text:
                    parent.children.append(TextBox(node.text, node.style))
                for child in node:
                    add_node(page, parent, child)
                    if child.tail:
                        parent.children.append(TextBox(child.tail, node.style)) # Note: the tail doesn't get the child's style
                return page

            if node.tag in ["b", "code", "i", "em", "small", "span", "strong", "sub", "sup"]:
                parent.children.append(Box(node.style))
                parent = parent.children[-1]
                if node.text:
                    parent.children.append(TextBox(node.text, node.style))
                for child in node:
                    add_node(page, parent, child)
                    if child.tail:
                        parent.children.append(TextBox(child.tail, node.style)) # Note: the tail doesn't get the child's style
                return

            if node.tag == "br":
                parent.children.append(Newline(node.style))
                return

            raise ValueError("Unknown tag: %s" % node.tag)

        return add_node(None, None, node)


    def break_lines(page):
        lines = []
        for line in page.children:
            lines.append(line)
        page.children = lines

    def compute_size(fonts, box):
        toyplot.log.debug("compute size: %s", box)

        for child in box.children:
            compute_size(fonts, child)

        if isinstance(box, Page):
            box.content_width = numpy.max([child.content_width for child in box.children]) if box.children else 0
            box.content_height = numpy.sum([child.content_height for child in box.children]) if box.children else 0
        elif isinstance(box, Line):
            box.content_width = numpy.sum([child.content_width for child in box.children]) if box.children else 0
            box.content_height = numpy.max([child.content_height for child in box.children]) if box.children else 0
        elif isinstance(box, TextBox): # This must come before Box
            font = fonts.font(box.style)
            box.content_width = font.width(box.text)
            box.content_height = box.style["line-height"]
            box.text_height = font.ascent - font.descent
        elif isinstance(box, Box):
            box.content_width = numpy.sum([child.content_width for child in box.children]) if box.children else 0
            box.content_height = numpy.max([child.content_height for child in box.children]) if box.children else 0
        else:
            raise Exception("Unknown box type: %s" % box)

    def compute_layout(box, left, top):
        box.left = left
        box.top = top
        box.right = box.left + box.content_width
        box.bottom = box.top + box.content_height
        for child in box.children:
            compute_layout(child, left, top)
            if isinstance(child, Line):
                top += child.content_height
            elif isinstance(child, Box):
                left += child.content_width

    if "font-family" not in style:
        raise ValueError("style must specify font-family")
    if "font-size" not in style:
        raise ValueError("style must specify font-size")

    dom = xml.fromstring(("<body>" + text + "</body>").encode("utf-8"))

    default_style = {
        "line-height": "normal",
        "vertical-align": "baseline",
    }
    style = toyplot.style.combine(default_style, style)
    reference_font_size = toyplot.units.convert(style["font-size"], target="px", default="px")

    cascade_styles(style, dom)
    compute_styles(reference_font_size, dom)

    page = build_formatting_model(dom)
    break_lines(page)
    compute_size(fonts, page)
    compute_layout(page, left=0, top=0)

    return page


def dump(box, stream=None, text=True, style=False, location=False, size=True, level=0, indent="  "):
    if stream is None:
        stream = sys.stdout
    stream.write(indent * level)
    stream.write("%s.%s" % (box.__module__, box.__class__.__name__))
    if text and isinstance(box, TextBox):
        stream.write(" %r" % box.text)
    if style:
        stream.write(" %r" % box.style)
    if location:
        stream.write(" %s,%s" % (box.left, box.top))
    if size:
        stream.write(" %sx%s" % (box.content_width, box.content_height))
    stream.write("\n")
    for child in box.children:
        dump(box=child, stream=stream, text=text, style=style, location=location, size=size, level=level+1, indent=indent)

