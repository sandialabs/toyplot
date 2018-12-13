# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import absolute_import, division

import collections
import io
import json
import os
import numbers
import re
import subprocess
import sys
import xml.etree.ElementTree as xml

import numpy.testing
import png
import six

import toyplot.html
import toyplot.require
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

root_dir = os.path.dirname(os.path.dirname(__file__))
failed_dir = os.path.join(root_dir, "failed")
reference_dir = os.path.join(root_dir, "reference")
backend_dir = os.path.join(root_dir, "backends")


def _assert_string_equal(content, test_file, reference_file, encoding="utf-8"):
    if os.path.exists(test_file):
        os.remove(test_file)
    if os.path.exists(reference_file):
        reference = six.text_type(
            open(reference_file, "rb").read(), encoding=encoding)
        if content != reference:
            if not os.path.exists(failed_dir):
                os.mkdir(failed_dir)
            with open(test_file, "wb") as stream:
                stream.write(content.encode(encoding))
            raise AssertionError(
                "Test output %s doesn't match %s." %
                (test_file, reference_file))
    else:
        with open(reference_file, "wb") as stream:
            stream.write(content.encode(encoding))
        raise AssertionError(
            "Created new reference file %s.  You should verify its contents before re-running the test." %
            (reference_file))


def assert_color_equal(a, b):
    """Raise an exception if a toyplot color doesn't match a reference.

    Parameters
    ----------
    a: toyplot RGBA color, required
    b: 4-tuple
    """
    if a is None and b is None:
        return
    numpy.testing.assert_array_almost_equal(
        (a["r"], a["g"], a["b"], a["a"]), b)


def assert_colors_equal(a, b):
    """Raise an exception if sequence of toyplot colors don't match a reference.

    Parameters
    ----------
    a: sequence of toyplot RGBA colors, required
    b: sequence of 4-tuples
    """
    for ai, bi in zip(a, b):
        if ai is not None and bi is not None:
            numpy.testing.assert_array_almost_equal(
                (ai["r"], ai["g"], ai["b"], ai["a"]), bi)


def assert_html_equal(html, name):
    """Raise an exception if HTML content doesn't match a reference.

    Parameters
    ----------
    html: string, required
      The HTML content to be compared.
    name: string, required
      Unique identifier of the reference file to use as a comparison.
      The reference file will be located at toyplot/features/reference/<name>.html
    """
    test_file = os.path.join(failed_dir, "%s.html" % name)
    reference_file = os.path.join(reference_dir, "%s.html" % name)
    _assert_string_equal(html, test_file, reference_file)


def attribute_mismatch(tag, key, avalue, bvalue):
    raise AssertionError("Tag %r attribute %r value\n\t%r\ndoes not match\n\t%r." % (tag, key, avalue, bvalue))


def optional_float(value):
    try:
        return float(value)
    except:
        return value


def assert_mixed_list_equal(alist, blist, tag, key, avalue, bvalue):
    print(alist)
    print(blist)
    if len(alist) != len(blist):
        attribute_mismatch(tag, key, avalue, bvalue)

    for a, b in zip(alist, blist):
        if isinstance(a, float):
            if not numpy.allclose(a, b):
                attribute_mismatch(tag, key, avalue, bvalue)
        else:
            if a != b:
                attribute_mismatch(tag, key, avalue, bvalue)


def assert_path_equal(tag, key, avalue, bvalue):
    alist = [optional_float(value) for value in avalue.split()]
    blist = [optional_float(value) for value in bvalue.split()]
    assert_mixed_list_equal(alist, blist, tag, key, avalue, bvalue)


def assert_points_equal(tag, key, avalue, bvalue):
    alist = [float(value) for pair in avalue.split() for value in pair.split(",")]
    blist = [float(value) for pair in bvalue.split() for value in pair.split(",")]
    assert_mixed_list_equal(alist, blist, tag, key, avalue, bvalue)


def assert_style_equal(tag, key, avalue, bvalue):
    alist = [optional_float(value) for pair in avalue.split(":") for value in pair.split(";") if not value.startswith("url(")]
    blist = [optional_float(value) for pair in bvalue.split(":") for value in pair.split(";") if not value.startswith("url(")]
    assert_mixed_list_equal(alist, blist, tag, key, avalue, bvalue)


def assert_transform_equal(tag, key, avalue, bvalue):
    alist = [optional_float(value.strip()) for value in re.split("[(,)]", avalue)]
    blist = [optional_float(value.strip()) for value in re.split("[(,)]", bvalue)]
    assert_mixed_list_equal(alist, blist, tag, key, avalue, bvalue)


def assert_dom_equal(a, b, exceptions):
    if a.tag != b.tag:
        raise AssertionError("Tag %r does not match %r." % (a.tag, b.tag))

    for (akey, avalue), (bkey, bvalue) in zip(a.items(), b.items()):
        if akey != bkey:
            raise AssertionError("Tag %r attribute %r does not match %r." % (a.tag, akey, bkey))

        # Optionally skip some tag/attribute pairs
        exception = exceptions.get(a.tag, {})
        exception = exception.get(akey, {})
        if exception.get("ignore", False):
            continue

        if exception.get("type", None) == "float":
            if not numpy.allclose(float(avalue), float(bvalue)):
                attribute_mismatch(a.tag, akey, avalue, bvalue)
        elif exception.get("type", None) == "path":
            assert_path_equal(a.tag, akey, avalue, bvalue)
        elif exception.get("type", None) == "points":
            assert_points_equal(a.tag, akey, avalue, bvalue)
        elif exception.get("type", None) == "style":
            assert_style_equal(a.tag, akey, avalue, bvalue)
        elif exception.get("type", None) == "transform":
            assert_transform_equal(a.tag, akey, avalue, bvalue)
        else:
            if avalue != bvalue:
                attribute_mismatch(a.tag, akey, avalue, bvalue)

    if a.text != b.text:
        raise AssertionError("Tag %r text %r does not match %r." % (a.tag, a.text, b.text))

    if a.tail != b.tail:
        raise AssertionError("Tag %r tail %r does not match %r." % (a.tag, a.tail, b.tail))

    for achild, bchild in zip(a, b):
        assert_dom_equal(achild, bchild, exceptions)


def assert_canvas_equal(canvas, name, show_diff=True):
    test_file = os.path.join(failed_dir, "%s.svg" % name)
    reference_file = os.path.join(reference_dir, "%s.svg" % name)

    # Render multiple representations of the canvas for coverage.
    for module in ["toyplot.html", "toyplot.pdf", "toyplot.png", "toyplot.reportlab.pdf", "toyplot.reportlab.png"]:
        if module in sys.modules:
            stream = io.BytesIO()
            sys.modules[module].render(canvas, stream)

    # Render the canvas to svg for comparison against the reference.
    svg = io.BytesIO()
    toyplot.svg.render(canvas, svg)

    # Get rid of any past failures ...
    if os.path.exists(test_file):
        os.remove(test_file)

    # If there's no stored SVG reference for this canvas, create one.
    if not os.path.exists(reference_file):
        with open(reference_file, "wb") as stream:
            stream.write(svg.getvalue())
        raise AssertionError(
            "Created new reference file %s ... you should verify its contents before re-running the test." %
            reference_file)

    # Compare the SVG representation of the canvas to the SVG reference.
    svg_dom = xml.fromstring(svg.getvalue())
    reference_dom = xml.parse(reference_file).getroot()

    try:
        assert_dom_equal(
            svg_dom,
            reference_dom,
            exceptions={
                "{http://www.w3.org/2000/svg}clipPath": {
                    "id": {"ignore": True},
                    },
                "{http://www.w3.org/2000/svg}g": {
                    "clip-path": {"ignore": True},
                    "id": {"ignore": True},
                    "transform": {"type": "transform"},
                    "style": {"type": "style"},
                    },
                "{http://www.w3.org/2000/svg}linearGradient": {
                    "id": {"ignore": True},
                    },
                "{http://www.w3.org/2000/svg}line": {
                    "x1": {"type": "float"},
                    "x2": {"type": "float"},
                    "y1": {"type": "float"},
                    "y2": {"type": "float"},
                    "style": {"type": "style"},
                    },
                "{http://www.w3.org/2000/svg}linearGradient": {
                    "id": {"ignore": True},
                    "x1": {"type": "float"},
                    "x2": {"type": "float"},
                    "y1": {"type": "float"},
                    "y2": {"type": "float"},
                    },
                "{http://www.w3.org/2000/svg}path": {
                    "d": {"type": "path"},
                    },
                "{http://www.w3.org/2000/svg}polygon": {
                    "points": {"type": "points"},
                    },
                "{http://www.w3.org/2000/svg}rect": {
                    "x": {"type": "float"},
                    "y": {"type": "float"},
                    "width": {"type": "float"},
                    "height": {"type": "float"},
                    "style": {"type": "style"},
                    },
                "{http://www.w3.org/2000/svg}stop": {
                    "offset": {"type": "float"},
                    },
                "{http://www.w3.org/2000/svg}svg": {
                    "id": {"ignore": True},
                    },
                "{http://www.w3.org/2000/svg}text": {
                    "x": {"type": "float"},
                    "y": {"type": "float"},
                    },
                }
            )

    except AssertionError as e:
        if not os.path.exists(failed_dir):
            os.mkdir(failed_dir)
        with open(test_file, "wb") as stream:
            stream.write(svg.getvalue())
        raise AssertionError("%s\nTest output\n\t%s\ndoesn't match\n\t%s.\n" % (e, test_file, reference_file))


def read_png(fobj):
    if isinstance(fobj, six.string_types):
        reader = png.Reader(filename=fobj)
    else:
        reader = png.Reader(fobj)
    width, height, pixels, meta = reader.read()
    planes = 1 if meta["greyscale"] else 3
    if meta["alpha"]:
        planes += 1
    if meta["bitdepth"] == 1:
        image = numpy.resize(numpy.vstack(pixels), (height, width, planes))
    elif meta["bitdepth"] == 8:
        image = numpy.resize(numpy.vstack(map(numpy.uint8, pixels)), (height, width, planes))
    return image


def prufer_tree(sequence):
    """Use a Prufer sequence to generate a tree.
    """
    sequence = toyplot.require.integer_vector(sequence)
    n = len(sequence)
    if numpy.any(sequence < 0) or numpy.any(sequence >= n+2):
        raise ValueError("Sequence values must be in the range [0, %s)" % n+2) # pragma: no cover

    sources = []
    targets = []

    degree = numpy.ones(n+2, dtype="int64")
    for i in sequence:
        degree[i] += 1

    for i in sequence:
        for j in numpy.arange(n+2):
            if degree[j] == 1:
                sources.append(i)
                targets.append(j)
                degree[i] -= 1
                degree[j] -= 1
                break

    u, v = numpy.flatnonzero(degree == 1)
    sources.append(u)
    targets.append(v)

    return numpy.column_stack((sources, targets))


def barabasi_albert_graph(n=30, m=2, seed=1234):
    """Generate a graph using the preferential attachment model of Barabasi and Albert.
    """
    if m < 1 or m >= n:
        raise ValueError("m must be in the range [1, n].") # pragma: no cover

    generator = numpy.random.RandomState(seed=seed)

    sources = []
    targets = []

    new_source = m
    new_targets = numpy.arange(m)
    repeated_nodes = numpy.array([], dtype="int64")
    while new_source < n:
        for new_target in new_targets:
            sources.append(new_source)
            targets.append(new_target)
        repeated_nodes = numpy.append(repeated_nodes, new_targets)
        repeated_nodes = numpy.append(repeated_nodes, numpy.repeat(new_source, m))
        new_targets = generator.choice(repeated_nodes, size=m)
        new_source += 1

    return numpy.column_stack((sources, targets))
