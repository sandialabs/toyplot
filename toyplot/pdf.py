# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import absolute_import
from __future__ import division


import cairo
import numpy
import toyplot.svg
import toyplot.cairo

def render(canvas, fobj, width=None, height=None, scale=None):
  """Render the PDF representation of a canvas.

  Because the canvas dimensions are specified explicitly at creation time, they
  map directly to real-world units in the output PDF image.  Use one of
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

  Examples
  --------

  >>> toyplot.pdf.render(canvas, "figure-1.pdf", width=(4, "inches"))

  Notes
  -----
  The output PDF is rendered using an SVG representation of the canvas
  generated with :func:`toyplot.svg.render()`.
  """
  svg = toyplot.svg.render(canvas)
  scale = canvas._point_scale(width=width, height=height, scale=scale)
  surface = cairo.PDFSurface(fobj, scale * canvas._width, scale * canvas._height)
  context = cairo.Context(surface)
  context.scale(scale, scale)
  toyplot.cairo.render(svg, context)
  surface.flush()
  surface.finish()

