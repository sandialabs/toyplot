# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functions to render PNG images."""



import toyplot.require
import toyplot.reportlab.png as implementation


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
    png: :class:`bytes` containing PNG image data, or `None`
      Returns `None` if the caller specifies the `fobj` parameter, returns the PNG image data otherwise.

    Notes
    -----
    The output PNG is rendered using :func:`toyplot.reportlab.png.render()`.
    This is subject to change.
    """
    canvas = toyplot.require.instance(canvas, toyplot.canvas.Canvas)
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
    frames: Sequence of :class:`bytes` objects containing PNG image data.
      The caller must iterate over the returned frames and is responsible for all
      subsequent processing, including disk I/O, video compression, etc.

    Notes
    -----
    The output PNG images are rendered using
    :func:`toyplot.reportlab.png.render_frames()`.  This is subject to change.

    Examples
    --------
    >>> for frame, png in enumerate(toyplot.png.render_frames(canvas)):
    ...   open("frame-%s.png" % frame, "wb").write(png)
    """
    canvas = toyplot.require.instance(canvas, toyplot.canvas.Canvas)
    return implementation.render_frames(canvas, width, height, scale)
