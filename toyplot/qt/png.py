# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import absolute_import
from __future__ import division

import toyplot.qt
import toyplot.svg
import xml.etree.ElementTree as xml


def render(canvas, fobj, width=None, height=None, scale=None):
    """Render the PNG representation of a canvas using Qt.

    Because the canvas dimensions are specified explicitly at creation time, they
    map directly to real-world units in the output PNG image.  Use one of
    `width`, `height`, or `scale` to override this behavior.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      Canvas to be rendered.
    fobj: file-like object or string
      The file to write.  Use a string filepath to write data directly to disk.
    width: number, string, or (number, string) tuple, optional
      Specify the width of the output image with optional units.  If the units
      aren't specified, defaults to points.  See :ref:`units` for details on
      unit conversion in Toyplot.
    height: number or (number, string) tuple, optional
      Specify the height of the output image with optional units.  If the units
      aren't specified, defaults to points.  See :ref:`units` for details on
      unit conversion in Toyplot.
    scale: number, optional
      Scales the output `canvas` by the given ratio.
    qapplication: :class:`QApplication`, optional
        If you're using Toyplot as part of a larger Qt application,
        pass your global QApplication instance here.  Otherwise,
        an internal QApplication instance will be created automatically.

    Examples
    --------

    >>> toyplot.pdf.render(canvas, "figure-1.pdf", width=(4, "inches"))

    Notes
    -----
    The output PDF is rendered using an SVG representation of the canvas
    generated with :func:`toyplot.svg.render()`.
    """
    qapplication = toyplot.qt.application()

    html = xml.Element("html")
    head = xml.SubElement(html, "head")
    style = xml.SubElement(head, "style")
    style.text = """body { background-color: rgba(100%, 100%, 100%, 0.0); }"""
    body = xml.SubElement(html, "body")
    body.append(toyplot.svg.render(canvas))

    scale = canvas._point_scale(width=width, height=height, scale=scale)
    #surface = cairo.PDFSurface(fobj, scale * canvas._width, scale * canvas._height)

    page = toyplot.qt.QWebPage()
    page.mainFrame().setHtml(xml.tostring(html, method="html"))
    page.setViewportSize(page.mainFrame().contentsSize())

    image = toyplot.qt.QImage(page.viewportSize(), toyplot.qt.QImage.Format_ARGB32)
    painter = toyplot.qt.QPainter(image)
    page.mainFrame().render(painter)
    painter.end()
    image.save(fobj)
