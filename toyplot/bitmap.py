# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Bitmap management and manipulation.
"""

from __future__ import absolute_import

import base64
import io
import logging

import numpy
import png

import toyplot.color


log = logging.getLogger(__name__)


def to_png(data, stream):
    """Convert an in-memory bitmap to PNG format.

    Parameters
    ----------
    data: :class:`numpy.ndarray`, required
        Source array containing bitmap data to be converted.  Valid array shapes
        are :math:`M \times N \times 1` (greyscale data), :math:`M \times N \times 2`
        (greyscale plus alpha channel), :math:`M \times N \times 3`
        (RGB data), or :math:`M \times N \times 4` (RGB + alpha).  Floating
        point values are scaled and converted to unsigned 8 bit integers.
    stream: file-like object, required
        Target file to receive PNG data.
    """
    log.debug("Image data: %s %s", data.shape, data.dtype)

    if data.dtype == toyplot.color.dtype:
        data = numpy.dstack((data["r"], data["g"], data["b"], data["a"]))
    if issubclass(data.dtype.type, numpy.bool_):
        bitdepth = 1
    elif issubclass(data.dtype.type, numpy.floating):
        data = (data * 255.0).astype("uint8")
        bitdepth = 8
    else:
        bitdepth = 8

    width = data.shape[1]
    height = data.shape[0]
    greyscale = data.shape[2] < 3
    alpha = data.shape[2] == 2 or data.shape[2] == 4

    writer = png.Writer(width=width, height=height, greyscale=greyscale, alpha=alpha, bitdepth=bitdepth)
    writer.write(stream, numpy.reshape(data, (-1, data.shape[1] * data.shape[2])))


def to_png_data_uri(data):
    """Convert an in-memory bitmap to PNG format, encoded as a data: URI.

    Parameters
    ----------
    data: :class:`numpy.ndarray`, required
        Source array containing bitmap data to be converted.  Valid array shapes
        are :math:`M \times N \times 1` (greyscale data), :math:`M \times N \times 2`
        (greyscale plus alpha channel), :math:`M \times N \times 3`
        (RGB data), or :math:`M \times N \times 4` (RGB + alpha).  Floating
        point values are scaled and converted to unsigned 8 bit integers.

    Returns
    -------
    uri: str
        A data: URI containing the base64 encoded bitmap.
    """
    stream = io.BytesIO()
    to_png(data, stream)
    return "data:image/png;base64," + base64.standard_b64encode(stream.getvalue()).decode("ascii")


