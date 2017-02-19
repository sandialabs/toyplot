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


class Box(object):
    """Generic container for all content."""
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children


class Layout(Box):
    """Top-level container for one-or-more lines of text."""
    def __init__(self):
        super(Layout, self).__init__()


class LineBox(Box):
    """Container for one line of text."""
    def __init__(self, children=None):
        super(LineBox, self).__init__(children=children)


class TextBox(Box):
    """Container for text."""
    def __init__(self, text, style):
        super(TextBox, self).__init__()
        self.text = text
        self.style = style


class Newline(Box):
    """Representation for a single line break."""
    def __init__(self):
        super(Newline, self).__init__()


def layout(text, style, fonts):
    def cascade_styles(style, node):
        if node.tag in ["b", "strong"]:
            style = toyplot.style.combine(style, {"font-weight": "bold"})
        elif node.tag in ["code"]:
            style = toyplot.style.combine(style, {"font-family": "monospace"})
        elif node.tag in ["em", "i"]:
            style = toyplot.style.combine(style, {"font-style": "italic"})

        if "style" in node.attrib:
            node_style = toyplot.require.style(toyplot.style.parse(node.attrib["style"]), toyplot.require.style.text)
            style = toyplot.style.combine(style, node_style)

        node.style = copy.deepcopy(style)
        for child in node:
            cascade_styles(style, child)

    def compute_styles(reference_font_size, node):
        font_size = node.style["font-size"]
        font_size = toyplot.units.convert(font_size, target="px", default="px", reference=reference_font_size)

        baseline_shift = node.style["baseline-shift"]
        baseline_shift = toyplot.units.convert(baseline_shift, target="px", default="px", reference=reference_font_size)

        if node.tag == "small":
            font_size *= 0.8
        elif node.tag == "sub":
            font_size *= 0.7
            baseline_shift += 0.2 * font_size
        elif node.tag == "sup":
            font_size *= 0.7
            baseline_shift -= 0.3 * font_size

        line_height = node.style["line-height"]
        if line_height == "normal":
            line_height = "120%"
        line_height = toyplot.units.convert(line_height, target="px", default="px", reference=font_size)

        node.style["baseline-shift"] = baseline_shift
        node.style["font-size"] = font_size
        node.style["line-height"] = line_height

        #toyplot.log.debug("%s %s %r %r", node.tag, node.style, node.text, node.tail)
        for child in node:
            compute_styles(font_size, child)

    def build_formatting_model(node, root=None):
        #toyplot.log.debug("build formatting model: %s", node)

        if node.tag == "body":
            root = Layout()

        if node.tag in ["body", "b", "code", "i", "em", "small", "span", "strong", "sub", "sup"]:
            if node.text:
                root.children.append(TextBox(node.text, node.style))
            for child in node:
                build_formatting_model(child, root)
                if child.tail:
                    root.children.append(TextBox(child.tail, node.style)) # Note: the tail doesn't get the child's style
            return root

        if node.tag == "br":
            root.children.append(Newline())
            return root

        raise ValueError("Unknown tag: %s" % node.tag)

    def create_lines(root):
        #toyplot.log.debug("create lines")
        children = root.children
        root.children = [LineBox()]
        for child in children:
            if isinstance(child, Newline):
                root.children.append(LineBox())
            else:
                root.children[-1].children.append(child)

    def compute_size(fonts, box):
        #toyplot.log.debug("compute size: %s", box)

        for child in box.children:
            compute_size(fonts, child)

        if isinstance(box, Layout):
            box.width = numpy.max([child.width for child in box.children]) if box.children else 0
            box.height = numpy.sum([child.height for child in box.children]) if box.children else 0
        elif isinstance(box, LineBox):
            box.width = numpy.sum([child.width for child in box.children]) if box.children else 0
            box.height = numpy.max([child.height for child in box.children]) if box.children else 0
        elif isinstance(box, TextBox): # This must come before Box
            font = fonts.font(box.style)
            box.width = font.width(box.text)
            box.height = box.style["line-height"]
            box.baseline = (box.height - (font.ascent - font.descent)) * 0.5
        elif isinstance(box, Box):
            box.width = numpy.sum([child.width for child in box.children]) if box.children else 0
            box.height = numpy.max([child.height for child in box.children]) if box.children else 0
        else:
            raise Exception("Unexpected box type: %s" % box)

    def compute_position(root):
        left = 0
        top = 0

        root.left = left
        root.top = top
        root.right = root.left + root.width
        root.bottom = root.top + root.height

        top = 0
        for line in root.children:
            left = 0
            line.left = left
            line.top = top
            line.right = line.left + line.width
            line.bottom = line.top + line.height

            for child in line.children:
                child.left = left
                child.top = top
                child.right = child.left + child.width
                child.bottom = child.top + line.height
                left += child.width
            top += line.height

    def compute_baseline(fonts, root):
        for line in root.children:
            baseline = numpy.min([child.baseline for child in line.children]) if line.children else 0
            for child in line.children:
                child.baseline = baseline - child.style["baseline-shift"]
        for line in root.children:
            for child in line.children:
                child.style.pop("baseline-shift", None)

    if "font-family" not in style:
        raise ValueError("style must specify font-family")
    if "font-size" not in style:
        raise ValueError("style must specify font-size")

    dom = xml.fromstring(("<body>" + text + "</body>").encode("utf-8"))

    default_style = {
        "baseline-shift": "0",
        "line-height": "normal",
        "vertical-align": "baseline",
    }
    style = toyplot.style.combine(default_style, style)
    reference_font_size = toyplot.units.convert(style["font-size"], target="px", default="px")

    cascade_styles(style, dom)
    compute_styles(reference_font_size, dom)

    root = build_formatting_model(dom)
    create_lines(root)
    compute_size(fonts, root)
    compute_position(root)
    compute_baseline(fonts, root)

    return root


def dump(box, stream=None, text=True, style=False, location=False, size=True, level=0, indent="  "):
    if stream is None:
        stream = sys.stdout
    stream.write(indent * level)
    stream.write("%s.%s" % (box.__module__, box.__class__.__name__))
    if text and isinstance(box, TextBox):
        stream.write(" %r" % box.text)
    if style and hasattr(box, "style"):
        stream.write(" %r" % box.style)
    if location:
        stream.write(" %s,%s" % (box.left, box.top))
    if size and hasattr(box, "width") and hasattr(box, "height"):
        stream.write(" %sx%s" % (box.width, box.height))
    stream.write("\n")
    for child in box.children:
        dump(box=child, stream=stream, text=text, style=style, location=location, size=size, level=level+1, indent=indent)

