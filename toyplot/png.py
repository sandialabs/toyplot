# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generate PNG images."""

from __future__ import absolute_import
from __future__ import division

import toyplot

try:
    import toyplot.qt.png as implementation
except:
    try:
        import toyplot.cairo.png as implementation
        toyplot.log.warning("Couldn't load toyplot.qt.png (preferred), using toyplot.cairo.png (deprecated).")
    except:
        toyplot.log.error("Couldn't load a PNG backend.  Try installing PyQt 5 (preferred), or pango / cairo.")
        raise


def render(canvas, fobj=None, width=None, height=None, scale=None):
    """Render the PNG bitmap representation of a canvas.

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

    Notes
    -----
    The output PNG is currently rendered using
    :func:`toyplot.cairo.png.render()`.  This may change in the future.
    """
    return implementation.render(canvas, fobj, width, height, scale)


def render_frames(canvas, width=None, height=None, scale=None):
    """Render a canvas as a sequence of PNG images.

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

    Notes
    -----
    The output PNG images are currently rendered using
    :func:`toyplot.cairo.png.render_frames()`.  This may change in the future.

    Examples
    --------
    >>> for frame, png in enumerate(toyplot.cairo.render_png_frames(canvas)):
    ...   open("frame-%s.png" % frame, "wb").write(png)
    """
    return implementation.render_frames(canvas, width, height, scale)

