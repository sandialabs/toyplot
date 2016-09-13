# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Font management and font metrics.
"""

from __future__ import absolute_import

import reportlab.pdfbase.pdfmetrics

import toyplot.units

def family(style):
    """Extract the name of a standard PDF font family from a CSS style dict.

    Parameters
    ----------
    style: dict containing CSS key-value pairs.
    """
    if "font-family" not in style:
        raise ValueError("No font family specified: %s" % style)

    bold = True if style.get("font-weight", "") == "bold" else False
    italic = True if style.get("font-style", "") == "italic" else False
    for font_family in style["font-family"].split(","):
        font_family = font_family.lower()
        if font_family in family.substitutions:
            font_family = family.substitutions[font_family]
            return family.font_table[(font_family, bold, italic)]

    raise ValueError("Unknown font family: %s" % style) # pragma: no cover

family.font_table = {
    ("courier", False, False): "Courier",
    ("courier", True, False): "Courier-Bold",
    ("courier", False, True): "Courier-Oblique",
    ("courier", True, True): "Courier-BoldOblique",
    ("helvetica", False, False): "Helvetica",
    ("helvetica", True, False): "Helvetica-Bold",
    ("helvetica", False, True): "Helvetica-Oblique",
    ("helvetica", True, True): "Helvetica-BoldOblique",
    ("times", False, False): "Times-Roman",
    ("times", True, False): "Times-Bold",
    ("times", False, True): "Times-Italic",
    ("times", True, True): "Times-BoldItalic",
    }

family.substitutions = {
    "courier": "courier",
    "helvetica": "helvetica",
    "monospace": "courier",
    "sans-serif": "helvetica",
    "serif": "times",
    "times": "times",
    }

def string_width(string, font_family, font_size):
    """Return the width of a string.

    Parameters
    ----------
    string: str
        The text to be measured.
    font_family: str
        PDF font family to use for measurement.
    font_size: number
        Font size for the measurement.  Defaults to CSS pixel units, and
        supports all toyplot :ref:`units`.

    Returns
    -------
    width: number
        Width of the string in CSS pixels, if rendered using the given font and
        font size.
    """

    font_size = toyplot.units.convert(font_size, target="pt", default="px")
    width = reportlab.pdfbase.pdfmetrics.stringWidth(string, font_family, font_size)
    width = toyplot.units.convert(width, target="px", default="pt")
    return width

def ascent_descent(font_family, font_size):
    """Return the ascent and descent for the given font.

    Parameters
    ----------
    font_family: str
        PDF font family to use for measurement.
    font_size: number
        Font size for the measurement.  Defaults to CSS pixel units, and
        supports all toyplot :ref:`units`.

    Returns
    -------
    ascent: number
        ascent of the font in CSS pixels.
    descent: number
        descent of the font in CSS pixels.
    """
    font_size = toyplot.units.convert(font_size, target="pt", default="px")
    ascent, decent = reportlab.pdfbase.pdfmetrics.getAscentDescent(font_family, font_size)
    ascent = toyplot.units.convert(ascent, target="px", default="pt")
    descent = toyplot.units.convert(descent, target="px", default="pt")
    return width
