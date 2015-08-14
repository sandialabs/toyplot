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

import toyplot
import toyplot.color
import toyplot.compatibility
import toyplot.data
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
    import toyplot.cairo.eps
except:
    pass

try:
    import toyplot.cairo.pdf
except:
    pass

try:
    import toyplot.cairo.png
except:
    pass

try:
    import toyplot.qt.pdf
except:
    pass

try:
    import toyplot.qt.png
except:
    pass


##########################################################################
# Test fixtures.

def assert_color_equal(a, b):
    numpy.testing.assert_array_almost_equal(
        (a["r"], a["g"], a["b"], a["a"]), b)


def assert_colors_equal(a, b):
    for j, k in zip(a, b):
        assert_color_equal(j, k)


def assert_masked_array(a, dtype, b, mask):
    nose.tools.assert_is_instance(a, numpy.ma.MaskedArray)
    nose.tools.assert_equal(a.dtype, dtype)
    numpy.testing.assert_array_equal(a, b)
    numpy.testing.assert_array_equal(a.mask, mask)


def json_comparison_string(o):
    """Convert a Python object to a JSON string representation that can be used for comparison.

    Limits the precision of floating-point numbers.
    """
    if o is None:
        return "null"
    if isinstance(o, toyplot.compatibility.string_type):
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
                "{http://www.sandia.gov/toyplot}axes"]:
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

    for module in ["toyplot.pdf", "toyplot.png", "toyplot.cairo.eps", "toyplot.cairo.pdf", "toyplot.cairo.png", "toyplot.qt.pdf", "toyplot.qt.png"]:
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
            file.write(svg_string)
        with open("tests/diffs/%s.reference.svg" % name, "wb") as file:
            file.write(reference_string)
        if not os.path.exists("tests/failed"):
            os.mkdir("tests/failed")
        with open("tests/failed/%s.svg" % name, "wb") as file:
            file.write(svg.getvalue())
        raise AssertionError(
            "Test output tests/failed/%s.svg doesn't match tests/reference/%s.svg:\n%s" %
            (name, name, e))


def assert_html_matches(html, name):
    reference_file = "tests/reference/%s.html" % name
    test_file = "tests/failed/%s.html" % name
    if os.path.exists(test_file):
        os.remove(test_file)
    if os.path.exists(reference_file):
        reference_html = open(reference_file, "rb").read()
        if html != reference_html:
            if not os.path.exists("tests/failed"):
                os.mkdir("tests/failed")
            with open(test_file, "wb") as file:
                file.write(html)
            raise AssertionError(
                "Test output %s doesn't match %s." %
                (test_file, reference_file))
    else:
        with open(reference_file, "wb") as file:
            file.write(html)
        raise AssertionError(
            "Created new reference file %s.  You should verify its contents before re-running the test." %
            (reference_file))

##########################################################################
# Test test fixtures.


def test_xml_comparison_string():
    nose.tools.assert_equal(
        xml_comparison_string(xml.fromstring("<svg/>")), "<svg>\n</svg>\n")
    nose.tools.assert_equal(xml_comparison_string(
        xml.fromstring("<svg><a/></svg>")), "<svg>\n  <a>\n  </a>\n</svg>\n")
    nose.tools.assert_equal(
        xml_comparison_string(
            xml.fromstring("<svg><a>foo</a></svg>")),
        "<svg>\n  <a>foo\n  </a>\n</svg>\n")
    nose.tools.assert_equal(
        xml_comparison_string(
            xml.fromstring("<svg><a b='c'>foo</a></svg>")),
        "<svg>\n  <a b='c'>foo\n  </a>\n</svg>\n")
    nose.tools.assert_equal(
        xml_comparison_string(
            xml.fromstring("<svg><a b='.333333333333333'>foo</a></svg>")),
        "<svg>\n  <a b='0.333333333'>foo\n  </a>\n</svg>\n")
    nose.tools.assert_equal(
        xml_comparison_string(
            xml.fromstring("<svg><a b='.666666666666666'>foo</a></svg>")),
        "<svg>\n  <a b='0.666666667'>foo\n  </a>\n</svg>\n")
    nose.tools.assert_equal(
        xml_comparison_string(
            xml.fromstring("<svg><a id='1234'/></svg>")),
        "<svg>\n  <a>\n  </a>\n</svg>\n")

##########################################################################
# toyplot


def test_require_style():
    nose.tools.assert_equal(toyplot.require.style(None), None)
    nose.tools.assert_equal(toyplot.require.style({}), {})
    nose.tools.assert_equal(toyplot.require.style(
        {"stroke": toyplot.color.near_black}), {"stroke": toyplot.color.near_black})
    with nose.tools.assert_raises(ValueError):
        toyplot.require.style([])
    with nose.tools.assert_raises(ValueError):
        toyplot.require.style("")


def test_style_combine():
    nose.tools.assert_equal(toyplot.style.combine(None), {})
    nose.tools.assert_equal(toyplot.style.combine({}), {})
    nose.tools.assert_equal(
        toyplot.style.combine({"a": "b"}, None), {"a": "b"})
    nose.tools.assert_equal(toyplot.style.combine({"a": "b"}, {}), {"a": "b"})
    nose.tools.assert_equal(
        toyplot.style.combine({"a": "b"}, {"c": "d"}), {"a": "b", "c": "d"})
    nose.tools.assert_equal(
        toyplot.style.combine({"a": "b"}, {"a": "d"}), {"a": "d"})


def test_require_scalar():
    nose.tools.assert_equal(toyplot.require.scalar(1), 1)
    nose.tools.assert_equal(toyplot.require.scalar(1.2), 1.2)
    with nose.tools.assert_raises(ValueError):
        nose.tools.assert_equal(toyplot.require.scalar("foo"), "foo")


def test_require_scalar_array():
    assert_masked_array(
        toyplot.require.scalar_array(1), "float64", [1], [False])
    assert_masked_array(
        toyplot.require.scalar_array(1.1), "float64", [1.1], [False])
    assert_masked_array(
        toyplot.require.scalar_array("1.2"), "float64", [1.2], [False])
    assert_masked_array(toyplot.require.scalar_array(
        [1, 2, 3]), "float64", [1, 2, 3], [False, False, False])
    assert_masked_array(toyplot.require.scalar_array(
        ["1", "2", 3]), "float64", [1, 2, 3], [False, False, False])
    assert_masked_array(toyplot.require.scalar_array([[1, 2], [3, 4]]), "float64", [
                        [1, 2], [3, 4]], [[False, False], [False, False]])
    assert_masked_array(toyplot.require.scalar_array(
        numpy.array([1, 2, 3])), "float64", [1, 2, 3], [False, False, False])
    assert_masked_array(
        toyplot.require.scalar_array(
            numpy.ma.array(
                [
                    1, 2, 3], mask=[
                    False, True, False])), "float64", [
                        1, 2, 3], [
                            False, True, False])
    assert_masked_array(
        toyplot.require.scalar_array(
            numpy.array(
                [
                    1, numpy.nan, 3])), "float64", [
            1, numpy.nan, 3], [
                        False, True, False])
    assert_masked_array(
        toyplot.require.scalar_array(
            numpy.ma.array(
                [
                    1, numpy.nan, 3], mask=[
                    False, False, True])), "float64", [
                        1, numpy.nan, 3], [
                            False, True, True])
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_array("foo")
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_array(["1", "foo"])


def test_require_scalar_vector():
    numpy.testing.assert_array_equal(toyplot.require.scalar_vector(1), [1])
    numpy.testing.assert_array_equal(
        toyplot.require.scalar_vector([1, 2, 3]), [1, 2, 3])
    numpy.testing.assert_array_equal(
        toyplot.require.scalar_vector([1, 2, 3], length=3), [1, 2, 3])
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_vector(1, length=3)
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_vector([1, 2, 3], length=2)
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_vector([[1, 2], [3, 4]])


def test_require_scalar_matrix():
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_matrix(1)
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_matrix([1, 2, 3])
    numpy.testing.assert_array_equal(
        toyplot.require.scalar_matrix([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_matrix([[1, 2], [3, 4]], rows=3)
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_matrix([[1, 2], [3, 4]], columns=3)
    with nose.tools.assert_raises(ValueError):
        toyplot.require.scalar_matrix([[[1, 2], [3, 4]]])


def test_require_string():
    nose.tools.assert_equal(toyplot.require.string("foo"), "foo")
    nose.tools.assert_equal(toyplot.require.string(u"foo"), u"foo")
    with nose.tools.assert_raises(ValueError):
        nose.tools.assert_equal(toyplot.require.string(None), None)
    with nose.tools.assert_raises(ValueError):
        nose.tools.assert_equal(toyplot.require.string(1), 1)


def test_require_string_vector():
    numpy.testing.assert_array_equal(toyplot.require.string_vector("a"), ["a"])
    numpy.testing.assert_array_equal(
        toyplot.require.string_vector(["a", "b", "c"]), ["a", "b", "c"])
    numpy.testing.assert_array_equal(
        toyplot.require.string_vector([1, 2, 3]), ["1", "2", "3"])


def test_require_optional_string():
    nose.tools.assert_equal(toyplot.require.optional_string("foo"), "foo")
    nose.tools.assert_equal(toyplot.require.optional_string(u"foo"), u"foo")
    nose.tools.assert_equal(toyplot.require.optional_string(None), None)
    with nose.tools.assert_raises(ValueError):
        nose.tools.assert_equal(toyplot.require.optional_string(1), 1)


def test_require_marker_array():
    numpy.testing.assert_array_equal(
        toyplot.require.marker_array("foo"), ["foo"])
    numpy.testing.assert_array_equal(
        toyplot.require.marker_array(["foo", "bar"]), ["foo", "bar"])
    numpy.testing.assert_array_equal(
        toyplot.require.marker_array([1, 2]), [1, 2])
    numpy.testing.assert_array_equal(
        toyplot.require.marker_array([1, 2, "foo"]), [1, 2, "foo"])
    with nose.tools.assert_raises(ValueError):
        toyplot.require.marker_array(["foo", "bar"], 3)


def test_broadcast_scalar():
    numpy.testing.assert_equal(toyplot.broadcast.scalar(1, 3), [1, 1, 1])
    numpy.testing.assert_equal(
        toyplot.broadcast.scalar(1, (3, 3)), [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    numpy.testing.assert_equal(
        toyplot.broadcast.scalar([1, 2, 3], 3), [1, 2, 3])
    numpy.testing.assert_equal(
        toyplot.broadcast.scalar([1, 2, 3], (3, 3)), [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    numpy.testing.assert_equal(toyplot.broadcast.scalar(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], (3, 3)), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    numpy.testing.assert_equal(
        toyplot.broadcast.scalar([1, 2, 3], (3, 1)), [[1], [2], [3]])


def test_broadcast_string():
    numpy.testing.assert_equal(
        toyplot.broadcast.string("1", 3), ["1", "1", "1"])
    numpy.testing.assert_equal(toyplot.broadcast.string(
        "1", (3, 3)), [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]])
    numpy.testing.assert_equal(
        toyplot.broadcast.string(["1", "2", "3"], 3), ["1", "2", "3"])
    numpy.testing.assert_equal(toyplot.broadcast.string(
        ["1", "2", "3"], (3, 3)), [["1", "2", "3"], ["1", "2", "3"], ["1", "2", "3"]])
    numpy.testing.assert_equal(toyplot.broadcast.string([["1", "2", "3"], ["4", "5", "6"], [
                               "7", "8", "9"]], (3, 3)), [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
    numpy.testing.assert_equal(
        toyplot.broadcast.string(["1", "2", "3"], (3, 1)), [["1"], ["2"], ["3"]])


def test_axes_coordinates_show():
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.coordinates.show = False
    nose.tools.assert_equal(axes.coordinates.show, False)
    assert_canvas_matches(canvas, "axes-coordinates-show")


def test_axes_coordinates_style():
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.coordinates.style = {"stroke": "red", "fill": "ivory"}
    nose.tools.assert_equal(axes.coordinates.style["stroke"], "red")
    assert_canvas_matches(canvas, "axes-coordinates-style")


def test_axes_coordinates_label():
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.coordinates.label.style = {"fill": "red"}
    nose.tools.assert_equal(axes.coordinates.label.style["fill"], "red")
    assert_canvas_matches(canvas, "axes-coordinates-label")


def test_axes_tick_titles():
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.x.ticks.locator = toyplot.locator.Explicit(
        locations=[-0.5, 0, 0.5], titles=["Foo", "Bar", "Baz"])
    axes.y.ticks.locator = toyplot.locator.Explicit(
        locations=[-0.5, 0, 0.5], titles=["Red", "Green", "Blue"])
    assert_canvas_matches(canvas, "axes-tick-titles")


def test_axes_colorbar():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar()
    assert_canvas_matches(canvas, "axes-colorbar")


def test_axes_colorbar_data():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(
        numpy.arange(100), palette=toyplot.color.brewer("BlueYellowRed"))
    assert_canvas_matches(canvas, "axes-colorbar-ticks-data")


def test_axes_colorbar_domain():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.domain.min = 0
    nose.tools.assert_equal(colorbar.domain.min, 0)
    colorbar.domain.max = 1
    nose.tools.assert_equal(colorbar.domain.max, 1)
    assert_canvas_matches(canvas, "axes-colorbar-domain")


def test_axes_colorbar_label():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.label.text = "Colorbar Label"
    nose.tools.assert_equal(colorbar.label.text, "Colorbar Label")
    colorbar.label.style = {"fill": "red"}
    nose.tools.assert_equal(colorbar.label.style["fill"], "red")
    assert_canvas_matches(canvas, "axes-colorbar-label")


def test_axes_colorbar_ticks_show():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.show = True
    nose.tools.assert_equal(colorbar.ticks.show, True)
    assert_canvas_matches(canvas, "axes-colorbar-ticks-show")


def test_axes_colorbar_ticks_length():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.show = True
    colorbar.ticks.length = 20
    nose.tools.assert_equal(colorbar.ticks.length, 20)
    assert_canvas_matches(canvas, "axes-colorbar-ticks-length")


def test_axes_colorbar_ticks_style():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.show = True
    colorbar.ticks.style = {"stroke": "red"}
    nose.tools.assert_equal(colorbar.ticks.style["stroke"], "red")
    assert_canvas_matches(canvas, "axes-colorbar-ticks-style")


def test_axes_colorbar_ticks_locator():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.show = True
    locator = toyplot.locator.Explicit(
        locations=[-0.5, 0.0, 0.5], titles=["blue", "yellow", "red"])
    colorbar.ticks.locator = locator
    nose.tools.assert_is(colorbar.ticks.locator, locator)
    assert_canvas_matches(canvas, "axes-colorbar-ticks-locator")


def test_axes_colorbar_ticks_tick_index_style():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.show = True
    colorbar.ticks.tick(index=1).style = {"stroke": "red"}
    nose.tools.assert_equal(
        colorbar.ticks.tick(index=1).style["stroke"], "red")
    assert_canvas_matches(canvas, "axes-colorbar-ticks-tick-index-style")


def test_axes_colorbar_ticks_tick_value_style():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.show = True
    colorbar.ticks.tick(value=0.5).style = {"stroke": "red"}
    nose.tools.assert_equal(
        colorbar.ticks.tick(value=0.5).style["stroke"], "red")
    assert_canvas_matches(canvas, "axes-colorbar-ticks-tick-value-style")


def test_axes_colorbar_ticks_labels_show():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.labels.show = False
    nose.tools.assert_equal(colorbar.ticks.labels.show, False)
    assert_canvas_matches(canvas, "axes-colorbar-ticks-labels-show")


def test_axes_colorbar_ticks_labels_style():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.labels.style = {"fill": "red"}
    nose.tools.assert_equal(colorbar.ticks.labels.style["fill"], "red")
    assert_canvas_matches(canvas, "axes-colorbar-ticks-labels-style")


def test_axes_colorbar_ticks_labels_label_index_style():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.labels.label(index=1).style = {"fill": "red"}
    nose.tools.assert_equal(
        colorbar.ticks.labels.label(index=1).style["fill"], "red")
    assert_canvas_matches(
        canvas, "axes-colorbar-ticks-labels-label-index-style")


def test_axes_colorbar_ticks_labels_label_value_style():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
    colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
    colorbar.ticks.labels.label(value=0.5).style = {"fill": "red"}
    nose.tools.assert_equal(
        colorbar.ticks.labels.label(value=0.5).style["fill"], "red")
    assert_canvas_matches(
        canvas, "axes-colorbar-ticks-labels-label-value-style")


def test_axes_palette():
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    for i in range(10):
        axes.plot(numpy.arange(2), numpy.repeat(i, 2))
    assert_canvas_matches(canvas, "axes-palette")


def test_axes_palettes():
    canvas = toyplot.Canvas()
    axes = canvas.axes()
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
    axes = canvas.axes()
    axes.bars(y)
    assert_canvas_matches(canvas, "axes-bars-one-magnitude")


def test_axes_bars_one_magnitude_centers():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.axes()
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
    axes = canvas.axes()
    axes.bars(x1, x2, y)
    assert_canvas_matches(canvas, "axes-bars-one-magnitude-edges")


def test_axes_bars_n_magnitudes():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.bars(series)
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes")


def test_axes_bars_n_magnitudes_along_y():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.bars(series, along="y")
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-along-y")


def test_axes_bars_n_magnitudes_centers():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
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
    axes = canvas.axes()
    axes.bars(x1, x2, series)
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-edges")


def test_axes_bars_n_magnitudes_symmetric():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.bars(series, baseline="symmetric")
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-symmetric")


def test_axes_bars_n_magnitudes_wiggle():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.bars(series, baseline="wiggle")
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-wiggle")


def test_axes_bars_n_magnitudes_titles():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.bars(series, baseline="stacked", title=["mean", "standard deviation"])
    assert_canvas_matches(canvas, "axes-bars-n-magnitudes-titles")


def test_axes_bars_histogram():
    numpy.random.seed(1234)
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.bars(numpy.histogram(numpy.random.normal(size=10000), 100))
    assert_canvas_matches(canvas, "axes-bars-histogram")


def test_axes_bars_one_boundary():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y1 = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.bars(y1, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-one-boundary")


def test_axes_bars_one_boundary_centers():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y1 = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.axes()
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
    axes = canvas.axes()
    axes.bars(x1, x2, y1, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-one-boundary-edges")


def test_axes_bars_n_boundaries():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.bars(series, baseline=None)
    assert_canvas_matches(canvas, "axes-bars-n-boundaries")


def test_axes_bars_n_boundaries_along_y():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.bars(series, along="y", baseline=None)
    assert_canvas_matches(canvas, "axes-bars-n-boundaries-along-y")


def test_axes_bars_n_boundaries_centers():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
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
    axes = canvas.axes()
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
    axes = canvas.axes()
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
    axes = canvas.axes()
    axes.plot(y)
    assert_canvas_matches(canvas, "axes-plot-one-variable")


def test_axes_plot_one_variable_x():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.plot(x, y)
    assert_canvas_matches(canvas, "axes-plot-one-variable-x")


def test_axes_plot_n_variables():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.plot(series)
    assert_canvas_matches(canvas, "axes-plot-n-variables")


def test_axes_plot_n_variables_x():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.plot(x, series)
    assert_canvas_matches(canvas, "axes-plot-n-variables-x")


def test_axes_plot_n_variables_along_y():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
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

    canvas, axes, mark = toyplot.plot(x, y, marker="o", size="64")
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
    axes = canvas.axes()
    axes.scatterplot(y)
    assert_canvas_matches(canvas, "axes-scatterplot-one-variable")


def test_axes_scatterplot_one_variable_x():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.scatterplot(x, y)
    assert_canvas_matches(canvas, "axes-scatterplot-one-variable-x")


def test_axes_scatterplot_one_variable_fill():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)
    fill = numpy.arange(len(observations))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.scatterplot(y, fill=fill)
    assert_canvas_matches(canvas, "axes-scatterplot-one-variable-fill")


def test_axes_scatterplot_n_variables():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.scatterplot(series)
    assert_canvas_matches(canvas, "axes-scatterplot-n-variables")


def test_axes_scatterplot_n_variables_x():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.scatterplot(x, series)
    assert_canvas_matches(canvas, "axes-scatterplot-n-variables-x")


def test_axes_scatterplot_n_variables_along_y():
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.scatterplot(series, along="y")
    assert_canvas_matches(canvas, "axes-scatterplot-n-variables-along-y")


def test_axes_scatterplot_singular():
    x = numpy.linspace(0, 2 * numpy.pi)
    y = numpy.sin(x)

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.plot(x, y)
    axes.scatterplot(x[0], y[0], fill="red")
    assert_canvas_matches(canvas, "axes-scatterplot-singular")


def test_axes_scatterplot_markers():
    marker_style = {"stroke": toyplot.color.near_black, "fill": "cornsilk"}
    label_style = {"stroke": "none", "fill": toyplot.color.near_black}
    markers = [
        None,
        "",
        "|",
        "-",
        {"shape": "|", "angle": -45},
        {"shape": "|", "angle": 45},
        "+",
        "x",
        {"shape": "x", "angle": -22.5},
        "*",
        "^",
        {"shape": ">", "mstyle": {"stroke": "red"}},
        {"shape": "v", "mstyle": {"stroke": "red", "fill": "yellow"}},
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
        {"shape": "", "label": "A"},
        {"shape": "o", "label": "1"},
        {"shape": "s", "mstyle": {"stroke": "blue", "fill": "white"},
         "label": "B", "lstyle": {"fill": "blue"}},
        {"shape": "d", "label": "2", "lstyle": {"fill": "green"}},
    ]

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.scatterplot(
        numpy.arange(
            len(markers)),
        fill="steelblue",
        marker=markers,
        size=100,
        mstyle=marker_style,
        mlstyle=label_style)
    assert_canvas_matches(canvas, "axes-scatterplot-markers")


def test_axes_rect_singular():
    canvas = toyplot.Canvas()
    axes = canvas.axes(xmin=0, xmax=1, ymin=0, ymax=1)
    axes.rect(0.1, 0.2, 0.3, 0.6)
    assert_canvas_matches(canvas, "axes-rect-singular")


def test_axes_rect_singular_along_y():
    canvas = toyplot.Canvas()
    axes = canvas.axes(xmin=0, xmax=1, ymin=0, ymax=1)
    axes.rect(0.1, 0.2, 0.3, 0.6, along="y")
    assert_canvas_matches(canvas, "axes-rect-singular-along-y")


def test_axes_rect():
    x1 = numpy.arange(1, 10)
    x2 = x1 + 0.5
    y1 = x1 - 0.5
    y2 = x1 ** 1.5
    fill = x1
    title = x1
    palette = toyplot.color.brewer("BlueRed")

    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.rect(x1, x2, y1, y2, fill=(fill, palette), title=title)
    assert_canvas_matches(canvas, "axes-rect")


def test_axes_text():
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    x = numpy.linspace(0, 1)
    y = numpy.sin(x * 10)
    text = ["s%s" % index for index in range(len(x))]
    axes.text(x, y, text, annotation=False)
    assert_canvas_matches(canvas, "axes-text")


def test_axes_text_angle_fill():
    x = numpy.zeros(10)
    y = x
    angle = numpy.linspace(-90, 0, len(x), endpoint=True)
    fill = numpy.linspace(1, 0, len(x))

    canvas = toyplot.Canvas(400, 400)
    axes = canvas.axes(xmin=-0.25, xmax=0.5, ymin=-0.5, ymax=0.25)
    axes.text(
        x,
        y,
        text="Toyplot!",
        angle=angle,
        fill=fill,
        style={
            "font-size": "36px",
            "font-weight": "bold",
            "stroke": "white",
            "text-anchor": "start"})

    assert_canvas_matches(canvas, "axes-text-angle-fill")


def test_axes_legend():
    canvas = toyplot.Canvas()
    axes = canvas.axes(grid=(2, 2, 1, 1))
    axes.legend(
        (("foo", "s"), ("bar", "o")), corner=("bottom-left", 30, 100, 50))
    assert_canvas_matches(canvas, "axes-legend")


def test_animation_frame_sanity_checks():
    frame = toyplot.canvas.AnimationFrame(
        index=1,
        begin=2.3,
        end=2.4,
        changes=collections.defaultdict(
            lambda: collections.defaultdict(list)))
    nose.tools.assert_equal(frame.index(), 1)
    nose.tools.assert_equal(frame.time(), 2.3)
    numpy.testing.assert_almost_equal(frame.duration(), 0.1)
    with nose.tools.assert_raises(ValueError):
        frame.set_mark_style(None, {})
    with nose.tools.assert_raises(ValueError):
        frame.set_datum_style(None, 0, 0, {})
    with nose.tools.assert_raises(ValueError):
        frame.set_datum_text(None, 0, 0, "")


def test_canvas_defaults():
    canvas = toyplot.Canvas()
    assert_canvas_matches(canvas, "canvas-defaults")


def test_canvas_time():
    canvas = toyplot.Canvas()
    frame = canvas.time(0.3, 0.4)
    nose.tools.assert_equal(frame.time(), 0.3)
    numpy.testing.assert_almost_equal(frame.duration(), 0.1)
    nose.tools.assert_equal(frame.index(), 0)

    frame = canvas.time(0.3, 0.4, 5)
    nose.tools.assert_equal(frame.time(), 0.3)
    numpy.testing.assert_almost_equal(frame.duration(), 0.1)
    nose.tools.assert_equal(frame.index(), 5)


def test_canvas_repr_html():
    canvas = toyplot.Canvas(autorender="html")
    html = canvas._repr_html_()
    nose.tools.assert_is_instance(html, toyplot.compatibility.unicode_type)


def test_explicit_tick_locator_failure():
    with nose.tools.assert_raises(ValueError):
        toyplot.locator.Explicit()

##########################################################################
# toyplot.html


def test_color_require_color():
    assert_color_equal(toyplot.color._require_color("red"), (1, 0, 0, 1))
    assert_color_equal(
        toyplot.color._require_color(toyplot.color.rgb(1, 1, 0)), (1, 1, 0, 1))
    assert_color_equal(toyplot.color._require_color(
        toyplot.color.rgba(1, 1, 0, 0.5)), (1, 1, 0, 0.5))
    assert_color_equal(toyplot.color._require_color((1, 1, 0)), (1, 1, 0, 1))
    assert_color_equal(
        toyplot.color._require_color((1, 1, 0, 0.5)), (1, 1, 0, 0.5))
    with nose.tools.assert_raises(ValueError):
        toyplot.color._require_color(5)

##########################################################################
# toyplot.html


def test_html_render_animation():
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    text = canvas.text(100, 100, "")
    scatterplot = axes.scatterplot(numpy.arange(10))

    def callback(frame):
        frame.set_mark_style(text, {"fill-opacity": frame.time()})
        frame.set_datum_text(text, 0, 0, "frame %s time %s duration %s" % (
            frame.index(), frame.time(), frame.duration()))
        frame.set_datum_style(
            scatterplot, 0, frame.index(), {"stroke": "none"})
    canvas.animate(10, callback)
    dom = toyplot.html.render(canvas)


def test_html_ipython_html():
    canvas = toyplot.Canvas()
    canvas.axes()
    canvas._repr_html_()

##########################################################################
# toyplot.png


def test_png_render_frames():
    if hasattr(toyplot, "png"):
        canvas = toyplot.Canvas()
        axes = canvas.axes()
        text = canvas.text(100, 100, "")
        scatterplot = axes.scatterplot(numpy.arange(10))

        def callback(frame):
            frame.set_mark_style(text, {"fill-opacity": frame.time()})
            frame.set_datum_text(text, 0, 0, "frame %s" % frame.index())
            frame.set_datum_style(
                scatterplot, 0, frame.index(), {"stroke": "none"})
        canvas.animate(10, callback)
        for frame in toyplot.png.render_frames(canvas):
            nose.tools.assert_is_instance(
                frame, toyplot.compatibility.string_type)
            nose.tools.assert_equal(frame[1:4], "PNG")


def test_cairo_small_font():
    if hasattr(toyplot, "png"):
        canvas = toyplot.Canvas()
        axes = canvas.axes(label="Small Text!")
        axes.label.style = {"font-size": "8px"}
        toyplot.png.render(canvas)

##########################################################################
# High-level tests that combine multiple API calls into whole figures.


def test_basic_api():
    numpy.random.seed(1234)
    x = numpy.linspace(0, 1, 100)
    y = x + (0.1 * x * numpy.random.random(len(x)))

    canvas = toyplot.Canvas()
    axes = canvas.axes(grid=(2, 2, 0, 1, 0, 2))
    axes.plot(
        x, y, style={"stroke": "steelblue", "stroke-width": 1.0}, marker="o")
    axes.x.label.text = "1st Axis"
    axes.y.label.text = "2nd Axis"

    axes = canvas.axes(grid=(2, 2, 2), label="2nd Axes")
    axes.plot(x, y, style={"stroke": "red"})

    axes = canvas.axes(grid=(2, 2, 3), label="3rd Axes")
    axes.plot(x, y, style={"stroke": "green"})

    canvas.text(
        300,
        30,
        "Plot Title",
        style={
            "font-size": "16px",
            "font-weight": "bold",
            "text-anchor": "middle"},
        title="The plot's title")

    assert_canvas_matches(canvas, "basic-api")


def test_axes_clipping():
    x = numpy.linspace(0, 2 * numpy.pi, 100)
    canvas = toyplot.Canvas()
    axes = canvas.axes(xmin=0.5, xmax=4.5, ymin=-0.5, ymax=0.5)
    axes.plot(x, numpy.sin(x))
    axes.plot(x, numpy.cos(x))
    assert_canvas_matches(canvas, "axes-clipping")


def test_axes():
    x = numpy.linspace(0, 2 * numpy.pi, 200)
    canvas = toyplot.Canvas(800, 400)
    axes = canvas.axes(xlabel="Time", ylabel="Value")
    axes.hlines(0, style={"stroke-dasharray": "5,5"}, title="y = 0")
    axes.vlines(0, style={"stroke-dasharray": "5,5"}, title="x = 0")
    for i in numpy.linspace(1, 2, 7):
        axes.plot(x, 0.5 * i * numpy.sin(x * i),
                  title="%s * sin(x * %s)" % (0.5 * i, i))
    assert_canvas_matches(canvas, "axes")


def test_axes_layout():
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Title", xlabel="X Label",
                       ylabel="Y Label", xmin=0, xmax=1, ymin=0, ymax=1)
    axes.text(
        0.5,
        0.5,
        "Axes Region",
        style={
            "fill": toyplot.color.near_black,
            "text-anchor": "middle",
            "alignment-baseline": "middle"})
    assert_canvas_matches(canvas, "axes-layout")


def test_legend():
    x = numpy.linspace(0, 2 * numpy.pi, 200)
    canvas = toyplot.Canvas(800, 600)
    axes = canvas.axes()
    plots = [axes.plot(x, 0.5 * i * numpy.sin(x * i))
             for i in numpy.linspace(1, 2, 3)]
    fill = axes.fill(x, numpy.sin(x) * 0.1, numpy.cos(x) * 0.1)
    axes.x.label.text = "Time"
    axes.y.label.text = "Temp"
    canvas.legend([
        ("Plot 1", plots[0]),
        ("Plot 2", plots[1]),
        ("Plot 3", plots[2]),
        ("Fill", fill),
        ("Explicit Line", "line", {"stroke": "red", "stroke-width": 1.0}),
        ("Explicit Rect", "rect", {"fill": "green"}),
        ("Explicit Marker", "^", {
            "fill": "lightblue", "stroke": toyplot.color.near_black}),
        ("Explicit Marker", "o", {
            "fill": "yellow", "stroke": toyplot.color.near_black}),
        ("Explicit Marker", "s", {"fill": "pink", "stroke": toyplot.color.near_black})],
        bounds=(100, 200, 350, 550),
    )
    assert_canvas_matches(canvas, "legend")


def test_bounds_placement():
    style = {"stroke": toyplot.color.near_black}
    canvas = toyplot.Canvas(
        800, 600, style={"border": "1px solid %s" % toyplot.color.near_black})
    canvas.legend([], style=style, bounds=(400 - 100, 400 + 100, 20, 50))
    canvas.legend([], style=style, bounds=("25%", 400 + 100, 80, 110))
    canvas.legend([], style=style, bounds=(400 - 100, "75%", 140, 170))
    canvas.legend([], style=style, bounds=("33%", "66%", 200, 230))
    canvas.legend([], style=style, bounds=(20, 50, 450 - 20, 450 + 20))
    canvas.legend([], style=style, bounds=(80, 110, "50%", 450 + 20))
    canvas.legend([], style=style, bounds=(140, 170, 450 - 20, "90%"))
    canvas.legend([], style=style, bounds=(200, 230, "50%", "90%"))
    canvas.legend([], style=style, bounds=("66%", "90%", "66%", "90%"))
    assert_canvas_matches(canvas, "bounds-placement")


def test_corner_placement():
    style = {"stroke": toyplot.color.near_black}
    canvas = toyplot.Canvas(
        800, 600, style={"border": "1px solid %s" % toyplot.color.near_black})
    canvas.legend([("top", "^")], style=style, corner=("top", 10, 100, 30))
    canvas.legend(
        [("top-right", "^")], style=style, corner=("top-right", 10, 100, 30))
    canvas.legend([("right", "^")], style=style, corner=("right", 10, 100, 30))
    canvas.legend(
        [("bottom-right", "^")], style=style, corner=("bottom-right", 10, 150, 30))
    canvas.legend(
        [("bottom", "^")], style=style, corner=("bottom", 10, 100, 30))
    canvas.legend(
        [("bottom-left", "^")], style=style, corner=("bottom-left", 10, 100, 30))
    canvas.legend([("left", "^")], style=style, corner=("left", 10, 100, 30))
    canvas.legend(
        [("top-left", "^")], style=style, corner=("top-left", 10, 100, 30))
    canvas.legend(
        [("top-left", "^")], style=style, corner=("top-left", 50, 100, 30))
    canvas.legend(
        [("top-left", "^")], style=style, corner=("top-left", 100, "20%", "10%"))
    assert_canvas_matches(canvas, "corner-placement")


def test_grid_placement():
    x = numpy.linspace(0, 2 * numpy.pi, 1000)
    canvas = toyplot.Canvas(
        800, 600, style={"border": "1px solid %s" % toyplot.color.near_black})
    inset = canvas.axes(grid=(3, 3, 0), label="3x3 Grid")
    inset.plot(x, numpy.sin(x))
    inset = canvas.axes(grid=(3, 3, 0, 1, 1, 2), label="3x3 Grid colspan=2")
    inset.plot(x, numpy.sin(x))
    inset = canvas.axes(
        grid=(3, 3, 1, 0), gutter=20, label="3x3 Grid gutter=20")
    inset.plot(x, numpy.sin(x))
    inset = canvas.axes(
        grid=(3, 3, 1, 1), gutter=20, label="3x3 Grid gutter=20")
    inset.plot(x, numpy.sin(x))
    inset = canvas.axes(
        grid=(
            3,
            3,
            1,
            2,
            2,
            1),
        gutter=20,
        label="3x3 Grid gutter=20 rowspan=2")
    inset.plot(x, numpy.sin(x))
    assert_canvas_matches(canvas, "grid-placement")
