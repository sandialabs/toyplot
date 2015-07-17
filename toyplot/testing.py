# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import collections
import difflib
import io
import json
import os
import numbers
import numpy.testing
import re
import toyplot.html
import toyplot.svg
import xml.etree.ElementTree as xml

root_dir = os.path.dirname(os.path.dirname(__file__))
failed_dir = os.path.join(root_dir, "features", "failed")
reference_dir = os.path.join(root_dir, "features", "reference")


def _assert_content_equal(content, test_file, reference_file):
    if os.path.exists(test_file):
        os.remove(test_file)
    if os.path.exists(reference_file):
        reference = open(reference_file, "rb").read()
        if content != reference:
            if not os.path.exists(failed_dir):
                os.mkdir(failed_dir)
            with open(test_file, "wb") as file:
                file.write(content)
            #raise AssertionError("Test output %s doesn't match %s." % (test_file, reference_file))
            raise AssertionError(
                "\n".join(
                    list(
                        difflib.context_diff(
                            content.split("\n"),
                            reference.split("\n"),
                            lineterm="",
                            fromfile="test",
                            tofile="reference"))))
    else:
        with open(reference_file, "wb") as file:
            file.write(content)
        raise AssertionError(
            "Created new reference file %s.  You should verify its contents before re-running the test." %
            (reference_file))


def _assert_string_equal(content, test_file, reference_file, encoding="utf-8"):
    if os.path.exists(test_file):
        os.remove(test_file)
    if os.path.exists(reference_file):
        reference = toyplot.compatibility.unicode_type(
            open(reference_file, "rb").read(), encoding=encoding)
        if content != reference:
            if not os.path.exists(failed_dir):
                os.mkdir(failed_dir)
            with open(test_file, "wb") as file:
                file.write(content.encode(encoding))
            raise AssertionError(
                "Test output %s doesn't match %s." %
                (test_file, reference_file))
    else:
        with open(reference_file, "wb") as file:
            file.write(content.encode(encoding))
        raise AssertionError(
            "Created new reference file %s.  You should verify its contents before re-running the test." %
            (reference_file))


def _json_comparison_string(o):
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
        return "[" + ",".join([_json_comparison_string(i) for i in o]) + "]"
    if isinstance(o, collections.Mapping):
        return "{" + ",".join(["\"" + key + "\":" + _json_comparison_string(value)
                               for key, value in o.items()]) + "}"
    raise Exception("Unexpected value: %s" % o)


def _xml_comparison_string(element):
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
            text = str(_json_comparison_string(json.loads(element.text)))
        buffer.write(u">%s\n" % text)
        for child in list(element):
            write_element(child, buffer, indent + "  ")
        buffer.write(u"%s</%s>\n" % (indent, element.tag))

    buffer = io.StringIO()
    write_element(element, buffer, indent="")
    return buffer.getvalue()


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
    _assert_content_equal(html, test_file, reference_file)


def assert_latex_equal(latex, name):
    """Raise an exception if LaTeX content doesn't match a reference.

    Parameters
    ----------
    latex: string, required
      The LaTeX content to be compared.
    name: string, required
      Unique identifier of the reference file to use as a comparison.
      The reference file will be located at toyplot/features/reference/<name>.tex
    """

    test_file = os.path.join(failed_dir, "%s.tex" % name)
    reference_file = os.path.join(reference_dir, "%s.tex" % name)
    _assert_string_equal(latex, test_file, reference_file)


def assert_canvas_equal(canvas, name):
    test_file = os.path.join(failed_dir, "%s.svg" % name)
    reference_file = os.path.join(reference_dir, "%s.svg" % name)

    # Render multiple representations of the canvas for coverage ...
    html = io.BytesIO()
    toyplot.html.render(canvas, html)

    svg = io.BytesIO()
    toyplot.svg.render(canvas, svg)

    if hasattr(toyplot, "eps"):
        eps = io.BytesIO()
        toyplot.eps.render(canvas, eps)

    if hasattr(toyplot, "pdf"):
        pdf = io.BytesIO()
        toyplot.pdf.render(canvas, pdf)

    if hasattr(toyplot, "png"):
        png = io.BytesIO()
        toyplot.png.render(canvas, png)

    # Get rid of any past failures ...
#  if os.path.exists("tests/diffs/%s.svg" % name):
#    os.remove("tests/diffs/%s.svg" % name)
#  if os.path.exists("tests/diffs/%s.reference.svg" % name):
#    os.remove("tests/diffs/%s.reference.svg" % name)
    if os.path.exists(test_file):
        os.remove(test_file)

    # If there's no stored SVG reference for this canvas, create one ...
    if not os.path.exists(reference_file):
        with open(reference_file, "wb") as file:
            file.write(svg.getvalue())
        raise AssertionError(
            "Created new reference file %s ... you should verify its contents before re-running the test." %
            reference_file)

    # Compare the SVG representation of the canvas to the SVG reference ...
    svg_dom = xml.fromstring(svg.getvalue())
    reference_dom = xml.parse(reference_file).getroot()

    svg_string = _xml_comparison_string(svg_dom)
    reference_string = _xml_comparison_string(reference_dom)

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
        #    if not os.path.exists("tests/diffs"):
        #      os.mkdir("tests/diffs")
        #    with open("tests/diffs/%s.svg" % name, "wb") as file:
        #      file.write(svg_string)
        #    with open("tests/diffs/%s.reference.svg" % name, "wb") as file:
        #      file.write(reference_string)
        if not os.path.exists(failed_dir):
            os.mkdir(failed_dir)
        with open(test_file, "wb") as file:
            file.write(svg.getvalue())
        raise AssertionError(
            "Test output %s doesn't match %s:\n%s" %
            (test_file, reference_file, e))
