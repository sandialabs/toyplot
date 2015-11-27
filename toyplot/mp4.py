# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generate MPEG-4 videos."""

from __future__ import absolute_import
from __future__ import division


import os
import subprocess
import toyplot.png


for path in os.environ["PATH"].split(os.pathsep):
    if os.path.exists(os.path.join(path, "ffmpeg")):
        break
else:
    raise Exception("An ffmpeg executable is required.")  # pragma: no cover


def render(
        canvas,
        filename,
        width=None,
        height=None,
        scale=None,
        progress=None):
    """Render a canvas as an MPEG-4 video.

    By default, the canvas dimensions in CSS pixels are mapped directly to
    pixels in the output MPEG-4 video.  Use one of `width`, `height`, or
    `scale` to override this behavior.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      Canvas to be rendered.
    filename: string
      Output video filename.
    width: number, optional
      Specify the width of the output video in pixels.
    height: number, optional
      Specify the height of the output video in pixels.
    scale: number, optional
      Ratio of output video pixels to `canvas` drawing units.
    progress: callback function taking a single `frame` argument, optional
      Callback function that will receive the number of each frame as it's
      written; useful to provide an indication of progress to end-users.

    Notes
    -----
    The individual video frames are rendered using PNG representations
    of the canvas generated with :func:`toyplot.png.render_frames()`.

    Examples
    --------
    >>> def callback(frame):
    ...   print "Writing frame %s" % frame
    ... toyplot.mp4.render(canvas, "test.mp4", progress=callback)
    """

    command = [
        "ffmpeg",
        "-f", "image2pipe",
        "-c", "png",
        "-i", "-",
        "-pix_fmt", "yuv420p",
        "-y",
        filename,
    ]
    ffmpeg = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    for frame, png in enumerate(
            toyplot.png.render_frames(
                canvas=canvas, width=width, height=height, scale=scale)):
        if progress is not None:
            progress(frame)
        ffmpeg.stdin.write(png)
    ffmpeg.stdin.close()
    ffmpeg.wait()
