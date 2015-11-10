# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generate PNG images using Qt.
"""

from __future__ import absolute_import
from __future__ import division

import toyplot.compatibility
import toyplot.qt
import toyplot.svg
import xml.etree.ElementTree as xml


def render(canvas, fobj=None, width=None, height=None, scale=None):
    """Render the PNG representation of a canvas using Qt.

    Because the canvas dimensions in CSS pixels are mapped directly to pixels
    in the output PNG image.  Use one of `width`, `height`, or `scale` to
    override this behavior.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      Canvas to be rendered.
    fobj: file-like object or string, optional
      The file to write.  Use a string filepath to write data directly to disk.
      If `None` (the default), the PNG data will be returned to the caller
      instead.
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

    Returns
    -------
    png: PNG image data, or `None`
      PNG representation of `canvas`, or `None` if the caller specifies the
      `fobj` parameter.

    Examples
    --------

    >>> toyplot.pdf.render(canvas, "figure-1.pdf", width=(4, "inches"))
    """
    qapplication = toyplot.qt.application()

    scale = canvas.pixel_scale(width=width, height=height, scale=scale)
    width = canvas.width * scale
    height = canvas.height * scale

    svg = toyplot.svg.render(canvas)

    page = toyplot.qt.QWebPage()
    page.mainFrame().setHtml(xml.tostring(svg, method="html"))
    page.setViewportSize(page.mainFrame().contentsSize())

    image = toyplot.qt.QImage(width, height, toyplot.qt.QImage.Format_ARGB32)
    painter = toyplot.qt.QPainter(image)
    painter.scale(scale, scale)
    page.mainFrame().render(painter)
    painter.end()

    if isinstance(fobj, toyplot.compatibility.string_type):
        image.save(fobj, "PNG")
    else:
        storage = toyplot.qt.QByteArray()
        stream = toyplot.qt.QBuffer(storage)
        stream.open(toyplot.qt.QIODevice.WriteOnly)
        image.save(stream, "PNG")
        if fobj is None:
            return storage.data()
        else:
            fobj.write(storage.data())

