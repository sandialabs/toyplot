# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functions to render PDF documents using ReportLab."""



import io
import reportlab.pdfgen.canvas
import toyplot.reportlab
import toyplot.require
import toyplot.svg


def render(canvas, fobj=None, width=None, height=None, scale=None):
    """Render the PDF representation of a canvas using ReportLab.

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

    >>> toyplot.reportlab.pdf.render(canvas, "figure-1.pdf", width=(4, "inches"))
    """
    canvas = toyplot.require.instance(canvas, toyplot.canvas.Canvas)
    svg = toyplot.svg.render(canvas)
    scale = canvas._point_scale(width=width, height=height, scale=scale)
    if fobj is None:
        stream = io.BytesIO()
        surface = reportlab.pdfgen.canvas.Canvas(
            stream, pagesize=(scale * canvas.width, scale * canvas.height))
    else:
        surface = reportlab.pdfgen.canvas.Canvas(
            fobj, pagesize=(scale * canvas.width, scale * canvas.height))
    surface.translate(0, scale * canvas.height)
    surface.scale(1, -1)
    surface.scale(scale, scale)
    toyplot.reportlab.render(svg, surface)
    surface.showPage()
    surface.save()
    if fobj is None:
        return stream.getvalue()
