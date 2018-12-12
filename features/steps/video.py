# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import nose.tools

import collections
import io
import json
import logging
import numpy.testing
import os
import subprocess
import sys
import tempfile

import testing

try:
    import toyplot.mp4
except:
    pass

try:
    import toyplot.png
except:
    pass


@given(u'an animated canvas')
def step_impl(context):
    context.canvas = toyplot.Canvas(
        style={"background-color": "white"}, width=600, height=600)
    axes = context.canvas.cartesian()
    scatterplot = axes.scatterplot(numpy.arange(10))

    for frame in context.canvas.frames(11):
        if frame.number == 0:
            for i in numpy.arange(10):
                frame.set_datum_style(scatterplot, 0, i, {"opacity": 0})
        else:
            frame.set_datum_style(
                scatterplot, 0, frame.number - 1, {"opacity": 1})


@then(u'the canvas can be rendered as {type} video')
def step_impl(context, type):
    nose.tools.assert_in(type, ["mp4"])

    def progress(frame):
        pass
    context.path = os.path.join(tempfile.mkdtemp(), "test.%s" % type)
    context.backend.render(context.canvas, context.path, progress=progress)
    sys.stderr.write("**** %s ****\n" % context.path)
    sys.stderr.flush()

    command = ["ffprobe", "-print_format", "json", "-show_format",
               "-show_streams", "-count_frames", context.path]
    ffprobe = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = ffprobe.communicate()
    video_metadata = json.loads(stdout.decode())
    logging.info("video metadata: %s", video_metadata)
    video_format = video_metadata["format"]
    nose.tools.assert_equal(video_format["nb_streams"], 1)
    nose.tools.assert_in(type, video_format["format_name"])
    video_stream = video_metadata["streams"][0]
    nose.tools.assert_equal(
        video_stream["codec_name"], "h264" if type == "mp4" else "vp8")
    nose.tools.assert_equal(video_stream["codec_type"], "video")
    nose.tools.assert_equal(video_stream["width"], 600)
    nose.tools.assert_equal(video_stream["height"], 600)
    nose.tools.assert_equal(video_stream["nb_read_frames"], "11")


@then(u'the canvas can be rendered as png frames')
def step_impl(context):
    for frame in toyplot.png.render_frames(context.canvas):
        image = testing.read_png(io.BytesIO(frame))
        nose.tools.assert_equal(image.shape, (600, 600, 4))
        nose.tools.assert_equal(image.dtype, "uint8")


@when(u'an animation frame is created, its fields are populated correctly.')
def step_impl(context):
    frame = toyplot.canvas.AnimationFrame(number=1, begin=2.3, end=2.4, count=1, changes=collections.defaultdict(lambda: collections.defaultdict(list)))
    nose.tools.assert_equal(frame.number, 1)
    nose.tools.assert_equal(frame.begin, 2.3)
    numpy.testing.assert_almost_equal(frame.length, 0.1)
    with nose.tools.assert_raises(ValueError):
        frame.set_mark_style(None, {})
    with nose.tools.assert_raises(ValueError):
        frame.set_datum_style(None, 0, 0, {})


@when(u'a canvas is used to create an animation frame, its fields are populated correctly.')
def step_impl(context):
    canvas = toyplot.Canvas()
    frame = canvas.frame(0.3, 0.4)
    nose.tools.assert_equal(frame.begin, 0.3)
    numpy.testing.assert_almost_equal(frame.length, 0.1)
    nose.tools.assert_equal(frame.number, 0)

    frame = canvas.frame(0.3, 0.4, 5)
    nose.tools.assert_equal(frame.begin, 0.3)
    numpy.testing.assert_almost_equal(frame.length, 0.1)
    nose.tools.assert_equal(frame.number, 5)



