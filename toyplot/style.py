# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for working with CSS style information."""


import numbers

import numpy

import toyplot.color

def require(css, allowed):
    """Validate that an object is usable as CSS style information.

    Parameters
    ----------
    css: dict or None
        The style dictionary to be validated.  An exception will be raised if it is
        not a valid style dictionary or None.
    allowed: sequence of strings
        The set of allowed style properties.  An exception will be raised if `css`
        contains any keys that aren't in this sequence.

    Returns
    -------
    style: dict
        The validated style dictionary.
    """
    if css is None:
        return css

    if not isinstance(css, dict):
        raise ValueError("Expected a dictionary of CSS styles or None, received %s." % css) # pragma: no cover

    for key, value in css.items():
        if key not in allowed:
            raise ValueError("Not an allowed CSS style: %s.  Use one of: %s" % (key, ", ".join(allowed))) # pragma: no cover
        if isinstance(value, numpy.ndarray) and value.dtype == toyplot.color.dtype:
            css[key] = toyplot.color.to_css(value)

    return css


class allowed(object):
    """Defines groups of allowable CSS property names."""

    #: Allowable CSS property names for filling areas.
    fill = set([
        "fill",
        "fill-opacity",
        "opacity",
        "stroke",
        "stroke-dasharray",
        "stroke-opacity",
        "stroke-width",
        ])

    #: Allowable CSS property names for stroking lines.
    line = set([
        "opacity",
        "stroke",
        "stroke-dasharray",
        "stroke-linecap",
        "stroke-opacity",
        "stroke-width",
        ])

    #: Allowable CSS property names for :ref:`markers`.
    marker = set([
        "fill",
        "fill-opacity",
        "opacity",
        "stroke",
        "stroke-opacity",
        "stroke-width",
        ])

    #: Allowable CSS property names for text.
    text = set([
        "alignment-baseline",
        "baseline-shift",
        "fill",
        "fill-opacity",
        "font-family",
        "font-size",
        "font-weight",
        "line-height",
        "opacity",
        "stroke",
        "stroke-opacity",
        "stroke-width",
        "text-anchor",
        "text-decoration-line",
        "text-shadow",
        "-toyplot-anchor-shift",
        "-toyplot-text-layout-box-visibility",
        "-toyplot-text-layout-line-visibility",
        "-toyplot-text-layout-visibility",
        "-toyplot-vertical-align",
        ])

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
    """Convert one-or-more dicts containing CSS properties into a single CSS string."""
    declarations = []
    for key, value in sorted( _color_fixup(combine(*styles)).items()):
        if isinstance(value, numbers.Number):
            value = "{:.6g}".format(value)
        declarations.append("%s:%s" % (key, value))
    return ";".join(declarations)
