# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generate PNG images using Cairo.
"""

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
    """Render the PNG bitmap representation of a canvas using Cairo.

    By default, canvas dimensions in CSS pixels are mapped directly to pixels in
    the output PNG image.  Use one of `width`, `height`, or `scale` to override
    this behavior.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      Canvas to be rendered.
    fobj: file-like object or string, optional
      The file to write.  Use a string filepath to write data directly to disk.
      If `None` (the default), the PNG data will be returned to the caller
      instead.
    width: number, optional
      Specify the width of the output image in pixels.
    height: number, optional
      Specify the height of the output image in pixels.
    scale: number, optional
      Ratio of output image pixels to `canvas` pixels.

    Returns
    -------
    png: PNG image data, or `None`
      PNG representation of `canvas`, or `None` if the caller specifies the
      `fobj` parameter.
    """
    svg = toyplot.svg.render(canvas)
    scale = canvas.pixel_scale(width=width, height=height, scale=scale)
    surface = cairo.ImageSurface(
        cairo.FORMAT_ARGB32, int(scale * canvas.width), int(scale * canvas.height))
    context = cairo.Context(surface)
    context.scale(scale, scale)
    toyplot.cairo.render(svg, context)
    if fobj is None:
        stream = StringIO.StringIO()
        surface.write_to_png(stream)
        return stream.getvalue()
    else:
        surface.write_to_png(fobj)


def render_frames(canvas, width=None, height=None, scale=None):
    """Render a canvas as a sequence of PNG images using Cairo.

    By default, canvas dimensions in CSS pixels are mapped directly to pixels in
    the output PNG images.  Use one of `width`, `height`, or `scale` to override
    this behavior.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      Canvas to be rendered.
    width: number, optional
      Specify the width of the output image in pixels.
    height: number, optional
      Specify the height of the output image in pixels.
    scale: number, optional
      Ratio of output image pixels to `canvas` pixels.

    Returns
    -------
    frames: Python generator expression that returns each PNG image in the sequence.
      The caller must iterate over the returned frames and is responsible for all
      subsequent processing, including disk I/O, video compression, etc.

    Examples
    --------
    >>> for frame, png in enumerate(toyplot.cairo.render_png_frames(canvas)):
    ...   open("frame-%s.png" % frame, "wb").write(png)
    """
    svg, svg_animation = toyplot.svg.render(canvas, animation=True)
    scale = canvas.pixel_scale(width=width, height=height, scale=scale)
    for time, changes in sorted(svg_animation.items()):
        toyplot.svg.apply_changes(svg, changes)
        surface = cairo.ImageSurface(
            cairo.FORMAT_ARGB32, int(scale * canvas.width), int(scale * canvas.height))
        context = cairo.Context(surface)
        context.scale(scale, scale)
        toyplot.cairo.render(svg, context)
        fobj = StringIO.StringIO()
        surface.write_to_png(fobj)
        yield fobj.getvalue()
