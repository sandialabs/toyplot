# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generate PNG images using Ghostscript.
"""

from __future__ import absolute_import
from __future__ import division

import distutils.version
import io
import os.path
import subprocess

import reportlab.pdfgen.canvas

import toyplot.reportlab
import toyplot.require
import toyplot.svg

for path in os.environ["PATH"].split(os.pathsep):
    if os.path.exists(os.path.join(path, "gs")):
        gs_version = subprocess.check_output(["gs", "--version"])
        _downscale = distutils.version.StrictVersion(gs_version) >= "9.10"
        if not _downscale:
            toyplot.log.warning("For better output PNG quality, install ghostscript >= 9.10.")
        break
else:
    raise Exception("The gs executable is required.")  # pragma: no cover


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
        "gs",
        "-dSAFER",
        "-dBATCH",
        "-dNOPAUSE",
        "-dQUIET",
        "-sOutputFile=-",
        "-dMaxBitmap=2147483647",
        "-dTextAlphaBits=4",
        "-dGraphicsAlphaBits=4",
        "-sDEVICE=pngalpha",
        ]
    if _downscale:
        command += [
            "-r%s" % (96 * 4),
            "-dDownScaleFactor=4",
            ]
    else:
        command += [
            "-r%s" % (96),
            ]
    command += [
        "-",
        ]

    gs = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = gs.communicate(pdf.getvalue()) # pylint: disable=unused-variable

    if fobj is None:
        return stdout
    elif isinstance(fobj, toyplot.compatibility.string_type):
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

    for time, changes in sorted(svg_animation.items()): # pylint: disable=unused-variable
        toyplot.svg.apply_changes(svg, changes)

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
        stdout, stderr = gs.communicate(pdf.getvalue()) # pylint: disable=unused-variable
        yield stdout
