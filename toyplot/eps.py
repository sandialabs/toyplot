# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import absolute_import

import cairo
import toyplot.cairo
import toyplot.svg

def render(canvas, fobj, width=None, height=None, scale=None):
  """Render the Encapsulated Postscript representation of a canvas.

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

  >>> toyplot.eps.render(canvas, "figure-1.eps", width=(4.5, "inches"))

  Notes
  -----
  When you specify `width` or `height` the output EPS file may have a smaller
  bounding-box than expected.  This is because `width` and `height` specify the
  desired dimensions of the *canvas*, while the output EPS file bounding box
  tightly bounds only the visible parts of the graphic.  A Toyplot canvas is
  transparent by default, and thus wouldn't be included in the EPS bounding
  box, unless explicitly made visible with the "background-color" style.
  """
  svg = toyplot.svg.render(canvas)
  scale = canvas._point_scale(width=width, height=height, scale=scale)
  surface = cairo.PSSurface(fobj, scale * canvas._width, scale * canvas._height)
  surface.set_eps(True)
  context = cairo.Context(surface)
  context.scale(scale, scale)
  toyplot.cairo.render(svg, context)
  surface.flush()
  surface.finish()

