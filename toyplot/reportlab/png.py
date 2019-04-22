# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functions to render PNG images using Ghostscript.
"""


import distutils.version
import io
import subprocess

import reportlab.pdfgen.canvas

import toyplot.reportlab
import toyplot.require
import toyplot.svg

# Verify that ghostscript is installed, and check the version
_gs_command = None
_gs_version = None
for command in ["gs", "gswin64c", "gswin32c"]:
    try:
        _gs_version = subprocess.check_output([command, "--version"]).decode(encoding="utf-8").strip()
        _gs_command = command
    except:
        pass

if _gs_command is None:
    raise Exception("A ghostscript executable is required.")  # pragma: no cover

if distutils.version.StrictVersion(_gs_version) >= "9.14":
    _gs_resolution = ["-r%s" % (96 * 4), "-dDownScaleFactor=4"]
else: # pragma: no cover
    _gs_resolution = ["-r%s" % (96)]
    toyplot.log.warning("For better output PNG quality, install ghostscript >= 9.14.")


def render(canvas, fobj=None, width=None, height=None, scale=None):
    """Render the PNG bitmap representation of a canvas using ReportLab and Ghostscript.

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
    """
    canvas = toyplot.require.instance(canvas, toyplot.canvas.Canvas)
    svg = toyplot.svg.render(canvas)
    scale = canvas._point_scale(width=width, height=height, scale=scale)
    pdf = io.BytesIO()
    surface = reportlab.pdfgen.canvas.Canvas(pdf, pagesize=(scale * canvas.width, scale * canvas.height))
    surface.translate(0, scale * canvas.height)
    surface.scale(1, -1)
    surface.scale(scale, scale)
    toyplot.reportlab.render(svg, surface)
    surface.showPage()
    surface.save()

    command = [
        _gs_command,
        "-dSAFER",
        "-dBATCH",
        "-dNOPAUSE",
        "-dQUIET",
        "-sOutputFile=-",
        "-dMaxBitmap=2147483647",
        "-dTextAlphaBits=4",
        "-dGraphicsAlphaBits=4",
        "-sDEVICE=pngalpha",
        ] + _gs_resolution + ["-"]

    gs = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = gs.communicate(pdf.getvalue())

    if fobj is None:
        return stdout
    elif isinstance(fobj, str):
        with open(fobj, "wb") as stream:
            stream.write(stdout)
    else:
        fobj.write(stdout)


def render_frames(canvas, width=None, height=None, scale=None):
    """Render a canvas as a sequence of PNG images using ReportLab and Ghostscript.

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

    Examples
    --------
    >>> for frame, png in enumerate(toyplot.reportlab.png.render_frames(canvas)):
    ...   open("frame-%s.png" % frame, "wb").write(png)
    """
    canvas = toyplot.require.instance(canvas, toyplot.canvas.Canvas)
    svg, svg_animation = toyplot.svg.render(canvas, animation=True)
    scale = canvas._point_scale(width=width, height=height, scale=scale)

    for time in sorted(svg_animation.keys()):
        toyplot.svg.apply_changes(svg, svg_animation[time])

        pdf = io.BytesIO()
        surface = reportlab.pdfgen.canvas.Canvas(pdf, pagesize=(scale * canvas.width, scale * canvas.height))
        surface.translate(0, scale * canvas.height)
        surface.scale(1, -1)
        surface.scale(scale, scale)
        toyplot.reportlab.render(svg, surface)
        surface.showPage()
        surface.save()

        command = [
            "gs",
            "-dNOPAUSE",
            "-dBATCH",
            "-dQUIET",
            "-dMaxBitmap=2147483647",
            "-sDEVICE=pngalpha",
            "-r%s" % 96,
            "-sOutputFile=-",
            "-",
            ]

        gs = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = gs.communicate(pdf.getvalue())
        yield stdout
