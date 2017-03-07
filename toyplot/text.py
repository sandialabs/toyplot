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


class Layout(object):
    """Top-level container for one-or-more lines of text."""
    def __init__(self):
        self.children = []


class LineBox(object):
    """Container for one line of text."""
    def __init__(self):
        self.children = []


class TextBox(object):
    """Container for text."""
    def __init__(self, text, style):
        self.text = text
        self.style = style


class LineBreak(object):
    """Representation for a single line break."""
    pass


def layout(text, style, fonts):
    def cascade_styles(style, node):
        """Cascades style information so that each node in an XML DOM has an explicit representation of each property/value pair."""
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
        """Compute explicit numeric CSS pixel values for the baseline-shift, font-size, line-height, and -toyplot-text-anchor-shift properties."""
        font_size = node.style["font-size"]
        font_size = toyplot.units.convert(font_size, target="px", default="px", reference=reference_font_size)

        baseline_shift = node.style["baseline-shift"]
        baseline_shift = toyplot.units.convert(baseline_shift, target="px", default="px", reference=reference_font_size)

        toyplot_text_anchor_shift = node.style["-toyplot-text-anchor-shift"]
        toyplot_text_anchor_shift = toyplot.units.convert(toyplot_text_anchor_shift, target="px", default="px", reference=reference_font_size)

        # Note that baseline shift is the opposite of canvas coordinates (positive values shift UP)
        if node.tag == "small":
            font_size *= 0.8
        elif node.tag == "sub":
            font_size *= 0.7
            baseline_shift -= 0.2 * font_size
        elif node.tag == "sup":
            font_size *= 0.7
            baseline_shift += 0.3 * font_size

        line_height = node.style["line-height"]
        if line_height == "normal":
            line_height = "120%"
        line_height = toyplot.units.convert(line_height, target="px", default="px", reference=font_size)

        node.style["baseline-shift"] = baseline_shift
        node.style["font-size"] = font_size
        node.style["line-height"] = line_height
        node.style["-toyplot-text-anchor-shift"] = toyplot_text_anchor_shift

        for child in node:
            compute_styles(font_size, child)

    def build_formatting_model(node, root=None):
        """Convert the XML DOM into a flat layout containing text boxes and line breaks."""
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
            root.children.append(LineBreak())
            return root

        raise ValueError("Unknown tag: %s" % node.tag)

    def split_lines(layout):
        """Convert a flat layout into a two level hierarchy of line boxes containing text boxes."""
        children = layout.children
        layout.children = [LineBox()]
        for child in children:
            if isinstance(child, LineBreak):
                layout.children.append(LineBox())
            else:
                layout.children[-1].children.append(child)

    def compute_size(fonts, layout):
        """Compute width + height for the layout + line boxes + text boxes."""
        for line in layout.children:
            for box in line.children:
                if isinstance(box, TextBox):
                    font = fonts.font(box.style)
                    box.width = font.width(box.text)

                    # Box baseline is its relative offset from the line baseline in canvas coordinates
                    alignment_baseline = box.style["alignment-baseline"]
                    if alignment_baseline == "alphabetic":
                        box.baseline = 0
                    elif alignment_baseline == "central":
                        box.baseline = font.ascent * 0.5
                    elif alignment_baseline == "hanging":
                        box.baseline = font.ascent
                    elif alignment_baseline == "middle":
                        box.baseline = font.ascent * 0.35
                    else:
                        raise ValueError("Unknown alignment-baseline: %s" % alignment_baseline)

                    # Box top is the relative offset from the line baseline in canvas coordinates
                    box.top = box.baseline - font.ascent
                    # Box bottom is the relative offset from the line baseline in canvas coordinates
                    box.bottom = box.baseline - font.descent

                    text_height = box.bottom - box.top
                    line_height = box.style["line-height"]
                    line_extra = (line_height - text_height) * 0.5
                    if line_extra > 0:
                        box.top -= line_extra
                        box.bottom += line_extra
                else:
                    raise Exception("Unexpected box type: %s" % box)

            line.width = numpy.sum([child.width for child in line.children]) if line.children else 0
            # Line top is the relative offset from the line baseline in canvas coordinates
            line.top = numpy.min([child.top for child in line.children]) if line.children else 0
            # Line bottom is the relative offset from the line baseline in canvas coordinates
            line.bottom = numpy.max([child.bottom for child in line.children]) if line.children else 0
            line.height = line.bottom - line.top

        layout.width = numpy.max([line.width for line in layout.children]) if layout.children else 0
        layout.height = numpy.sum([line.height for line in layout.children]) if layout.children else 0


    def compute_position(layout):
        """Compute top + bottom + left + right coordinates for line boxes + text boxes, relative to the layout anchor."""

        # Center the layout vertically on the anchor, or ...
        #current_y = -layout.height * 0.5
        # ... align the top of the layout with the anchor, or ...
        #current_y = 0
        # ... align the bottom of the layout with the anchor, or ...
        #current_y = -layout.height
        # ... align the first line's baseline with the anchor.
        current_y = layout.children[0].top

        # Layout top is the relative offset from the layout anchor in canvas coordinates (positive = down)
        layout.top = current_y

        for line in layout.children:
            text_anchor = line.children[-1].style.get("text-anchor", "middle") if line.children else "middle"
            if text_anchor == "start":
                anchor_offset = 0
            elif text_anchor == "middle":
                anchor_offset = -line.width * 0.5
            elif text_anchor == "end":
                anchor_offset = -line.width

            current_x = anchor_offset

            # Line left/right/bottom/top are relative offsets from the layout anchor in canvas coordinates.
            line.left = current_x
            line.right = current_x + line.width
            line.baseline = current_y - line.top
            line.top += line.baseline
            line.bottom += line.baseline

            for child in line.children:
                # Child left/right/bottom/top are relative offsets from the layout anchor in canvas coordinates.
                child.left = current_x + child.style["-toyplot-text-anchor-shift"]
                child.right = child.left + child.width
                # Note that baseline-shift is the opposite of canvas coordinates (positive values shift UP)
                child.baseline = line.baseline + child.baseline - child.style["baseline-shift"]
                child.top += child.baseline
                child.bottom += child.baseline
                current_x += child.width
            current_y += line.height

        # Layout left/right/bottom are relative offsets from the layout anchor in canvas coordinates
        layout.bottom = current_y
        layout.left = numpy.min([line.left for line in layout.children]) if layout.children else 0
        layout.right = numpy.max([line.right for line in layout.children]) if layout.children else 0

    def cleanup_styles(layout):
        """Remove style properties that we don't want rendered (because their effect is already baked into box positions."""
        for line in layout.children:
            for child in line.children:
                child.style.pop("-toyplot-text-anchor-shift", None)
                child.style.pop("alignment-baseline", None)
                child.style.pop("baseline-shift", None)
                child.style.pop("text-anchor", None)

    if "font-family" not in style:
        raise ValueError("style must specify font-family")
    if "font-size" not in style:
        raise ValueError("style must specify font-size")

    dom = xml.fromstring(("<body>" + text + "</body>").encode("utf-8"))

    default_style = {
        "-toyplot-text-anchor-shift": "0",
        "alignment-baseline": "middle",
        "baseline-shift": "0",
        "line-height": "normal",
        "text-anchor": "middle",
        "vertical-align": "baseline",
        "white-space": "pre",
    }
    style = toyplot.style.combine(default_style, style)
    reference_font_size = toyplot.units.convert(style["font-size"], target="px", default="px")

    cascade_styles(style, dom)
    compute_styles(reference_font_size, dom)

    root = build_formatting_model(dom)
    split_lines(root)
    compute_size(fonts, root)
    compute_position(root)
    cleanup_styles(root)

    return root


def dump(box, stream=None, level=0, indent="  "):
    if stream is None:
        stream = sys.stdout
    stream.write(indent * level)
    stream.write("%s.%s\n" % (box.__module__, box.__class__.__name__))

    for key, value in sorted(box.__dict__.items()):
        if key in ["children"]:
            continue
        if key == "style":
            stream.write(indent * (level + 1))
            stream.write("style:\n")
            for pair in box.style.items():
                stream.write(indent * (level + 2))
                stream.write("%s: %s\n" % pair)
        elif key in ["text"]:
            stream.write(indent * (level + 1))
            stream.write("%s: %r\n" % (key, value))
        else:
            stream.write(indent * (level + 1))
            stream.write("%s: %s\n" % (key, value))

    stream.write("\n")

    if hasattr(box, "children"):
        for child in box.children:
            dump(box=child, stream=stream, level=level+1, indent=indent)

