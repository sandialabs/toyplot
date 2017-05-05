# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Font management and font metrics.
"""

from __future__ import absolute_import

import reportlab.pdfbase.pdfmetrics

import toyplot.units

class Font(object):
    """Base class for objects that can return information about a specific typeface."""
    @property
    def ascent(self):
        """Return the ascent for the given font.

        Returns
        -------
        ascent: number
            ascent of the font in CSS pixels.
        """
        raise NotImplementedError() # pragma: no cover

    @property
    def descent(self):
        """Return the descent for the given font.

        Returns
        -------
        descent: number
            descent of the font in CSS pixels.
        """
        raise NotImplementedError() # pragma: no cover

    def width(self, string):
        """Return the width of a string.

        Parameters
        ----------
        string: str
            The text to be measured.

        Returns
        -------
        width: number
            Width of the string in CSS pixels, if rendered using the given font and
            font size.
        """
        raise NotImplementedError() # pragma: no cover


class Library(object):
    """Base class for objects that can manage information about a collection of fonts."""
    def font(self, style):
        """Lookup a font using CSS style information and return a corresponding Font object.

        Parameters
        ----------
        style: dict containing CSS style information

        Returns
        -------
        font: instance of :class:`toyplot.font.Font`
        """
        raise NotImplementedError() # pragma: no cover


class ReportlabFont(Font):
    """Use Reportlab to access the metrics for a font.

    Parameters
    ----------
    font_family: str
        PDF font family to use for measurement.
    font_size: number
        Font size for the measurement.  Defaults to CSS pixel units, and
        supports all toyplot :ref:`units`.
    """
    def __init__(self, family, size):
        self._family = family
        self._size = toyplot.units.convert(size, target="pt", default="px")

        ascent, descent = reportlab.pdfbase.pdfmetrics.getAscentDescent(self._family, self._size)
        self._ascent = toyplot.units.convert(ascent, target="px", default="pt")
        self._descent = toyplot.units.convert(descent, target="px", default="pt")

    def __repr__(self):
        return "<toyplot.font.ReportlabFont family=%r size=%r ascent=%r descent=%r>" % (self._family, self._size, self.ascent, self.descent)

    @property
    def ascent(self):
        return self._ascent

    @property
    def descent(self):
        return self._descent

    def width(self, string):
        width = reportlab.pdfbase.pdfmetrics.stringWidth(string, self._family, self._size)
        width = toyplot.units.convert(width, target="px", default="pt")
        return width


class ReportlabLibrary(Library):
    """Use Reportlab to provide information about standard PDF fonts."""
    def __init__(self):
        self._cache = dict()

    def font(self, style):
        size = style["font-size"]
        bold = True if style.get("font-weight", "") == "bold" else False
        italic = True if style.get("font-style", "") == "italic" else False

        for font_family in style["font-family"].split(","):
            font_family = font_family.lower()
            if font_family not in ReportlabLibrary.font._substitutions:
                continue

            font_family = ReportlabLibrary.font._substitutions[font_family]
            key = (font_family, bold, italic, size)
            if key not in self._cache:
                family = ReportlabLibrary.font._font_table[(font_family, bold, italic)]
                self._cache[key] = ReportlabFont(family, size)

            return self._cache[key]

        raise ValueError("Unknown font family: %s" % style) # pragma: no cover

    font._substitutions = {
        "courier": "courier",
        "helvetica": "helvetica",
        "monospace": "courier",
        "sans-serif": "helvetica",
        "serif": "times",
        "times": "times",
        }

    font._font_table = {
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
