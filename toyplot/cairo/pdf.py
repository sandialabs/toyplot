# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generate PDF documents using Cairo."""

from __future__ import absolute_import
from __future__ import division


import cairo
import toyplot.svg
import toyplot.cairo


try:
    import cStringIO as StringIO
except:  # pragma: no cover
    import StringIO


def render(canvas, fobj=None, width=None, height=None, scale=None):
    """Render the PDF representation of a canvas using Cairo.

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
    svg = toyplot.svg.render(canvas)
    scale = canvas._point_scale(width=width, height=height, scale=scale)
    if fobj is None:
        stream = StringIO.StringIO()
        surface = cairo.PDFSurface(
            stream, scale * canvas.width, scale * canvas.height)
    else:
        surface = cairo.PDFSurface(
            fobj, scale * canvas.width, scale * canvas.height)
    context = cairo.Context(surface)
    context.scale(scale, scale)
    toyplot.cairo.render(svg, context)
    surface.flush()
    surface.finish()
    if fobj is None:
        return stream.getvalue()
