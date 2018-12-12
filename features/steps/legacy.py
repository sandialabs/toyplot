# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import collections

import nose.tools
import numpy.testing
import toyplot


@given(u'axes-bars-boundaries-masked-nan')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(size=(50, 50))
    b = numpy.ma.column_stack((numpy.min(observations, axis=1), numpy.median(
        observations, axis=1), numpy.max(observations, axis=1)))
    b[10:20, 0] = numpy.nan
    b[30:40, 1] = numpy.ma.masked
    b[20:30, 2] = numpy.nan

    context.canvas, axes, mark = toyplot.bars(b, baseline=None)


@given(u'axes-bars-histogram')
def step_impl(context):
    numpy.random.seed(1234)
    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(numpy.histogram(numpy.random.normal(size=10000), 100))


@given(u'axes-bars-magnitudes-masked-nan')
def step_impl(context):
    x = numpy.linspace(0, 2 * numpy.pi, 51)
    y = numpy.ma.column_stack((
        1 + 0.5 * numpy.sin(x),
        1 + 0.5 * numpy.cos(x),
        1 + 0.2 * numpy.sin(2 * x),
    ))
    y[8:18, 0] = numpy.nan
    y[33:43, 1] = numpy.ma.masked

    context.canvas, axes, mark = toyplot.bars(x, y)


@given(u'axes-bars-n-boundaries-along-y')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(series, along="y", baseline=None)


@given(u'axes-bars-n-boundaries-centers')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(x, series, baseline=None)


@given(u'axes-bars-n-boundaries-edges')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(x1, x2, series, baseline=None)


@given(u'axes-bars-n-boundaries-titles')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.min(
            observations, axis=1), numpy.percentile(
            observations, 25, axis=1), numpy.percentile(
                observations, 50, axis=1), numpy.percentile(
                    observations, 75, axis=1), numpy.max(
                        observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(
        series,
        title=[
            "1st quartile",
            "2nd quartile",
            "3rd quartile",
            "4th quartile"],
        baseline=None)


@given(u'axes-bars-n-boundaries')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(series, baseline=None)


@given(u'axes-bars-n-magnitudes-along-y')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(series, along="y")


@given(u'axes-bars-n-magnitudes-centers')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(x, series)


@given(u'axes-bars-n-magnitudes-edges')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(x1, x2, series)


@given(u'axes-bars-n-magnitudes-symmetric')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(series, baseline="symmetric")


@given(u'axes-bars-n-magnitudes-titles')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(series, baseline="stacked", title=["mean", "standard deviation"])


@given(u'axes-bars-n-magnitudes-wiggle')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(series, baseline="wiggle")


@given(u'axes-bars-n-magnitudes')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(series)


@given(u'axes-bars-one-boundary-centers')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y1 = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(x, y1, baseline=None)


@given(u'axes-bars-one-boundary-edges')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    y1 = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(x1, x2, y1, baseline=None)


@given(u'axes-bars-one-boundary')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y1 = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(y1, baseline=None)


@given(u'axes-bars-one-magnitude-centers')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(x, y)


@given(u'axes-bars-one-magnitude-edges')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    y = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(x1, x2, y)


@given(u'axes-bars-one-magnitude')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.bars(y)


@given(u'axes-fill-boundaries-masked-nan')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(size=(50, 50))
    b = numpy.ma.column_stack((numpy.min(observations, axis=1), numpy.median(
        observations, axis=1), numpy.max(observations, axis=1)))
    b[10:20, 0] = numpy.nan
    b[30:40, 1] = numpy.ma.masked
    b[20:30, 2] = numpy.nan

    context.canvas, axes, mark = toyplot.fill(b)


@given(u'axes-fill-magnitudes-masked-nan')
def step_impl(context):
    x = numpy.linspace(0, 2 * numpy.pi, 51)
    y = numpy.ma.column_stack((
        1 + 0.5 * numpy.sin(x),
        1 + 0.5 * numpy.cos(x),
        1 + 0.2 * numpy.sin(2 * x),
    ))
    y[8:18, 0] = numpy.nan
    y[33:43, 1] = numpy.ma.masked

    context.canvas, axes, mark = toyplot.fill(x, y, baseline="stacked")


@given(u'axes-palette')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    for i in range(10):
        axes.plot(numpy.arange(2), numpy.repeat(i, 2))


@given(u'axes-palettes')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.fill(numpy.sin(numpy.linspace(0, 2 * numpy.pi, 100)),
              style={"fill-opacity": 0.5})
    axes.plot(numpy.sin(numpy.linspace(0, 2 * numpy.pi, 100)), marker="o")
    axes.fill(numpy.cos(numpy.linspace(0, 2 * numpy.pi, 100)),
              style={"fill-opacity": 0.5})
    axes.plot(numpy.cos(numpy.linspace(0, 2 * numpy.pi, 100)), marker="o")
    axes.fill((numpy.linspace(0, 1, 100)), style={"fill-opacity": 0.5})
    axes.plot((numpy.linspace(0, 1, 100)), marker="o")


@given(u'axes-plot-masked-nan')
def step_impl(context):
    x = numpy.linspace(0, 2 * numpy.pi, 51)
    y = numpy.ma.column_stack((
        1 + 0.5 * numpy.sin(x),
        1 + 0.5 * numpy.cos(x),
        1 + 0.2 * numpy.sin(2 * x),
    ))
    y[8:18, 0] = numpy.nan
    y[33:43, 1] = numpy.ma.masked

    context.canvas, axes, mark = toyplot.plot(x, y, marker="o")


@given(u'axes-plot-n-variables-along-y')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.plot(series, along="y")


@given(u'axes-plot-n-variables-x')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.plot(x, series)


@given(u'axes-plot-n-variables')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.plot(series)


@given(u'axes-plot-one-variable-x')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.plot(x, y)


@given(u'axes-plot-one-variable')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.plot(y)


@given(u'axes-rect-singular-along-y')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian(xmin=0, xmax=1, ymin=0, ymax=1)
    axes.rects(0.1, 0.2, 0.3, 0.6, along="y")


@given(u'axes-rect-singular')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian(xmin=0, xmax=1, ymin=0, ymax=1)
    axes.rects(0.1, 0.2, 0.3, 0.6)


@given(u'axes-rect')
def step_impl(context):
    x1 = numpy.arange(1, 10)
    x2 = x1 + 0.5
    y1 = x1 - 0.5
    y2 = x1 ** 1.5
    color = x1
    title = x1
    colormap = toyplot.color.CategoricalMap(toyplot.color.brewer.palette("BlueRed"))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.rects(x1, x2, y1, y2, color=(color, colormap), title=title)


@given(u'axes-scatterplot-markers')
def step_impl(context):
    marker_style = {"stroke": toyplot.color.black, "fill": "cornsilk"}
    label_style = {"stroke": "none", "fill": toyplot.color.black}
    markers = [
        None,
        "",
        "|",
        "-",
        "/",
        "\\",
        "+",
        "x",
        toyplot.marker.create(shape="x", angle=-22.5),
        "*",
        "^",
        toyplot.marker.create(shape=">", mstyle={"stroke": "red"}),
        toyplot.marker.create(shape="v", mstyle={"stroke": "red", "fill": "yellow"}),
        "<",
        "s",
        "d",
        "o",
        "oo",
        "o|",
        "o-",
        "o+",
        "ox",
        "o*",
        toyplot.marker.create(shape="", label="A"),
        toyplot.marker.create(shape="o", label="1"),
        toyplot.marker.create(shape="s", mstyle={"stroke": "blue", "fill": "white"}, label="B", lstyle={"fill": "blue"}),
        toyplot.marker.create(shape="d", label="2", lstyle={"fill": "green"}),
    ]

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.scatterplot(
        numpy.arange(
            len(markers)),
        color="steelblue",
        marker=markers,
        size=10,
        mstyle=marker_style,
        mlstyle=label_style)


@given(u'axes-scatterplot-n-variables-along-y')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.scatterplot(series, along="y")


@given(u'axes-scatterplot-n-variables-x')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.scatterplot(x, series)


@given(u'axes-scatterplot-n-variables')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.scatterplot(series)


@given(u'axes-scatterplot-one-variable-fill')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)
    color = numpy.arange(len(observations))

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.scatterplot(y, color=color)


@given(u'axes-scatterplot-one-variable-x')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.scatterplot(x, y)


@given(u'axes-scatterplot-one-variable')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.scatterplot(y)


@given(u'axes-scatterplot-singular')
def step_impl(context):
    x = numpy.linspace(0, 2 * numpy.pi)
    y = numpy.sin(x)

    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.plot(x, y)
    axes.scatterplot(x[0], y[0], color="red")


@given(u'axes-tick-titles')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.x.ticks.locator = toyplot.locator.Explicit(
        locations=[-0.5, 0, 0.5], titles=["Foo", "Bar", "Baz"])
    axes.y.ticks.locator = toyplot.locator.Explicit(
        locations=[-0.5, 0, 0.5], titles=["Red", "Green", "Blue"])


@given(u'bars-one-magnitude')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    context.canvas, axes, mark = toyplot.bars(y)


@given(u'scatterplot-one-variable')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    context.canvas, axes, mark = toyplot.scatterplot(y)

@when(u'an animation frame is created, its fields are populated.')
def step_impl(context):
    frame = toyplot.canvas.AnimationFrame(number=1, begin=2.3, end=2.4, count=1, changes=collections.defaultdict(lambda: collections.defaultdict(list)))
    nose.tools.assert_equal(frame.number, 1)
    nose.tools.assert_equal(frame.begin, 2.3)
    numpy.testing.assert_almost_equal(frame.length, 0.1)
    with nose.tools.assert_raises(ValueError):
        frame.set_mark_style(None, {})
    with nose.tools.assert_raises(ValueError):
        frame.set_datum_style(None, 0, 0, {})


@when(u'a canvas is used to create an animation frame, its fields are populated.')
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


