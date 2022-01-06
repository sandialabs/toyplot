# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generate MPEG-4 videos."""


import logging
import os
import subprocess

import toyplot.png

log = logging.getLogger(__name__)

# Verify that ffmpeg is installed, and check the version
_ffmpeg_command = None
_ffmpeg_version = None
for command in ["ffmpeg"]:
    try:
        _ffmpeg_version = subprocess.check_output([command, "-version"]).decode(encoding="utf-8").strip()
        _ffmpeg_command = command
        log.info("Using %s.", _ffmpeg_version)
    except: # pragma: no cover
        pass

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

    if _ffmpeg_command is None:
        raise RuntimeError("An ffmpeg executable is required.")  # pragma: no cover


    command = [
        _ffmpeg_command,
        "-f", "image2pipe",
        "-c", "png",
        "-i", "-",
        "-pix_fmt", "yuv420p",
        "-vcodec", "h264",
        "-preset", "slow",
        "-tune", "animation",
        "-crf", "17",
        "-y",
        filename,
    ]

    try:
        log.info("Running command: %s", " ".join(command))
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
    except Exception as e: # pragma: no cover
        log.error(ffmpeg.stdout.read())
        log.error(ffmpeg.stderr.read())
        raise e
