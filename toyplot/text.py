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
import toyplot.font
import toyplot.require
import toyplot.style
import toyplot.transform
import toyplot.units


def extents(text, angle, style):
    """Compute canvas coordinate extents for a text string, based on the given angle and style.
    """
    text = toyplot.require.string_vector(text)
    angle = toyplot.require.scalar_vector(angle)
    style = toyplot.require.style(style, toyplot.require.style.text)

    # TODO: don't hard-code this.
    fonts = toyplot.font.ReportlabLibrary()

    layouts = numpy.array([toyplot.text.layout(string, style, fonts) for string in text])
    left = numpy.array([layout.left for layout in layouts])
    right = numpy.array([layout.right for layout in layouts])
    top = numpy.array([layout.top for layout in layouts])
    bottom = numpy.array([layout.bottom for layout in layouts])

    corner1 = numpy.column_stack((left, top))
    corner2 = numpy.column_stack((right, top))
    corner3 = numpy.column_stack((right, bottom))
    corner4 = numpy.column_stack((left, bottom))

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
    top = -numpy.maximum(corner1.T[1], numpy.maximum(
        corner2.T[1], numpy.maximum(corner3.T[1], corner4.T[1])))
    bottom = -numpy.minimum(corner1.T[1], numpy.minimum(
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
    """Container for a block of text that shares a single style."""
    def __init__(self, text, style):
        self.text = text
        self.style = style


class _LineBreak(object):
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

        toyplot_anchor_shift = node.style["-toyplot-anchor-shift"]
        toyplot_anchor_shift = toyplot.units.convert(toyplot_anchor_shift, target="px", default="px", reference=reference_font_size)

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
        node.style["-toyplot-anchor-shift"] = toyplot_anchor_shift

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
            root.children.append(_LineBreak())
            return root

        raise ValueError("Unknown tag: %s" % node.tag)

    def split_lines(layout):
        """Convert a flat layout into a two level hierarchy of line boxes containing text boxes."""
        children = []
        for child in layout.children:
            if isinstance(child, _LineBreak):
                children.append(LineBox())
            else:
                if not children:
                    children.append(LineBox())
                children[-1].children.append(child)
        layout.children = children

    def compute_size(fonts, layout):
        """Compute width + height for the layout + line boxes + text boxes."""
        for line in layout.children:
            for box in line.children:
                if isinstance(box, TextBox):
                    font = fonts.font(box.style)
                    box.width = font.width(box.text)

                    # Box baseline is the relative offset from the line baseline in canvas coordinates
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

#                    text_height = box.bottom - box.top
#                    line_height = box.style["line-height"]
#                    line_extra = (line_height - text_height) * 0.5
#                    if line_extra > 0:
#                        box.top -= line_extra
#                        box.bottom += line_extra

                    box.height = box.bottom - box.top
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
        #current_baseline = -layout.height * 0.5
        # ... align the top of the layout with the anchor, or ...
        #current_baseline = 0
        # ... align the bottom of the layout with the anchor, or ...
        #current_baseline = -layout.height
        # ... align the first line's baseline with the anchor.
        current_baseline = 0

        # Layout top is the relative offset from the layout anchor in canvas coordinates (positive = down)
        layout.top = current_baseline

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
            line.top += current_baseline
            line.baseline = current_baseline
            line.bottom += current_baseline

            for child in line.children:
                # Child left/right/bottom/top are relative offsets from the layout anchor in canvas coordinates.
                child.left = current_x + child.style["-toyplot-anchor-shift"]
                child.right = child.left + child.width
                child.top += current_baseline
                child.baseline += current_baseline
                child.bottom += current_baseline
                # Note that baseline-shift is the opposite of canvas coordinates (positive values shift UP)
                child.baseline -= child.style["baseline-shift"]

                current_x += child.width
            current_baseline += line.height

        # Layout left/right/bottom are relative offsets from the layout anchor in canvas coordinates
        layout.bottom = current_baseline
        layout.left = numpy.min([line.left for line in layout.children]) if layout.children else 0
        layout.right = numpy.max([line.right for line in layout.children]) if layout.children else 0

    def cleanup_styles(layout):
        """Remove style properties that we don't want rendered (because their effect is already baked into box positions."""
        for line in layout.children:
            for child in line.children:
                child.style.pop("-toyplot-anchor-shift", None)
                child.style.pop("alignment-baseline", None)
                child.style.pop("baseline-shift", None)
                child.style.pop("text-anchor", None)

    dom = xml.fromstring(("<body>" + text + "</body>").encode("utf-8"))

    default_style = {
        "-toyplot-anchor-shift": "0",
        "alignment-baseline": "middle",
        "baseline-shift": "0",
        "font-family": "helvetica",
        "font-size": "12px",
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


def dump(box, stream=None, level=0, indent="  ", recursive=True):
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

    if recursive and hasattr(box, "children"):
        for child in box.children:
            dump(box=child, stream=stream, level=level+1, indent=indent)

