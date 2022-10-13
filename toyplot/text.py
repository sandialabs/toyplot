# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functions for manipulating text."""


import copy
import sys
import xml.etree.ElementTree as xml

import numpy

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
    style = toyplot.style.require(style, toyplot.style.allowed.text)

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
        corner1[index] = numpy.matmul(corner1[index], transformation)
        corner2[index] = numpy.matmul(corner2[index], transformation)
        corner3[index] = numpy.matmul(corner3[index], transformation)
        corner4[index] = numpy.matmul(corner4[index], transformation)

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
    def __init__(self, style):
        self.style = style
        self.children = []


class LineBox(object):
    """Container for one line of text."""
    def __init__(self, style):
        self.style = style
        self.children = []


class TextBox(object):
    """Container for a block of text that shares a single style."""
    def __init__(self, text, style):
        self.text = text
        self.style = style


class MarkerBox(object):
    """Container for a Toyplot marker specification."""
    def __init__(self, marker, style):
        self.marker = marker
        self.style = style


class PushHyperlink(object):
    """Marks the beginning of a hyperlink."""
    def __init__(self, href, target, style):
        self.href = href
        self.target = target
        self.style = style


class PopHyperlink(object):
    """Marks the end of a hyperlink."""
    def __init__(self, style):
        self.style = style


class _LineBreak(object):
    """Marks the position of a line break."""
    pass


def layout(text, style, fonts):
    """Convert text with markup into a layout that is ready to be rendered.

    Parameters
    ----------
    text: string, required
        Text with markup to be converted.
    style: dict, required
        Collection of CSS properties to be used as defaults for the text layout.
    fonts: :class:`toyplot.font.Library`, required
        Font library that will supply font information for the text layout.

    Returns
    -------
    layout: :class:`toyplot.text.Layout`
        The text layout contains a hierarchy of styled, positiioned nodes that
        are ready to be rendered.
    """
    def cascade_styles(style, node):
        """Cascades style information so that each node in an XML DOM has an explicit representation of each property/value pair."""
        if node.tag in ["b", "strong"]:
            style = toyplot.style.combine(style, {"font-weight": "bold"})
        elif node.tag in ["code"]:
            style = toyplot.style.combine(style, {"font-family": "monospace"})
        elif node.tag in ["em", "i"]:
            style = toyplot.style.combine(style, {"font-style": "italic"})
        elif node.tag in ["a"]:
            style = toyplot.style.combine(style, {"fill": "steelblue", "text-decoration-line": "none"})

        if "style" in node.attrib:
            node_style = toyplot.style.require(toyplot.style.parse(node.attrib["style"]), toyplot.style.allowed.text)
            style = toyplot.style.combine(style, node_style)

        node.set("style", copy.deepcopy(style))
        for child in node:
            cascade_styles(style, child)

    def compute_styles(reference_font_size, node):
        """Compute explicit numeric CSS pixel values for the baseline-shift, font-size, line-height, and -toyplot-text-anchor-shift properties."""
        font_size = node.get("style")["font-size"]
        font_size = toyplot.units.convert(font_size, target="px", default="px", reference=reference_font_size)

        baseline_shift = node.get("style")["baseline-shift"]
        baseline_shift = toyplot.units.convert(baseline_shift, target="px", default="px", reference=reference_font_size)

        toyplot_anchor_shift = node.get("style")["-toyplot-anchor-shift"]
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

        line_height = node.get("style")["line-height"]
        if line_height == "normal":
            line_height = "120%"
        line_height = toyplot.units.convert(line_height, target="px", default="px", reference=font_size)

        node.get("style")["baseline-shift"] = baseline_shift
        node.get("style")["font-size"] = "%spx" % font_size
        node.get("style")["line-height"] = line_height
        node.get("style")["-toyplot-anchor-shift"] = toyplot_anchor_shift

        for child in node:
            compute_styles(font_size, child)

    def build_formatting_model(node, root=None):
        """Convert the XML DOM into a flat layout containing text boxes and line breaks."""
        if node.tag == "body":
            root = Layout(node.get("style"))

        if node.tag in ["body", "b", "code", "i", "em", "small", "span", "strong", "sub", "sup"]:
            if node.text:
                root.children.append(TextBox(node.text, node.get("style")))
            for child in node:
                build_formatting_model(child, root)
                if child.tail:
                    root.children.append(TextBox(child.tail, node.get("style"))) # Note: the tail doesn't get the child's style
            return root

        if node.tag == "a":
            root.children.append(PushHyperlink(node.get("href"), node.get("target", None), node.get("style")))
            if node.text:
                root.children.append(TextBox(node.text, node.get("style")))
            for child in node:
                build_formatting_model(child, root)
                if child.tail:
                    root.children.append(TextBox(child.tail, node.get("style"))) # Note: the tail doesn't get the child's style
            root.children.append(PopHyperlink(node.get("style")))
            return root

        if node.tag == "marker":
            root.children.append(MarkerBox(toyplot.marker.from_html(node), node.get("style")))
            return root

        if node.tag == "br":
            root.children.append(_LineBreak())
            return root

        raise ValueError("Unknown tag: %s" % node.tag) # pragma: no cover

    def split_lines(layout):
        """Convert a flat layout into a two level hierarchy of line boxes containing text boxes."""
        children = []
        current_line = None

        for child in layout.children:
            if isinstance(child, _LineBreak):
                current_line = None
            else:
                if current_line is None:
                    current_line = LineBox(child.style)
                    children.append(current_line)
                current_line.children.append(child)

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
                        raise ValueError("Unknown alignment-baseline value: %s" % alignment_baseline)

                    # Box top is the relative offset from the line baseline in canvas coordinates
                    box.top = box.baseline - font.ascent
                    # Box bottom is the relative offset from the line baseline in canvas coordinates
                    box.bottom = box.baseline - font.descent

                    box.height = box.bottom - box.top
                elif isinstance(box, MarkerBox):
                    font = fonts.font(box.style)

                    box.baseline = 0
                    box.top = box.baseline - font.ascent
                    box.bottom = box.baseline - font.descent
                    box.height = box.bottom - box.top
                    box.width = box.height
                elif isinstance(box, (PushHyperlink, PopHyperlink)):
                    box.baseline = 0
                    box.top = box.baseline
                    box.bottom = box.baseline
                    box.height = box.bottom - box.top
                    box.width = 0
                else:
                    raise Exception("Unexpected box type: %s" % box) # pragma: no cover

            # Line top is the relative offset from the line baseline in canvas coordinates
            line.top = numpy.min([child.top for child in line.children]) if line.children else 0
            # Line bottom is the relative offset from the line baseline in canvas coordinates
            line.bottom = numpy.max([child.bottom for child in line.children]) if line.children else 0

            actual_line_height = line.bottom - line.top
            explicit_line_height = line.style["line-height"]
            offset = (explicit_line_height - actual_line_height) * 0.5
            if offset > 0:
                line.top -= offset
                line.bottom += offset

            line.width = numpy.sum([child.width for child in line.children]) if line.children else 0
            line.height = line.bottom - line.top

        layout.height = numpy.sum([line.height for line in layout.children]) if layout.children else 0


    def compute_position(layout):
        """Compute top + bottom + left + right coordinates for line boxes + text boxes, relative to the layout anchor."""

        if layout.children:
            toyplot_vertical_align = layout.style["-toyplot-vertical-align"]
            # Align the first line's baseline with the anchor.
            if toyplot_vertical_align == "first-baseline":
                offset_y = 0
            # Align the last line's baseline with the anchor.
            elif toyplot_vertical_align == "last-baseline":
                offset_y = -(layout.height + layout.children[0].top - layout.children[-1].bottom)
            # Align the top of the layout with the anchor.
            elif toyplot_vertical_align == "top":
                offset_y = -layout.children[0].top
            # Align the middle of the layout with the anchor.
            elif toyplot_vertical_align == "middle":
                offset_y = -((layout.height * 0.5) + layout.children[0].top)
            # Align the bottom of the layout with the anchor.
            elif toyplot_vertical_align == "bottom":
                offset_y = -(layout.height + layout.children[0].top)
            else:
                raise ValueError("Unknown -toyplot-vertical-align value: %s" % toyplot_vertical_align) # pragma: no cover

            for line in layout.children:
                text_anchor = line.style["text-anchor"] if line.children else "middle"
                if text_anchor == "start":
                    anchor_offset = 0
                elif text_anchor == "middle":
                    anchor_offset = -line.width * 0.5
                elif text_anchor == "end":
                    anchor_offset = -line.width
                else:
                    raise ValueError("Unknown text-anchor value: %s" % text_anchor)
                anchor_offset += layout.style["-toyplot-anchor-shift"]

                offset_x = anchor_offset

                # Line left/right/bottom/top are relative offsets from the layout anchor in canvas coordinates.
                line.left = offset_x
                line.right = offset_x + line.width
                line.top += offset_y
                line.baseline = offset_y
                line.bottom += offset_y

                for child in line.children:
                    # Child left/right/bottom/top are relative offsets from the layout anchor in canvas coordinates.
                    child.left = offset_x
                    child.right = child.left + child.width
                    child.top += offset_y
                    child.baseline += offset_y
                    child.bottom += offset_y
                    # Note that baseline-shift is the opposite of canvas coordinates (positive values shift UP)
                    child.baseline -= child.style["baseline-shift"]

                    offset_x += child.width
                offset_y += line.height

            layout.top = layout.children[0].top
            layout.left = numpy.min([line.left for line in layout.children])
            layout.right = numpy.max([line.right for line in layout.children])
            layout.bottom = layout.children[-1].bottom

        else:
            layout.top = 0
            layout.left = 0
            layout.right = 0
            layout.bottom = 0

        # Layout top/left/right/bottom are relative offsets from the layout anchor in canvas coordinates
        layout.width = layout.right - layout.left
        layout.height = layout.bottom - layout.top


    def cleanup_styles(layout):
        """Remove style properties that we don't want rendered (because their effect is already baked into the box positions."""
        for line in layout.children:
            for child in line.children:
                child.style.pop("-toyplot-anchor-shift", None)
                child.style.pop("-toyplot-vertical-align", None)
                child.style.pop("alignment-baseline", None)
                child.style.pop("baseline-shift", None)
                child.style.pop("text-anchor", None)
                child.style.pop("line-height", None)

    dom = xml.fromstring(("<body>" + text + "</body>").encode("utf-8"))

    default_style = {
        "-toyplot-anchor-shift": "0",
        "-toyplot-vertical-align": "middle",
        "alignment-baseline": "alphabetic",
        "baseline-shift": "0",
        "fill": toyplot.color.black,
        "font-family": "helvetica",
        "font-size": "12px",
        "font-weight": "normal",
        "line-height": "normal",
        "stroke": "none",
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


def dump(box, stream=None, level=0, indent="  ", recursive=True): # pragma: no cover
    """Writes formatted text layout information to a stream.

    Parameters
    ----------
    box: :class:`toyplot.text.Layout`, :class:`toyplot.text.LineBox`, :class:`toyplot.text.TextBox`, :class:`toyplot.text.MarkerBox`, :class:`toyplot.text.PushHyperlink`, or :class:`toyplot.text.PopHyperlink`, required
        The layout object to be formatted.
    stream: file like object, optional
        The stream where formatted data will be written.  Defaults to
        :data:`sys.stdout`
    recursive: boolean, optional
        If `True`, recursively print the entire layout tree underneath `box`.
    """
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
            for pair in sorted(box.style.items()):
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
