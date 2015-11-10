# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generate Encapsulated Postscript files using Cairo."""

from __future__ import absolute_import
from __future__ import division


import cairo
import toyplot.cairo
import toyplot.svg

try:
    import cStringIO as StringIO
except:  # pragma: no cover
    import StringIO


def render(canvas, fobj=None, width=None, height=None, scale=None):
    """Render the Encapsulated Postscript representation of a canvas using
    Cairo.

    Because the canvas dimensions are explicitly specified when it's created,
    they map directly to real-world units in the output EPS image.  Use one of
    `width`, `height`, or `scale` to override this behavior.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      Canvas to be rendered.
    fobj: file-like object or string
      The file to write.  Use a string filepath to write data directly to disk.
      If `None` (the default), the EPS data will be returned to the caller
      instead.
    width: number, string, or (number, string) tuple, optional
      Specify the width of the output image with optional units.  If the units
      aren't specified, defaults to points.  See :ref:`units` for details on
      unit conversion in Toyplot.
    height: number, string, or (number, string) tuple, optional
      Specify the height of the output image with optional units.  If the units
      aren't specified, defaults to points.  See :ref:`units` for details on
      unit conversion in Toyplot.
    scale: number, optional
      Scales the output `canvas` by the given ratio.

    Returns
    -------
    eps: EPS image data, or `None`
      EPS representation of `canvas`, or `None` if the caller specifies the
      `fobj` parameter.

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
    if fobj is None:
        stream = StringIO.StringIO()
        surface = cairo.PSSurface(
            stream, scale * canvas.width, scale * canvas.height)
    else:
        surface = cairo.PSSurface(
            fobj, scale * canvas.width, scale * canvas.height)
    surface.set_eps(True)
    context = cairo.Context(surface)
    context.scale(scale, scale)
    toyplot.cairo.render(svg, context)
    surface.flush()
    surface.finish()
    if fobj is None:
        return stream.getvalue()
