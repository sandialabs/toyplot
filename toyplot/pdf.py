# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import absolute_import

import cairo
import numpy
import toyplot.svg
import toyplot.cairo

def render(canvas, fobj, width=None, height=None, scale=None):
  """Render the PDF representation of a canvas.

  By default, canvas drawing units are mapped directly to points in the output
  PNG image.  Use one of `width`, `height`, or `scale` to override this behavior.

  Parameters
  ----------
  canvas : :class:`toyplot.Canvas`
    Canvas to be rendered.
  fobj : file-like object or string
    The file to write.  Use a string filepath to write data directly to disk.
  width : number or (number, string) tuple, optional
    Specify the width of the output image with optional units.  If the units
    aren't specified, defaults to points.
  height : number or (number, string) tuple, optional
    Specify the height of the output image with optional units.  If the units
    aren't specified, defaults to points.
  scale : number, optional
    Ratio of output image points to `canvas` drawing units.

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

