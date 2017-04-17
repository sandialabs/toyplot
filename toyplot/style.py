# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for working with CSS style information."""

from __future__ import division

import toyplot.color

def combine(*styles):
    """Combine multiple style specifications into one.

    Parameters
    ----------
    styles: sequence of :class:`dict` instances
        A collection of dicts containing CSS-compatible name-value pairs.

    Returns
    -------
    styles: :class:`dict` containing CSS-compatible name-value pairs.
    """
    computed_style = {}
    for style in styles:
        if style is not None:
            computed_style.update(style)
    return computed_style

def parse(css):
    """Parse a CSS style into a dict."""
    result = {}
    for declaration in css.split(";"):
        if declaration:
            key, value = declaration.split(":")
            result[key] = value.strip()
    return result

def _color_fixup(styles):
    """It turns-out that many applications and libraries (Inkscape, Adobe Illustrator, Qt)
    don't handle CSS rgba() colors correctly.  So convert them to CSS rgb colors and use
    fill-opacity / stroke-opacity instead."""

    if "fill" in styles:
        color = toyplot.color.css(styles["fill"])
        if color is not None:
            opacity = float(styles.get("fill-opacity", 1.0))
            styles["fill"] = "rgb(%.3g%%,%.3g%%,%.3g%%)" % (
                color["r"] * 100, color["g"] * 100, color["b"] * 100)
            styles["fill-opacity"] = str(color["a"] * opacity)
    if "stroke" in styles:
        color = toyplot.color.css(styles["stroke"])
        if color is not None:
            opacity = float(styles.get("stroke-opacity", 1.0))
            styles["stroke"] = "rgb(%.3g%%,%.3g%%,%.3g%%)" % (
                color["r"] * 100, color["g"] * 100, color["b"] * 100)
            styles["stroke-opacity"] = str(color["a"] * opacity)

    return styles

def to_css(*styles):
    style = _color_fixup(combine(*styles))
    return ";".join(["%s:%s" % (key, value) for key, value in sorted(style.items())])
