from behave import *
import nose.tools

import json
import numpy
import os
import subprocess
import sys
import tempfile
import toyplot

try:
    import toyplot.mp4
except:
    pass

try:
    import toyplot.webm
except:
    pass


@given(u'an animated canvas')
def step_impl(context):
    context.canvas = toyplot.Canvas(
        style={"background-color": "white"}, width=600, height=600)
    axes = context.canvas.axes()
    scatterplot = axes.scatterplot(numpy.arange(10))

    def callback(frame):
        if frame.index() == 0:
            for i in numpy.arange(10):
                frame.set_datum_style(scatterplot, 0, i, {"opacity": 0})
        else:
            frame.set_datum_style(
                scatterplot, 0, frame.index() - 1, {"opacity": 1})
    context.canvas.animate(11, callback)


@when(u'rendering a {type} video')
def step_impl(context, type):
    nose.tools.assert_in(type, ["mp4", "webm"])

    # Return quietly if the video backend isn't available
    if not hasattr(toyplot, type):
        return

    backend = getattr(toyplot, type)

    def progress(frame):
        pass
    context.path = os.path.join(tempfile.mkdtemp(), "test.%s" % type)
    backend.render(context.canvas, context.path, progress=progress)
    sys.stderr.write("**** %s ****\n" % context.path)
    sys.stderr.flush()


@then(u'the backend should return a {type} video')
def step_impl(context, type):
    nose.tools.assert_in(type, ["mp4", "webm"])

    # Return quietly if the video backend isn't available
    if not hasattr(toyplot, type):
        return

    command = ["ffprobe", "-print_format", "json", "-show_format",
               "-show_streams", "-count_frames", context.path]
    ffprobe = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = ffprobe.communicate()
    video_metadata = json.loads(stdout)
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
