# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generate PDF documents using Qt.
"""

from __future__ import absolute_import
from __future__ import division

import toyplot.compatibility
import toyplot.qt
import toyplot.svg
import xml.etree.ElementTree as xml


def render(canvas, fobj=None, width=None, height=None, scale=None):
    """Render the PDF representation of a canvas using Qt.

    Because the canvas dimensions are specified explicitly at creation time, they
    map directly to real-world units in the output PDF image.  Use one of
    `width`, `height`, or `scale` to override this behavior.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      Canvas to be rendered.
    fobj: file-like object or string
      The file to write.  Use a string filepath to write data directly to disk.
      If `None` (the default), the PDF data will be returned to the caller
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
    pdf: PDF data, or `None`
      PDF representation of `canvas`, or `None` if the caller specifies the
      `fobj` parameter.

    Examples
    --------

    >>> toyplot.pdf.render(canvas, "figure-1.pdf", width=(4, "inches"))
    """
    qapplication = toyplot.qt.application()

    scale = canvas.pixel_scale(width=width, height=height, scale=scale)
    width = canvas.width * scale
    height = canvas.height * scale

    page = toyplot.qt.QWebPage()
    page.mainFrame().setContent(xml.tostring(toyplot.svg.render(canvas)), "image/svg+xml")
    page.setViewportSize(page.mainFrame().contentsSize())

    page_size = toyplot.qt.QPageSize(
        toyplot.qt.QSizeF(
            toyplot.units.convert((width, "px"), "pt"),
            toyplot.units.convert((height, "px"), "pt")),
        toyplot.qt.QPageSize.Point,
        matchPolicy=toyplot.qt.QPageSize.ExactMatch)

    page_layout = toyplot.qt.QPageLayout(
        page_size,
        toyplot.qt.QPageLayout.Portrait,
        toyplot.qt.QMarginsF(0, 0, 0, 0),
        )

    if isinstance(fobj, toyplot.compatibility.string_type):
        pdf = toyplot.qt.QPdfWriter(fobj)
    else:
        storage = toyplot.qt.QByteArray()
        stream = toyplot.qt.QBuffer(storage)
        stream.open(toyplot.qt.QIODevice.WriteOnly)
        pdf = toyplot.qt.QPdfWriter(stream)

    pdf.setPageLayout(page_layout)
    pdf.setResolution(96) # CSS pixels per inch

    painter = toyplot.qt.QPainter(pdf)
    painter.scale(scale, scale)
    page.mainFrame().render(painter)
    painter.end()

    if isinstance(fobj, toyplot.compatibility.string_type):
        pass
    else:
        if fobj is None:
            return storage.data()
        else:
            fobj.write(storage.data())

