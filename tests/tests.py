# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import io
import collections
import difflib
import json
import nose.tools
import numbers
import numpy
import os
import re
import sys
import tempfile
import xml.etree.ElementTree as xml

import six
import toyplot
import toyplot.color
import toyplot.html
import toyplot.locator
import toyplot.svg

try:
    import toyplot.pdf
except:
    pass

try:
    import toyplot.png
except:
    pass

try:
    import toyplot.reportlab.pdf
except:
    pass

try:
    import toyplot.reportlab.png
except:
    pass


##########################################################################
# Test fixtures.

def json_comparison_string(o):
    """Convert a Python object to a JSON string representation that can be used for comparison.

    Limits the precision of floating-point numbers.
    """
    if o is None:
        return "null"
    if isinstance(o, six.string_types):
        return "\"" + o + "\""
    if isinstance(o, numbers.Integral):
        return str(o)
    if isinstance(o, numbers.Real):
        return "%.9g" % o
    if isinstance(o, collections.Sequence):
        return "[" + ",".join([json_comparison_string(i) for i in o]) + "]"
    if isinstance(o, collections.Mapping):
        return "{" + ",".join(["\"" + key + "\":" + json_comparison_string(value)
                               for key, value in o.items()]) + "}"
    raise Exception("Unexpected value: %s" % o)


def xml_comparison_string(element):
    """Convert an XML element to a pretty string representation that can be used for comparison.

    Filters-out elements and attributes (like id) that shouldn't be compared,
    and limits the precision of floating-point numbers.
    """
    def format_value(value):
        try:
            return "%.9g" % float(value)
        except:
            return value

    def write_element(element, buffer, indent):
        buffer.write(u"%s<%s" % (indent, element.tag))
        for key, value in element.items():
            if key in ["id", "clip-path"]:
                continue
            if key == "d" and element.tag == "{http://www.w3.org/2000/svg}path":
                buffer.write(
                    u" %s='%s'" % (key, " ".join([format_value(d) for d in value.split(" ")])))
            elif key == "transform":
                buffer.write(u" %s='%s'" % (
                    key, "".join([format_value(d) for d in re.split("(,|\(|\))", value)])))
            elif key == "points" and element.tag == "{http://www.w3.org/2000/svg}polygon":
                buffer.write(u" %s='%s'" % (key, " ".join(
                    [",".join([format_value(i) for i in p.split(",")]) for p in value.split(" ")])))
            else:
                buffer.write(u" %s='%s'" % (key, format_value(value)))

        text = element.text if element.text is not None else ""
        if element.tag in [
                "{http://www.sandia.gov/toyplot}data-table",
                "{http://www.sandia.gov/toyplot}coordinates"]:
            text = str(json_comparison_string(json.loads(element.text)))
        buffer.write(u">%s\n" % text)
        for child in list(element):
            write_element(child, buffer, indent + "  ")
        buffer.write(u"%s</%s>\n" % (indent, element.tag))

    buffer = io.StringIO()
    write_element(element, buffer, indent="")
    return buffer.getvalue()


def assert_canvas_matches(canvas, name):
    # Render every representation of the canvas for coverage ...
    html = io.BytesIO()
    toyplot.html.render(canvas, html)

    svg = io.BytesIO()
    toyplot.svg.render(canvas, svg)

    for module in ["toyplot.pdf", "toyplot.png", "toyplot.reportlab.pdf", "toyplot.reportlab.png"]:
        if module in sys.modules:
            buffer = io.BytesIO()
            sys.modules[module].render(canvas, buffer)

    # Get rid of any past failures ...
    if os.path.exists("tests/diffs/%s.svg" % name):
        os.remove("tests/diffs/%s.svg" % name)
    if os.path.exists("tests/diffs/%s.reference.svg" % name):
        os.remove("tests/diffs/%s.reference.svg" % name)
    if os.path.exists("tests/failed/%s.svg" % name):
        os.remove("tests/failed/%s.svg" % name)

    # If there's no stored SVG reference for this canvas, create one ...
    if not os.path.exists("tests/reference/%s.svg" % name):
        with open("tests/reference/%s.svg" % name, "wb") as file:
            file.write(svg.getvalue())
        raise AssertionError(
            "Created new reference file tests/reference/%s.svg ... you should verify its contents before re-running the test." %
            name)

    # Compare the SVG representation of the canvas to the SVG reference ...
    svg_dom = xml.fromstring(svg.getvalue())
    reference_dom = xml.parse("tests/reference/%s.svg" % name).getroot()

    svg_string = xml_comparison_string(svg_dom)
    reference_string = xml_comparison_string(reference_dom)

    try:
        if svg_string != reference_string:
            raise Exception(
                "\n".join(
                    list(
                        difflib.context_diff(
                            svg_string.split("\n"),
                            reference_string.split("\n"),
                            lineterm="",
                            fromfile="test svg",
                            tofile="reference svg"))))
    except Exception as e:
        if not os.path.exists("tests/diffs"):
            os.mkdir("tests/diffs")
        with open("tests/diffs/%s.svg" % name, "wb") as file:
            file.write(svg_string.encode("utf-8"))
        with open("tests/diffs/%s.reference.svg" % name, "wb") as file:
            file.write(reference_string.encode("utf-8"))
        if not os.path.exists("tests/failed"):
            os.mkdir("tests/failed")
        with open("tests/failed/%s.svg" % name, "wb") as file:
            file.write(svg.getvalue())
        raise AssertionError(
            "Test output tests/failed/%s.svg doesn't match tests/reference/%s.svg:\n%s" %
            (name, name, e))

##########################################################################
# toyplot


def test_axes_tick_titles():
    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.x.ticks.locator = toyplot.locator.Explicit(
        locations=[-0.5, 0, 0.5], titles=["Foo", "Bar", "Baz"])
    axes.y.ticks.locator = toyplot.locator.Explicit(
        locations=[-0.5, 0, 0.5], titles=["Red", "Green", "Blue"])
    assert_canvas_matches(canvas, "axes-tick-titles")


def test_axes_palette():
    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    for i in range(10):
        axes.plot(numpy.arange(2), numpy.repeat(i, 2))
    assert_canvas_matches(canvas, "axes-palette")


def test_axes_palettes():
    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.fill(numpy.sin(numpy.linspace(0, 2 * numpy.pi, 100)),
              style={"fill-opacity": 0.5})
    axes.plot(numpy.sin(numpy.linspace(0, 2 * numpy.pi, 100)), marker="o")
    axes.fill(numpy.cos(numpy.linspace(0, 2 * numpy.pi, 100)),
              style={"fill-opacity": 0.5})
    axes.plot(numpy.cos(numpy.linspace(0, 2 * numpy.pi, 100)), marker="o")
    axes.fill((numpy.linspace(0, 1, 100)), style={"fill-opacity": 0.5})
    axes.plot((numpy.linspace(0, 1, 100)), marker="o")
    assert_canvas_matches(canvas, "axes-palettes")


def test_bars_one_magnitude():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    canvas, axes, mark = toyplot.bars(y)
    assert_canvas_matches(canvas, "bars-one-magnitude")


def test_axes_bars_one_magnitude():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(y)
    assert_canvas_matches(canvas, "axes-bars-one-magnitude")


def test_axes_bars_one_magnitude_centers():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(x, y)
    assert_canvas_matches(canvas, "axes-bars-one-magnitude-centers")


def test_axes_bars_one_magnitude_edges():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(x1, x2, y)
    assert_canvas_matches(canvas, "axes-bars-one-magnitude-edges")


def test_axes_bars_n_magnitudes():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(series)
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes")


def test_axes_bars_n_magnitudes_along_y():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(series, along="y")
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-along-y")


def test_axes_bars_n_magnitudes_centers():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(x, series)
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-centers")


def test_axes_bars_n_magnitudes_edges():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(x1, x2, series)
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-edges")


def test_axes_bars_n_magnitudes_symmetric():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(series, baseline="symmetric")
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-symmetric")


def test_axes_bars_n_magnitudes_wiggle():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(series, baseline="wiggle")
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-wiggle")


def test_axes_bars_n_magnitudes_titles():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(series, baseline="stacked", title=["mean", "standard deviation"])
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-titles")


def test_axes_bars_histogram():
    numpy.random.seed(1234)
    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(numpy.histogram(numpy.random.normal(size=10000), 100))
    assert_canvas_matches(canvas, "axes-bars-histogram")


def test_axes_bars_one_boundary():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y1 = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(y1, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-one-boundary")


def test_axes_bars_one_boundary_centers():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y1 = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(x, y1, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-one-boundary-centers")


def test_axes_bars_one_boundary_edges():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    y1 = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(x1, x2, y1, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-one-boundary-edges")


def test_axes_bars_n_boundaries():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(series, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-n-boundaries")


def test_axes_bars_n_boundaries_along_y():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(series, along="y", baseline=None)
    assert_canvas_matches(canvas, "axes-bars-n-boundaries-along-y")


def test_axes_bars_n_boundaries_centers():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(x, series, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-n-boundaries-centers")


def test_axes_bars_n_boundaries_edges():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(x1, x2, series, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-n-boundaries-edges")


def test_axes_bars_n_boundaries_titles():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.min(
            observations, axis=1), numpy.percentile(
            observations, 25, axis=1), numpy.percentile(
                observations, 50, axis=1), numpy.percentile(
                    observations, 75, axis=1), numpy.max(
                        observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.bars(
        series,
        title=[
            "1st quartile",
            "2nd quartile",
            "3rd quartile",
            "4th quartile"],
        baseline=None)
    assert_canvas_matches(canvas, "axes-bars-n-boundaries-titles")


def test_axes_plot_one_variable():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.plot(y)
    assert_canvas_matches(canvas, "axes-plot-one-variable")


def test_axes_plot_one_variable_x():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.plot(x, y)
    assert_canvas_matches(canvas, "axes-plot-one-variable-x")


def test_axes_plot_n_variables():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.plot(series)
    assert_canvas_matches(canvas, "axes-plot-n-variables")


def test_axes_plot_n_variables_x():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.plot(x, series)
    assert_canvas_matches(canvas, "axes-plot-n-variables-x")


def test_axes_plot_n_variables_along_y():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.plot(series, along="y")
    assert_canvas_matches(canvas, "axes-plot-n-variables-along-y")


def test_axes_plot_masked_nan():
    x = numpy.linspace(0, 2 * numpy.pi, 51)
    y = numpy.ma.column_stack((
        1 + 0.5 * numpy.sin(x),
        1 + 0.5 * numpy.cos(x),
        1 + 0.2 * numpy.sin(2 * x),
    ))
    y[8:18, 0] = numpy.nan
    y[33:43, 1] = numpy.ma.masked

    canvas, axes, mark = toyplot.plot(x, y, marker="o")
    assert_canvas_matches(canvas, "axes-plot-masked-nan")


def test_axes_bars_magnitudes_masked_nan():
    x = numpy.linspace(0, 2 * numpy.pi, 51)
    y = numpy.ma.column_stack((
        1 + 0.5 * numpy.sin(x),
        1 + 0.5 * numpy.cos(x),
        1 + 0.2 * numpy.sin(2 * x),
    ))
    y[8:18, 0] = numpy.nan
    y[33:43, 1] = numpy.ma.masked

    canvas, axes, mark = toyplot.bars(x, y)
    assert_canvas_matches(canvas, "axes-bars-magnitudes-masked-nan")


def test_axes_fill_magnitudes_masked_nan():
    x = numpy.linspace(0, 2 * numpy.pi, 51)
    y = numpy.ma.column_stack((
        1 + 0.5 * numpy.sin(x),
        1 + 0.5 * numpy.cos(x),
        1 + 0.2 * numpy.sin(2 * x),
    ))
    y[8:18, 0] = numpy.nan
    y[33:43, 1] = numpy.ma.masked

    canvas, axes, mark = toyplot.fill(x, y, baseline="stacked")
    assert_canvas_matches(canvas, "axes-fill-magnitudes-masked-nan")


def test_axes_bars_boundaries_masked_nan():
    numpy.random.seed(1234)
    observations = numpy.random.normal(size=(50, 50))
    b = numpy.ma.column_stack((numpy.min(observations, axis=1), numpy.median(
        observations, axis=1), numpy.max(observations, axis=1)))
    b[10:20, 0] = numpy.nan
    b[30:40, 1] = numpy.ma.masked
    b[20:30, 2] = numpy.nan

    canvas, axes, mark = toyplot.bars(b, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-boundaries-masked-nan")


def test_axes_fill_boundaries_masked_nan():
    numpy.random.seed(1234)
    observations = numpy.random.normal(size=(50, 50))
    b = numpy.ma.column_stack((numpy.min(observations, axis=1), numpy.median(
        observations, axis=1), numpy.max(observations, axis=1)))
    b[10:20, 0] = numpy.nan
    b[30:40, 1] = numpy.ma.masked
    b[20:30, 2] = numpy.nan

    canvas, axes, mark = toyplot.fill(b)
    assert_canvas_matches(canvas, "axes-fill-boundaries-masked-nan")


def test_scatterplot_one_variable():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    canvas, axes, mark = toyplot.scatterplot(y)
    assert_canvas_matches(canvas, "scatterplot-one-variable")


def test_axes_scatterplot_one_variable():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.scatterplot(y)
    assert_canvas_matches(canvas, "axes-scatterplot-one-variable")


def test_axes_scatterplot_one_variable_x():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.scatterplot(x, y)
    assert_canvas_matches(canvas, "axes-scatterplot-one-variable-x")


def test_axes_scatterplot_one_variable_fill():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)
    color = numpy.arange(len(observations))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.scatterplot(y, color=color)
    assert_canvas_matches(canvas, "axes-scatterplot-one-variable-fill")


def test_axes_scatterplot_n_variables():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.scatterplot(series)
    assert_canvas_matches(canvas, "axes-scatterplot-n-variables")


def test_axes_scatterplot_n_variables_x():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.scatterplot(x, series)
    assert_canvas_matches(canvas, "axes-scatterplot-n-variables-x")


def test_axes_scatterplot_n_variables_along_y():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.scatterplot(series, along="y")
    assert_canvas_matches(canvas, "axes-scatterplot-n-variables-along-y")


def test_axes_scatterplot_singular():
    x = numpy.linspace(0, 2 * numpy.pi)
    y = numpy.sin(x)

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.plot(x, y)
    axes.scatterplot(x[0], y[0], color="red")
    assert_canvas_matches(canvas, "axes-scatterplot-singular")


def test_axes_scatterplot_markers():
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

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.scatterplot(
        numpy.arange(
            len(markers)),
        color="steelblue",
        marker=markers,
        size=10,
        mstyle=marker_style,
        mlstyle=label_style)
    assert_canvas_matches(canvas, "axes-scatterplot-markers")


def test_axes_rect_singular():
    canvas = toyplot.Canvas()
    axes = canvas.cartesian(xmin=0, xmax=1, ymin=0, ymax=1)
    axes.rects(0.1, 0.2, 0.3, 0.6)
    assert_canvas_matches(canvas, "axes-rect-singular")


def test_axes_rect_singular_along_y():
    canvas = toyplot.Canvas()
    axes = canvas.cartesian(xmin=0, xmax=1, ymin=0, ymax=1)
    axes.rects(0.1, 0.2, 0.3, 0.6, along="y")
    assert_canvas_matches(canvas, "axes-rect-singular-along-y")


def test_axes_rect():
    x1 = numpy.arange(1, 10)
    x2 = x1 + 0.5
    y1 = x1 - 0.5
    y2 = x1 ** 1.5
    color = x1
    title = x1
    colormap = toyplot.color.CategoricalMap(toyplot.color.brewer.palette("BlueRed"))

    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.rects(x1, x2, y1, y2, color=(color, colormap), title=title)
    assert_canvas_matches(canvas, "axes-rect")


def test_animation_frame_sanity_checks():
    frame = toyplot.canvas.AnimationFrame(number=1, begin=2.3, end=2.4, count=1, changes=collections.defaultdict(lambda: collections.defaultdict(list)))
    nose.tools.assert_equal(frame.number, 1)
    nose.tools.assert_equal(frame.begin, 2.3)
    numpy.testing.assert_almost_equal(frame.length, 0.1)
    with nose.tools.assert_raises(ValueError):
        frame.set_mark_style(None, {})
    with nose.tools.assert_raises(ValueError):
        frame.set_datum_style(None, 0, 0, {})


def test_canvas_frame():
    canvas = toyplot.Canvas()
    frame = canvas.frame(0.3, 0.4)
    nose.tools.assert_equal(frame.begin, 0.3)
    numpy.testing.assert_almost_equal(frame.length, 0.1)
    nose.tools.assert_equal(frame.number, 0)

    frame = canvas.frame(0.3, 0.4, 5)
    nose.tools.assert_equal(frame.begin, 0.3)
    numpy.testing.assert_almost_equal(frame.length, 0.1)
    nose.tools.assert_equal(frame.number, 5)

