# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import StringIO
import collections
import nose.tools
import numpy
import os
import sys
import tempfile
import xml.etree.ElementTree as xml

import toyplot
import toyplot.color
import toyplot.color.css
import toyplot.html
import toyplot.svg

try:
  import toyplot.eps
except:
  pass

try:
  import toyplot.mp4
except:
  pass

try:
  import toyplot.pdf
except:
  pass

try:
  import toyplot.png
except:
  pass



#########################################################################################################################
# Test fixtures.

def assert_color_equal(a, b):
  numpy.testing.assert_array_almost_equal((a["r"], a["g"], a["b"], a["a"]), b)

def assert_colors_equal(a, b):
  for j, k in zip(a, b):
    assert_color_equal(j, k)

def assert_masked_array(a, dtype, b, mask):
  nose.tools.assert_is_instance(a, numpy.ma.MaskedArray)
  nose.tools.assert_equal(a.dtype, dtype)
  numpy.testing.assert_array_equal(a, b)
  numpy.testing.assert_array_equal(a.mask, mask)

def assert_dom_equal(a, b):
  if a.tag.split("}")[-1] != b.tag.split("}")[-1]:
    raise AssertionError("Tag %s != %s" % (a.tag, b.tag))
  if a.text != b.text:
    raise AssertionError("Text %s != %s" % (a.text, b.text))
  if a.tail != b.tail:
    raise AssertionError("Tail %s != %s" % (a.tail, b.tail))
  for key in a.attrib:
    if key in ["xmlns"]:
      continue
    if key not in b.attrib:
      raise AssertionError("Missing attribute %s" % (key))
  for key in b.attrib:
    if key not in a.attrib:
      raise AssertionError("Extra attribute %s" % (key))
  for key in a.attrib:
    if key in ["xmlns", "id", "clip-path"]:
      continue
    if a.attrib[key] != b.attrib[key]:
      raise AssertionError("Attribute %s value mismatch" % (key))

  if len(list(a)) != len(list(b)):
    raise AssertionError("Number of children doesn't match")

  for child_a, child_b in zip(list(a), list(b)):
    assert_dom_equal(child_a, child_b)

def assert_canvas_matches(canvas, name):
  # Render every representation of the canvas for coverage ...
  html = StringIO.StringIO()
  toyplot.html.render(canvas, html)

  svg = StringIO.StringIO()
  toyplot.svg.render(canvas, svg)

  if hasattr(toyplot, "eps"):
    eps = StringIO.StringIO()
    toyplot.eps.render(canvas, eps)

  if hasattr(toyplot, "pdf"):
    pdf = StringIO.StringIO()
    toyplot.pdf.render(canvas, pdf)

  if hasattr(toyplot, "png"):
    png = StringIO.StringIO()
    toyplot.png.render(canvas, png)

  # Get rid of any past failures ...
  if os.path.exists("tests/failed/%s.svg" % name):
    os.remove("tests/failed/%s.svg" % name)

  # If there's no stored SVG reference for this canvas, create one ...
  if not os.path.exists("tests/reference/%s.svg" % name):
    with open("tests/reference/%s.svg" % name, "w") as file:
      file.write(svg.getvalue())
    raise AssertionError("Created new reference file tests/reference/%s.svg ... you should verify its contents before re-running the test." % name)

  # Compare the SVG representation of the canvas to the SVG reference ...
  svg_dom = xml.fromstring(svg.getvalue())
  reference_dom = xml.parse("tests/reference/%s.svg" % name).getroot()

  try:
    assert_dom_equal(svg_dom, reference_dom)
  except Exception as e:
    if not os.path.exists("tests/failed"):
      os.mkdir("tests/failed")
    with open("tests/failed/%s.svg" % name, "w") as file:
      file.write(svg.getvalue())
    raise AssertionError("Test output tests/failed/%s.svg doesn't match tests/reference/%s.svg (%s)" % (name, name, e))

def assert_html_matches(html, name):
  reference_file = "tests/reference/%s.html" % name
  test_file = "tests/failed/%s.html" % name
  if os.path.exists(test_file):
    os.remove(test_file)
  if os.path.exists(reference_file):
    reference_html = open(reference_file).read()
    if html != reference_html:
      if not os.path.exists("tests/failed"):
        os.mkdir("tests/failed")
      with open(test_file, "w") as file:
        file.write(html)
      raise AssertionError("Test output %s doesn't match %s." % (test_file, reference_file))
  else:
    with open(reference_file, "w") as file:
      file.write(html)
    raise AssertionError("Created new reference file %s.  You should verify its contents before re-running the test." % (reference_file))

#########################################################################################################################
# toyplot

def test_require_scalar():
  nose.tools.assert_equal(toyplot._require_scalar(1), 1)
  nose.tools.assert_equal(toyplot._require_scalar(1.2), 1.2)
  with nose.tools.assert_raises(ValueError):
    nose.tools.assert_equal(toyplot._require_scalar("foo"), "foo")

def test_require_scalar_array():
  assert_masked_array(toyplot._require_scalar_array(1), "float64", [1], [False])
  assert_masked_array(toyplot._require_scalar_array(1.1), "float64", [1.1], [False])
  assert_masked_array(toyplot._require_scalar_array("1.2"), "float64", [1.2], [False])
  assert_masked_array(toyplot._require_scalar_array([1, 2, 3]), "float64", [1, 2, 3], [False, False, False])
  assert_masked_array(toyplot._require_scalar_array(["1", "2", 3]), "float64", [1, 2, 3], [False, False, False])
  assert_masked_array(toyplot._require_scalar_array([[1, 2], [3, 4]]), "float64", [[1, 2], [3, 4]], [[False, False], [False, False]])
  assert_masked_array(toyplot._require_scalar_array(numpy.array([1, 2, 3])), "float64", [1, 2, 3], [False, False, False])
  assert_masked_array(toyplot._require_scalar_array(numpy.ma.array([1, 2, 3], mask=[False, True, False])), "float64", [1, 2, 3], [False, True, False])
  assert_masked_array(toyplot._require_scalar_array(numpy.array([1, numpy.nan, 3])), "float64", [1, numpy.nan, 3], [False, True, False])
  assert_masked_array(toyplot._require_scalar_array(numpy.ma.array([1, numpy.nan, 3], mask=[False, False, True])), "float64", [1, numpy.nan, 3], [False, True, True])
  with nose.tools.assert_raises(ValueError):
    toyplot._require_scalar_array("foo")
  with nose.tools.assert_raises(ValueError):
    toyplot._require_scalar_array(["1", "foo"])

def test_require_scalar_vector():
  numpy.testing.assert_array_equal(toyplot._require_scalar_vector(1), [1])
  numpy.testing.assert_array_equal(toyplot._require_scalar_vector(1, length=3), [1, 1, 1])
  numpy.testing.assert_array_equal(toyplot._require_scalar_vector([1, 2, 3]), [1, 2, 3])
  numpy.testing.assert_array_equal(toyplot._require_scalar_vector([1, 2, 3], length=3), [1, 2, 3])
  with nose.tools.assert_raises(ValueError):
    toyplot._require_scalar_vector([1, 2, 3], length=2)
  with nose.tools.assert_raises(ValueError):
    toyplot._require_scalar_vector([[1, 2], [3, 4]])

def test_require_scalar_matrix():
  with nose.tools.assert_raises(ValueError):
    toyplot._require_scalar_matrix(1)
  with nose.tools.assert_raises(ValueError):
    toyplot._require_scalar_matrix([1, 2, 3])
  numpy.testing.assert_array_equal(toyplot._require_scalar_matrix([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
  with nose.tools.assert_raises(ValueError):
    toyplot._require_scalar_matrix([[1, 2], [3, 4]], rows=3)
  with nose.tools.assert_raises(ValueError):
    toyplot._require_scalar_matrix([[1, 2], [3, 4]], columns=3)
  with nose.tools.assert_raises(ValueError):
    toyplot._require_scalar_matrix([[[1, 2], [3, 4]]])

def test_require_string():
  nose.tools.assert_equal(toyplot._require_string("foo"), "foo")
  nose.tools.assert_equal(toyplot._require_string(u"foo"), u"foo")
  with nose.tools.assert_raises(ValueError):
    nose.tools.assert_equal(toyplot._require_string(None), None)
  with nose.tools.assert_raises(ValueError):
    nose.tools.assert_equal(toyplot._require_string(1), 1)

def test_require_optional_string():
  nose.tools.assert_equal(toyplot._require_optional_string("foo"), "foo")
  nose.tools.assert_equal(toyplot._require_optional_string(u"foo"), u"foo")
  nose.tools.assert_equal(toyplot._require_optional_string(None), None)
  with nose.tools.assert_raises(ValueError):
    nose.tools.assert_equal(toyplot._require_optional_string(1), 1)

def test_require_marker_array():
  numpy.testing.assert_array_equal(toyplot._require_marker_array("foo"), ["foo"])
  numpy.testing.assert_array_equal(toyplot._require_marker_array(["foo", "bar"]), ["foo", "bar"])
  numpy.testing.assert_array_equal(toyplot._require_marker_array([1, 2]), [1, 2])
  numpy.testing.assert_array_equal(toyplot._require_marker_array([1, 2, "foo"]), [1, 2, "foo"])
  with nose.tools.assert_raises(ValueError):
    toyplot._require_marker_array(["foo", "bar"], 3)

def test_require_style():
  nose.tools.assert_equal(toyplot._require_style({}), {})
  nose.tools.assert_equal(toyplot._require_style({"stroke":"black"}), {"stroke":"black"})
  with nose.tools.assert_raises(ValueError):
    nose.tools.assert_equal(toyplot._require_style(None), None)
  with nose.tools.assert_raises(ValueError):
    nose.tools.assert_equal(toyplot._require_style(""), "")

def test_require_optional_id():
  nose.tools.assert_equal(toyplot._require_optional_id("foo"), "foo")
  nose.tools.assert_equal(toyplot._require_optional_id(u"foo"), u"foo")
  nose.tools.assert_equal(toyplot._require_optional_id(None), None)
  with nose.tools.assert_raises(ValueError):
    nose.tools.assert_equal(toyplot._require_optional_id(1), 1)

def test_broadcast_scalar():
  numpy.testing.assert_equal(toyplot._broadcast_scalar(1, 3), [1,1,1])
  numpy.testing.assert_equal(toyplot._broadcast_scalar(1, (3, 3)), [[1,1,1],[1,1,1],[1,1,1]])
  numpy.testing.assert_equal(toyplot._broadcast_scalar([1,2,3], 3), [1,2,3])
  numpy.testing.assert_equal(toyplot._broadcast_scalar([1,2,3], (3, 3)), [[1,2,3],[1,2,3],[1,2,3]])
  numpy.testing.assert_equal(toyplot._broadcast_scalar([[1,2,3],[4, 5, 6],[7, 8, 9]], (3, 3)), [[1,2,3],[4,5,6],[7,8,9]])
  numpy.testing.assert_equal(toyplot._broadcast_scalar([1,2,3], (3, 1)), [[1],[2],[3]])

def test_broadcast_string():
  numpy.testing.assert_equal(toyplot._broadcast_string("1", 3), ["1","1","1"])
  numpy.testing.assert_equal(toyplot._broadcast_string("1", (3, 3)), [["1","1","1"],["1","1","1"],["1","1","1"]])
  numpy.testing.assert_equal(toyplot._broadcast_string(["1","2","3"], 3), ["1","2","3"])
  numpy.testing.assert_equal(toyplot._broadcast_string(["1","2","3"], (3, 3)), [["1","2","3"],["1","2","3"],["1","2","3"]])
  numpy.testing.assert_equal(toyplot._broadcast_string([["1","2","3"],["4","5","6"],["7","8","9"]], (3, 3)), [["1","2","3"],["4","5","6"],["7","8","9"]])
  numpy.testing.assert_equal(toyplot._broadcast_string(["1","2","3"], (3, 1)), [["1"],["2"],["3"]])

def test_axes():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  assert_canvas_matches(canvas, "axes")

def test_axes_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.show=False
  nose.tools.assert_equal(axes.show, False)
  assert_canvas_matches(canvas, "axes-show")

def test_axes_coordinates_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.coordinates.show=False
  nose.tools.assert_equal(axes.coordinates.show, False)
  assert_canvas_matches(canvas, "axes-coordinates-show")

def test_axes_coordinates_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.coordinates.style={"stroke":"red", "fill":"ivory"}
  nose.tools.assert_equal(axes.coordinates.style["stroke"], "red")
  assert_canvas_matches(canvas, "axes-coordinates-style")

def test_axes_coordinates_label():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.coordinates.label.style={"fill":"red"}
  nose.tools.assert_equal(axes.coordinates.label.style["fill"], "red")
  assert_canvas_matches(canvas, "axes-coordinates-label")

def test_axes_label():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.label.text="Howdy!"
  nose.tools.assert_equal(axes.label.text, "Howdy!")
  axes.label.style={"fill":"red"}
  nose.tools.assert_equal(axes.label.style["fill"], "red")
  assert_canvas_matches(canvas, "axes-label")

def test_axes_x_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.show=False
  nose.tools.assert_equal(axes.x.show, False)
  assert_canvas_matches(canvas, "axes-x-show")

def test_axes_x_scale():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.scale="log"
  nose.tools.assert_equal(axes.x.scale, ("log", 10))
  assert_canvas_matches(canvas, "axes-x-scale")

def test_axes_x_spine_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.spine.show=False
  nose.tools.assert_equal(axes.x.spine.show, False)
  assert_canvas_matches(canvas, "axes-x-spine-show")

def test_axes_x_spine_position():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.spine.position=0
  nose.tools.assert_equal(axes.x.spine.position, 0)
  assert_canvas_matches(canvas, "axes-x-spine-position")

def test_axes_x_spine_position_high():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.spine.position="high"
  nose.tools.assert_equal(axes.x.spine.position, "high")
  assert_canvas_matches(canvas, "axes-x-spine-position-high")

def test_axes_x_spine_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.spine.style={"stroke":"red"}
  nose.tools.assert_equal(axes.x.spine.style["stroke"], "red")
  assert_canvas_matches(canvas, "axes-x-spine-style")

def test_axes_x_ticks_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.show=True
  nose.tools.assert_equal(axes.x.ticks.show, True)
  assert_canvas_matches(canvas, "axes-x-ticks-show")

def test_axes_x_ticks_length():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.show=True
  axes.x.ticks.length=20
  nose.tools.assert_equal(axes.x.ticks.length, 20)
  assert_canvas_matches(canvas, "axes-x-ticks-length")

def test_axes_x_ticks_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.show=True
  axes.x.ticks.style={"stroke":"red"}
  nose.tools.assert_equal(axes.x.ticks.style["stroke"], "red")
  assert_canvas_matches(canvas, "axes-x-ticks-style")

def test_axes_x_ticks_locator():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.show=True
  locator=toyplot.BasicTickLocator(count=11)
  axes.x.ticks.locator=locator
  nose.tools.assert_is(axes.x.ticks.locator, locator)
  assert_canvas_matches(canvas, "axes-x-ticks-locator")

def test_axes_x_ticks_tick_index_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.show=True
  axes.x.ticks.tick(index=0).style={"stroke":"red"}
  nose.tools.assert_equal(axes.x.ticks.tick(index=0).style["stroke"], "red")
  assert_canvas_matches(canvas, "axes-x-ticks-tick-index-style")

def test_axes_x_ticks_tick_value_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.show=True
  axes.x.ticks.tick(value=0).style={"stroke":"red"}
  nose.tools.assert_equal(axes.x.ticks.tick(value=0).style["stroke"], "red")
  assert_canvas_matches(canvas, "axes-x-ticks-tick-value-style")

def test_axes_x_ticks_labels_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.labels.show=False
  nose.tools.assert_equal(axes.x.ticks.labels.show, False)
  assert_canvas_matches(canvas, "axes-x-ticks-labels-show")

def test_axes_x_ticks_labels_angle():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.labels.angle=-45
  nose.tools.assert_equal(axes.x.ticks.labels.angle, -45)
  axes.x.ticks.labels.style={"text-anchor":"end"}
  nose.tools.assert_equal(axes.x.ticks.labels.style["text-anchor"], "end")
  assert_canvas_matches(canvas, "axes-x-ticks-labels-angle")

def test_axes_x_ticks_labels_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.labels.style={"fill":"red"}
  nose.tools.assert_equal(axes.x.ticks.labels.style["fill"], "red")
  assert_canvas_matches(canvas, "axes-x-ticks-labels-style")

def test_axes_x_ticks_labels_label_index_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.labels.label(index=0).style={"fill":"red"}
  nose.tools.assert_equal(axes.x.ticks.labels.label(index=0).style["fill"], "red")
  assert_canvas_matches(canvas, "axes-x-ticks-labels-label-index-style")

def test_axes_x_ticks_labels_label_value_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.labels.label(value=0).style={"fill":"red"}
  nose.tools.assert_equal(axes.x.ticks.labels.label(value=0).style["fill"], "red")
  assert_canvas_matches(canvas, "axes-x-ticks-labels-label-value-style")

def test_axes_x_label():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.label.text="Howdy!"
  nose.tools.assert_equal(axes.x.label.text, "Howdy!")
  axes.x.label.style={"fill":"red"}
  nose.tools.assert_equal(axes.x.label.style["fill"], "red")
  assert_canvas_matches(canvas, "axes-x-label")

def test_axes_x_domain():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.domain.min=0
  nose.tools.assert_equal(axes.x.domain.min, 0)
  axes.x.domain.max=1
  nose.tools.assert_equal(axes.x.domain.max, 1)
  assert_canvas_matches(canvas, "axes-x-domain")

def test_axes_y_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.show=False
  assert_canvas_matches(canvas, "axes-y-show")

def test_axes_y_scale():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.scale="log"
  assert_canvas_matches(canvas, "axes-y-scale")

def test_axes_y_spine_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.spine.show=False
  assert_canvas_matches(canvas, "axes-y-spine-show")

def test_axes_y_spine_position():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.spine.position=0
  assert_canvas_matches(canvas, "axes-y-spine-position")

def test_axes_y_spine_position_high():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.spine.position="high"
  assert_canvas_matches(canvas, "axes-y-spine-position-high")

def test_axes_y_spine_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.spine.style={"stroke":"red"}
  assert_canvas_matches(canvas, "axes-y-spine-style")

def test_axes_y_ticks_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.show=True
  assert_canvas_matches(canvas, "axes-y-ticks-show")

def test_axes_y_ticks_length():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.show=True
  axes.y.ticks.length=20
  assert_canvas_matches(canvas, "axes-y-ticks-length")

def test_axes_y_ticks_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.show=True
  axes.y.ticks.style={"stroke":"red"}
  assert_canvas_matches(canvas, "axes-y-ticks-style")

def test_axes_y_ticks_locator():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.show=True
  axes.y.ticks.locator=toyplot.BasicTickLocator(count=11)
  assert_canvas_matches(canvas, "axes-y-ticks-locator")

def test_axes_y_ticks_tick_index_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.show=True
  axes.y.ticks.tick(index=0).style={"stroke":"red"}
  assert_canvas_matches(canvas, "axes-y-ticks-tick-index-style")

def test_axes_y_ticks_tick_value_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.show=True
  axes.y.ticks.tick(value=0).style={"stroke":"red"}
  assert_canvas_matches(canvas, "axes-y-ticks-tick-value-style")

def test_axes_y_ticks_labels_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.labels.show=False
  assert_canvas_matches(canvas, "axes-y-ticks-labels-show")

def test_axes_y_ticks_labels_angle():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.labels.angle=-45
  axes.y.ticks.labels.style={"text-anchor":"end"}
  assert_canvas_matches(canvas, "axes-y-ticks-labels-angle")

def test_axes_y_ticks_labels_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.labels.style={"fill":"red"}
  assert_canvas_matches(canvas, "axes-y-ticks-labels-style")

def test_axes_y_ticks_labels_label_index_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.labels.label(index=0).style={"fill":"red"}
  assert_canvas_matches(canvas, "axes-y-ticks-labels-label-index-style")

def test_axes_y_ticks_labels_label_value_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.ticks.labels.label(value=0).style={"fill":"red"}
  assert_canvas_matches(canvas, "axes-y-ticks-labels-label-value-style")

def test_axes_y_label():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.label.text="Howdy!"
  axes.y.label.style={"fill":"red"}
  assert_canvas_matches(canvas, "axes-y-label")

def test_axes_y_domain():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.y.domain.min=0
  axes.y.domain.max=1
  assert_canvas_matches(canvas, "axes-y-domain")

def test_axes_tick_titles():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.x.ticks.locator=toyplot.ExplicitTickLocator(locations=[-0.5, 0, 0.5], titles=["Foo", "Bar", "Baz"])
  axes.y.ticks.locator=toyplot.ExplicitTickLocator(locations=[-0.5, 0, 0.5], titles=["Red", "Green", "Blue"])
  assert_canvas_matches(canvas, "axes-tick-titles")

def test_axes_colorbar():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar()
  assert_canvas_matches(canvas, "axes-colorbar")

def test_axes_colorbar_data():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(numpy.arange(100), palette=toyplot.color.brewer("BlueYellowRed"))
  assert_canvas_matches(canvas, "axes-colorbar-ticks-data")

def test_axes_colorbar_domain():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.domain.min=0
  nose.tools.assert_equal(colorbar.domain.min, 0)
  colorbar.domain.max=1
  nose.tools.assert_equal(colorbar.domain.max, 1)
  assert_canvas_matches(canvas, "axes-colorbar-domain")

def test_axes_colorbar_label():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.label.text="Colorbar Label"
  nose.tools.assert_equal(colorbar.label.text, "Colorbar Label")
  colorbar.label.style={"fill":"red"}
  nose.tools.assert_equal(colorbar.label.style["fill"], "red")
  assert_canvas_matches(canvas, "axes-colorbar-label")

def test_axes_colorbar_ticks_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.show=True
  nose.tools.assert_equal(colorbar.ticks.show, True)
  assert_canvas_matches(canvas, "axes-colorbar-ticks-show")

def test_axes_colorbar_ticks_length():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.show=True
  colorbar.ticks.length=20
  nose.tools.assert_equal(colorbar.ticks.length, 20)
  assert_canvas_matches(canvas, "axes-colorbar-ticks-length")

def test_axes_colorbar_ticks_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.show=True
  colorbar.ticks.style={"stroke":"red"}
  nose.tools.assert_equal(colorbar.ticks.style["stroke"], "red")
  assert_canvas_matches(canvas, "axes-colorbar-ticks-style")

def test_axes_colorbar_ticks_locator():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.show=True
  locator=toyplot.ExplicitTickLocator(locations=[-0.5, 0.0, 0.5], titles=["blue", "yellow", "red"])
  colorbar.ticks.locator=locator
  nose.tools.assert_is(colorbar.ticks.locator, locator)
  assert_canvas_matches(canvas, "axes-colorbar-ticks-locator")

def test_axes_colorbar_ticks_tick_index_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.show=True
  colorbar.ticks.tick(index=1).style={"stroke":"red"}
  nose.tools.assert_equal(colorbar.ticks.tick(index=1).style["stroke"], "red")
  assert_canvas_matches(canvas, "axes-colorbar-ticks-tick-index-style")

def test_axes_colorbar_ticks_tick_value_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.show=True
  colorbar.ticks.tick(value=0.5).style={"stroke":"red"}
  nose.tools.assert_equal(colorbar.ticks.tick(value=0.5).style["stroke"], "red")
  assert_canvas_matches(canvas, "axes-colorbar-ticks-tick-value-style")

def test_axes_colorbar_ticks_labels_show():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.labels.show=False
  nose.tools.assert_equal(colorbar.ticks.labels.show, False)
  assert_canvas_matches(canvas, "axes-colorbar-ticks-labels-show")

def test_axes_colorbar_ticks_labels_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.labels.style={"fill":"red"}
  nose.tools.assert_equal(colorbar.ticks.labels.style["fill"], "red")
  assert_canvas_matches(canvas, "axes-colorbar-ticks-labels-style")

def test_axes_colorbar_ticks_labels_label_index_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.labels.label(index=1).style={"fill":"red"}
  nose.tools.assert_equal(colorbar.ticks.labels.label(index=1).style["fill"], "red")
  assert_canvas_matches(canvas, "axes-colorbar-ticks-labels-label-index-style")

def test_axes_colorbar_ticks_labels_label_value_style():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Axes Label", xlabel="X Label", ylabel="Y Label")
  colorbar = axes.colorbar(palette=toyplot.color.brewer("BlueYellowRed"))
  colorbar.ticks.labels.label(value=0.5).style={"fill":"red"}
  nose.tools.assert_equal(colorbar.ticks.labels.label(value=0.5).style["fill"], "red")
  assert_canvas_matches(canvas, "axes-colorbar-ticks-labels-label-value-style")

def test_axes_palette():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  for i in range(10):
    axes.plot(numpy.arange(2), numpy.repeat(i, 2))
  assert_canvas_matches(canvas, "axes-palette")

def test_axes_log_scale_negative():
  x = numpy.linspace(-100, -1e-5, 1000)
  y = numpy.sin(x)
  canvas = toyplot.Canvas(800, 200)
  axes = canvas.axes(xscale="log")
  axes.plot(x, y)
  assert_canvas_matches(canvas, "axes-log-scale-negative")

def test_axes_log_scale_negative_zero():
  x = numpy.linspace(-100, 0, 1000)
  y = numpy.sin(x)
  canvas = toyplot.Canvas(800, 200)
  axes = canvas.axes(xscale="log")
  axes.plot(x, y)
  assert_canvas_matches(canvas, "axes-log-scale-negative-zero")

def test_axes_log_scale_negative_small_positive():
  x = numpy.linspace(-100, 0.5, 1000)
  y = numpy.sin(x)
  canvas = toyplot.Canvas(800, 200)
  axes = canvas.axes(xscale="log")
  axes.plot(x, y)
  assert_canvas_matches(canvas, "axes-log-scale-negative-small-positive")

def test_axes_log_scale_positive_small_negative():
  x = numpy.linspace(-0.5, 100, 1000)
  y = numpy.sin(x)
  canvas = toyplot.Canvas(800, 200)
  axes = canvas.axes(xscale="log")
  axes.plot(x, y)
  assert_canvas_matches(canvas, "axes-log-scale-positive-small-negative")

def test_axes_log_scale_positive_zero():
  x = numpy.linspace(0, 100, 1000)
  y = numpy.sin(x)
  canvas = toyplot.Canvas(800, 200)
  axes = canvas.axes(xscale="log")
  axes.plot(x, y)
  assert_canvas_matches(canvas, "axes-log-scale-positive-zero")

def test_axes_log_scale_positive():
  x = numpy.linspace(1e-5, 100, 1000)
  y = numpy.sin(x)
  canvas = toyplot.Canvas(800, 200)
  axes = canvas.axes(xscale="log")
  axes.plot(x, y)
  assert_canvas_matches(canvas, "axes-log-scale-positive")

def test_axes_log_scale_negative_positive():
  x = numpy.linspace(-100, 100, 1000)
  y = numpy.sin(x)
  canvas = toyplot.Canvas(800, 200)
  axes = canvas.axes(xscale="log")
  axes.plot(x, y)
  assert_canvas_matches(canvas, "axes-log-scale-negative-positive")

def test_axes_log_log_positive():
  x = numpy.linspace(1, 100, 101)
  canvas = toyplot.Canvas(1000, 1000)
  axes = canvas.axes(grid=(2, 2, 0, 0), xscale="linear", yscale="linear")
  axes.plot(x, x, marker="o")
  axes = canvas.axes(grid=(2, 2, 0, 1), xscale="linear", yscale="log")
  axes.plot(x, x, marker="o")
  axes = canvas.axes(grid=(2, 2, 1, 0), xscale="log", yscale="linear")
  axes.plot(x, x, marker="o")
  axes = canvas.axes(grid=(2, 2, 1, 1), xscale="log", yscale="log")
  axes.plot(x, x, marker="o")
  assert_canvas_matches(canvas, "axes-log-log-positive")

def test_axes_log_log_negative_positive():
  x = numpy.linspace(-100, 100, 101)
  canvas = toyplot.Canvas(1000, 1000)
  axes = canvas.axes(grid=(2, 2, 0, 0), xscale="linear", yscale="linear")
  axes.plot(x, x, marker="o")
  axes = canvas.axes(grid=(2, 2, 0, 1), xscale="linear", yscale="log")
  axes.plot(x, x, marker="o")
  axes = canvas.axes(grid=(2, 2, 1, 0), xscale="log", yscale="linear")
  axes.plot(x, x, marker="o")
  axes = canvas.axes(grid=(2, 2, 1, 1), xscale="log", yscale="log")
  axes.plot(x, x, marker="o")
  assert_canvas_matches(canvas, "axes-log-log-negative-positive")

def test_axes_log2():
  x = numpy.linspace(1, 100)
  canvas = toyplot.Canvas()
  axes = canvas.axes(xscale="log2", yscale="log2")
  axes.plot(x, x, marker="o")
  assert_canvas_matches(canvas, "axes-log2-log2")

def test_axes_log10():
  x = numpy.linspace(1, 100)
  canvas = toyplot.Canvas()
  axes = canvas.axes(xscale="log10", yscale="log10")
  axes.plot(x, x, marker="o")
  assert_canvas_matches(canvas, "axes-log10-log10")

def test_axes_palettes():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(numpy.sin(numpy.linspace(0, 2 * numpy.pi, 100)), style={"fill-opacity":0.5})
  axes.plot(numpy.sin(numpy.linspace(0, 2 * numpy.pi, 100)), marker="o")
  axes.fill(numpy.cos(numpy.linspace(0, 2 * numpy.pi, 100)), style={"fill-opacity":0.5})
  axes.plot(numpy.cos(numpy.linspace(0, 2 * numpy.pi, 100)), marker="o")
  axes.fill((numpy.linspace(0, 1, 100)), style={"fill-opacity":0.5})
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
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.bars(series)
  assert_canvas_matches(canvas, "axes-bars-n-magnitudes")

def test_axes_bars_n_magnitudes_along_y():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.bars(series, along="y")
  assert_canvas_matches(canvas, "axes-bars-n-magnitudes-along-y")

def test_axes_bars_n_magnitudes_centers():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  x = numpy.linspace(0, 1, len(observations))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

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
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.bars(x1, x2, series)
  assert_canvas_matches(canvas, "axes-bars-n-magnitudes-edges")

def test_axes_bars_n_magnitudes_symmetric():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.bars(series, baseline="symmetric")
  assert_canvas_matches(canvas, "axes-bars-n-magnitudes-symmetric")

def test_axes_bars_n_magnitudes_wiggle():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.bars(series, baseline="wiggle")
  assert_canvas_matches(canvas, "axes-bars-n-magnitudes-wiggle")

def test_axes_bars_n_magnitudes_titles():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

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
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.bars(series, baseline=None)
  assert_canvas_matches(canvas, "axes-bars-n-boundaries")

def test_axes_bars_n_boundaries_along_y():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.bars(series, along="y", baseline=None)
  assert_canvas_matches(canvas, "axes-bars-n-boundaries-along-y")

def test_axes_bars_n_boundaries_centers():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  x = numpy.linspace(0, 1, len(observations))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

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
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.bars(x1, x2, series, baseline=None)
  assert_canvas_matches(canvas, "axes-bars-n-boundaries-edges")

def test_axes_bars_n_boundaries_titles():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.percentile(observations, 25, axis=1), numpy.percentile(observations, 50, axis=1), numpy.percentile(observations, 75, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.bars(series, title=["1st quartile", "2nd quartile", "3rd quartile", "4th quartile"], baseline=None)
  assert_canvas_matches(canvas, "axes-bars-n-boundaries-titles")

def test_fill_one_boundary():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  y = numpy.mean(observations, axis=1)

  canvas, axes, mark = toyplot.fill(y)
  assert_canvas_matches(canvas, "fill-one-boundary")

def test_axes_fill_one_boundary():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  y = numpy.mean(observations, axis=1)

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(y)
  assert_canvas_matches(canvas, "axes-fill-one-boundary")

def test_axes_fill_two_boundaries():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  y1 = numpy.mean(observations, axis=1)
  y2 = numpy.max(observations, axis=1)

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(y1, y2)
  assert_canvas_matches(canvas, "axes-fill-two-boundaries")

def test_axes_fill_two_boundaries_x():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  x = numpy.linspace(0, 1, len(observations))
  y1 = numpy.mean(observations, axis=1)
  y2 = numpy.max(observations, axis=1)

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(x, y1, y2)
  assert_canvas_matches(canvas, "axes-fill-two-boundaries-x")

def test_axes_fill_n_boundaries():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(series)
  assert_canvas_matches(canvas, "axes-fill-n-boundaries")

def test_axes_fill_n_boundaries_x():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  x = numpy.linspace(0, 1, len(observations))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(x, series)
  assert_canvas_matches(canvas, "axes-fill-n-boundaries-x")

def test_axes_fill_n_boundaries_along_y():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(series, along="y")
  assert_canvas_matches(canvas, "axes-fill-n-boundaries-along-y")

def test_axes_fill_n_boundaries_titles():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.percentile(observations, 25, axis=1), numpy.percentile(observations, 50, axis=1), numpy.percentile(observations, 75, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(series, title=["1st quartile", "2nd quartile", "3rd quartile", "4th quartile"])
  assert_canvas_matches(canvas, "axes-fill-n-boundaries-titles")

def test_axes_fill_one_magnitude():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  height = numpy.mean(observations, axis=1)

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(height, baseline="stacked")
  assert_canvas_matches(canvas, "axes-fill-one-magnitude")

def test_axes_fill_one_magnitude_x():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  x = numpy.linspace(0, 1, len(observations))
  height = numpy.mean(observations, axis=1)

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(x, height, baseline="stacked")
  assert_canvas_matches(canvas, "axes-fill-one-magnitude-x")

def test_axes_fill_n_magnitudes():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(series, baseline="stacked")
  assert_canvas_matches(canvas, "axes-fill-n-magnitudes")

def test_axes_fill_n_magnitudes_x():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  x = numpy.linspace(0, 1, len(observations))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(x, series, baseline="stacked")
  assert_canvas_matches(canvas, "axes-fill-n-magnitudes-x")

def test_axes_fill_n_magnitudes_symmetric():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(series, baseline="symmetric")
  assert_canvas_matches(canvas, "axes-fill-n-magnitudes-symmetric")

def test_axes_fill_n_magnitudes_wiggle():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(series, baseline="wiggle")
  assert_canvas_matches(canvas, "axes-fill-n-magnitudes-wiggle")

def test_axes_fill_n_magnitudes_along_y():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(series, baseline="stacked", along="y")
  assert_canvas_matches(canvas, "axes-fill-n-magnitudes-along-y")

def test_axes_fill_n_magnitudes_titles():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.fill(series, title=["mean", "standard deviation"], baseline="stacked")
  assert_canvas_matches(canvas, "axes-fill-n-magnitudes-titles")

def test_axes_hlines_fail():
  with nose.tools.assert_raises(ValueError):
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.hlines("foo")

def test_axes_hlines():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.hlines(0)
  assert_canvas_matches(canvas, "axes-hlines")

def test_axes_hlines_multiple():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.hlines(numpy.linspace(-1, 1, 10))
  assert_canvas_matches(canvas, "axes-hlines-multiple")

def test_axes_vlines_fail():
  with nose.tools.assert_raises(ValueError):
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.vlines("foo")

def test_axes_vlines():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.vlines(0)
  assert_canvas_matches(canvas, "axes-vlines")

def test_axes_vlines_multiple():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.vlines(numpy.linspace(-1, 1, 10))
  assert_canvas_matches(canvas, "axes-vlines-multiple")

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
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.plot(series)
  assert_canvas_matches(canvas, "axes-plot-n-variables")

def test_axes_plot_n_variables_x():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  x = numpy.linspace(0, 1, len(observations))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.plot(x, series)
  assert_canvas_matches(canvas, "axes-plot-n-variables-x")

def test_axes_plot_n_variables_along_y():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

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
  b = numpy.ma.column_stack((numpy.min(observations, axis=1), numpy.median(observations, axis=1), numpy.max(observations, axis=1)))
  b[10:20, 0] = numpy.nan
  b[30:40, 1] = numpy.ma.masked
  b[20:30, 2] = numpy.nan

  canvas, axes, mark = toyplot.bars(b, baseline=None)
  assert_canvas_matches(canvas, "axes-bars-boundaries-masked-nan")

def test_axes_fill_boundaries_masked_nan():
  numpy.random.seed(1234)
  observations = numpy.random.normal(size=(50, 50))
  b = numpy.ma.column_stack((numpy.min(observations, axis=1), numpy.median(observations, axis=1), numpy.max(observations, axis=1)))
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
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.scatterplot(series)
  assert_canvas_matches(canvas, "axes-scatterplot-n-variables")

def test_axes_scatterplot_n_variables_x():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  x = numpy.linspace(0, 1, len(observations))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.scatterplot(x, series)
  assert_canvas_matches(canvas, "axes-scatterplot-n-variables-x")

def test_axes_scatterplot_n_variables_along_y():
  numpy.random.seed(1234)
  observations = numpy.random.normal(loc=1, size=(25, 100))
  series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(observations, axis=1), numpy.max(observations, axis=1)))

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
  marker_style = {"stroke":"black", "fill":"cornsilk"}
  label_style = {"stroke":"none", "fill":"black"}
  markers=[
    None,
    "",
    "|",
    "-",
    {"shape":"|", "angle":45},
    {"shape":"|", "angle":-45},
    "+",
    "x",
    {"shape":"x", "angle":22.5},
    "*",
    "^",
    {"shape":">", "mstyle":{"stroke":"red"}},
    {"shape":"v", "mstyle":{"stroke":"red", "fill":"yellow"}},
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
    {"shape":"", "label":"A"},
    {"shape":"o", "label":"1"},
    {"shape":"s", "mstyle":{"stroke":"blue", "fill":"white"}, "label":"B", "lstyle":{"fill":"blue"}},
    {"shape":"d", "label":"2", "lstyle":{"fill":"green"}},
    ]

  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.scatterplot(numpy.arange(len(markers)), fill="steelblue", marker=markers, size=100, mstyle=marker_style, mlstyle=label_style)
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
  axes.rect(x1, x2, y1, y2, fill=fill, palette=palette, title=title)
  assert_canvas_matches(canvas, "axes-rect")

def test_axes_text():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  x = numpy.linspace(0, 1)
  y = numpy.sin(x * 10)
  text = ["s%s" % index for index in range(len(x))]
  axes.text(x, y, text)
  assert_canvas_matches(canvas, "axes-text")

def test_axes_text_along_y():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  x = numpy.linspace(0, 1)
  y = numpy.sin(x * 10)
  text = ["s%s" % index for index in range(len(x))]
  axes.text(x, y, text, along="y")
  assert_canvas_matches(canvas, "axes-text-along-y")

def test_axes_text_angle_fill():
  x = numpy.zeros(10)
  y = x
  angle = numpy.linspace(90, 0, len(x), endpoint=True)
  fill = numpy.linspace(1, 0, len(x))

  canvas = toyplot.Canvas(400, 400)
  axes = canvas.axes(xmin=-0.25, xmax=0.5, ymin=-0.5, ymax=0.25)
  axes.text(x, y, text="Toyplot!", angle=angle, fill=fill, style={"font-size":"36px", "font-weight":"bold", "stroke":"white", "text-anchor":"begin"})

  assert_canvas_matches(canvas, "axes-text-angle-fill")

def test_axes_legend():
  canvas = toyplot.Canvas()
  axes = canvas.axes(grid=(2, 2, 1, 1))
  axes.legend((("foo", "s"), ("bar", "o")), corner=("bottom-left", 100, 50, 30))
  assert_canvas_matches(canvas, "axes-legend")

def test_animation_frame_sanity_checks():
  frame = toyplot.AnimationFrame(index=1, begin=2.3, end=2.4, changes=collections.defaultdict(lambda : collections.defaultdict(list)))
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
  nose.tools.assert_is_instance(html, basestring)

def test_locator_defaults():
  x = numpy.linspace(0, 2 * numpy.pi, 100)
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  axes.plot(x, numpy.sin(x))
  assert_canvas_matches(canvas, "locator-defaults")

def test_basic_tick_locator():
  x = numpy.linspace(0, 2 * numpy.pi, 100)
  canvas = toyplot.Canvas()
  axes = canvas.axes(xticklocator=toyplot.BasicTickLocator(count=10, format="{:.3g}"))
  axes.y.ticks.locator=toyplot.BasicTickLocator(count=3, format="{:.1f}")
  axes.plot(x, numpy.sin(x))
  assert_canvas_matches(canvas, "basic-tick-locator")

def test_explicit_tick_locator_locations():
  x = numpy.linspace(0, 2 * numpy.pi, 100)
  canvas = toyplot.Canvas()
  axes = canvas.axes(xticklocator=toyplot.ExplicitTickLocator(locations=[0, 2, numpy.pi, 4, 6]))
  axes.plot(x, numpy.sin(x))
  assert_canvas_matches(canvas, "explicit-tick-locator-locations")

def test_explicit_tick_locator_locations_labels():
  x = numpy.linspace(0, 2 * numpy.pi, 100)
  canvas = toyplot.Canvas()
  axes = canvas.axes(xticklocator=toyplot.ExplicitTickLocator(locations=[0, numpy.pi, 2 * numpy.pi], labels=["0", "pi", "2pi"]))
  axes.y.ticks.locator=toyplot.ExplicitTickLocator([-1, 1], ["-1", "1"])
  axes.plot(x, numpy.sin(x))
  assert_canvas_matches(canvas, "explicit-tick-locator-locations-labels")

def test_explicit_tick_locator_labels():
  x = numpy.linspace(0, 2 * numpy.pi, 100)
  canvas = toyplot.Canvas()
  axes = canvas.axes(xticklocator=toyplot.ExplicitTickLocator(labels=["red", "green", "blue"]))
  axes.y.ticks.locator=toyplot.ExplicitTickLocator([-1, 1], ["-1", "1"])
  axes.plot(x, numpy.sin(x))
  assert_canvas_matches(canvas, "explicit-tick-locator-labels")

def test_explicit_tick_locator_failure():
  with nose.tools.assert_raises(ValueError):
    toyplot.ExplicitTickLocator()

def test_extended_tick_locator():
  x = numpy.linspace(0, 2 * numpy.pi, 100)
  canvas = toyplot.Canvas()
  axes = canvas.axes(xticklocator=toyplot.ExtendedTickLocator(count=12))
  axes.y.ticks.locator=toyplot.ExtendedTickLocator(count=5)
  axes.plot(x, numpy.sin(x))
  assert_canvas_matches(canvas, "extended-tick-locator")

def test_heckbert_tick_locator():
  x = numpy.linspace(0, 2 * numpy.pi, 100)
  canvas = toyplot.Canvas()
  axes = canvas.axes(xticklocator=toyplot.HeckbertTickLocator(count=10))
  axes.y.ticks.locator=toyplot.HeckbertTickLocator(count=3)
  axes.plot(x, numpy.sin(x))
  assert_canvas_matches(canvas, "heckbert-tick-locator")

##################################################################################
# toyplot.html

def test_color_require_color():
  assert_color_equal(toyplot.color._require_color("red"), (1, 0, 0, 1))
  assert_color_equal(toyplot.color._require_color(toyplot.color.rgb(1, 1, 0)), (1, 1, 0, 1))
  assert_color_equal(toyplot.color._require_color(toyplot.color.rgba(1, 1, 0, 0.5)), (1, 1, 0, 0.5))
  assert_color_equal(toyplot.color._require_color((1, 1, 0)), (1, 1, 0, 1))
  assert_color_equal(toyplot.color._require_color((1, 1, 0, 0.5)), (1, 1, 0, 0.5))
  with nose.tools.assert_raises(ValueError):
    toyplot.color._require_color(5)

def test_color_palette():
  palette = toyplot.color.Palette()
  assert_html_matches(palette._repr_html_(), "color-palette")

def test_color_palette_reverse():
  palette = toyplot.color.Palette(reverse=True)
  assert_html_matches(palette._repr_html_(), "color-palette-reverse")

def test_color_palette_css_names():
  palette = toyplot.color.Palette(["red", "green", "blue", (1, 1, 0)])
  assert_html_matches(palette._repr_html_(), "color-palette-css-names")

def test_color_palette_len():
  palette = toyplot.color.Palette()
  nose.tools.assert_equal(len(palette), 8)

def test_color_palette_getitem():
  palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
  assert_color_equal(palette[0], (1, 0, 0, 1))
  assert_color_equal(palette[1], (0, 1, 0, 1))
  assert_color_equal(palette[-1], (0, 0, 1, 1))
  with nose.tools.assert_raises(IndexError):
    palette[3]
  with nose.tools.assert_raises(TypeError):
    palette[0:3]

def test_color_palette_iter():
  palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
  color = iter(palette)
  assert_color_equal(color.next(), (1, 0, 0, 1))
  assert_color_equal(color.next(), (0, 1, 0, 1))
  assert_color_equal(color.next(), (0, 0, 1, 1))
  with nose.tools.assert_raises(StopIteration):
    color.next()

def test_color_palette_color():
  palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
  assert_color_equal(palette.color(0), (1, 0, 0, 1))
  assert_color_equal(palette.color(-1), (0, 0, 1, 1))

def test_color_palette_css():
  palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
  nose.tools.assert_equal(palette.css(0), "rgba(100%,0%,0%,1)")
  nose.tools.assert_equal(palette.css(-1), "rgba(0%,0%,100%,1)")

def test_color_palette_add():
  palette = toyplot.color.brewer("Reds") + toyplot.color.brewer("Blues")
  assert_html_matches(palette._repr_html_(), "color-palette-add")

  with nose.tools.assert_raises(NotImplementedError):
    toyplot.color.Palette() + "foo"

def test_color_palette_iadd():
  palette = toyplot.color.Palette()
  palette += toyplot.color.brewer("Greens")
  assert_html_matches(palette._repr_html_(), "color-palette-iadd")

  with nose.tools.assert_raises(NotImplementedError):
    palette = toyplot.color.Palette()
    palette += "foo"

def test_color_lighten():
  palette = toyplot.color.lighten(toyplot.color.Palette().color(0))
  assert_html_matches(palette._repr_html_(), "color-lighten")

def test_color_brewer():
  palette = toyplot.color.brewer("BlueYellowRed")
  assert_html_matches(palette._repr_html_(), "color-brewer")

def test_color_brewer_count():
  palette = toyplot.color.brewer("BlueYellowRed", 5)
  assert_html_matches(palette._repr_html_(), "color-brewer-count")

def test_color_brewer_reverse():
  palette = toyplot.color.brewer("BlueYellowRed", 5, reverse=True)
  assert_html_matches(palette._repr_html_(), "color-brewer-reverse")

def test_color_brewer_all():
  for name in toyplot.color.brewer.names():
    for count in toyplot.color.brewer.counts(name):
      toyplot.color.brewer.category(name)

def test_color_brewer_palettes():
  def test(name):
    assert_html_matches(toyplot.color.brewer(name)._repr_html_(), "color-brewer-%s" % name)
  for name in toyplot.color.brewer.names():
    yield test, name

def test_color_categorical_map():
  colormap = toyplot.color.CategoricalMap(toyplot.color.brewer("BlueGreenBrown", 3))
  assert_html_matches(colormap._repr_html_(), "color-categorical-map")

def test_color_categorical_map_colors():
  colormap = toyplot.color.CategoricalMap(toyplot.color.Palette(["red", "lime", "blue", (1, 1, 1)]))
  assert_colors_equal(colormap.colors([0, 1, 3, 4]), [(1, 0, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1), (1, 0, 0, 1)])

def test_color_categorical_map_color():
  colormap = toyplot.color.CategoricalMap(toyplot.color.Palette(["red", "lime", "blue", (1, 1, 1)]))
  assert_color_equal(colormap.color(0), (1, 0, 0, 1))
  assert_color_equal(colormap.color(-1), (1, 1, 1, 1))

def test_color_categorical_map_css():
  colormap = toyplot.color.CategoricalMap(toyplot.color.Palette(["red", "lime", "blue", (1, 1, 1)]))
  nose.tools.assert_equal(colormap.css(0), "rgba(100%,0%,0%,1)")
  nose.tools.assert_equal(colormap.css(-1), "rgba(100%,100%,100%,1)")

def test_color_linear_map():
  map = toyplot.color.LinearMap(toyplot.color.brewer("BlueYellowRed"))
  assert_html_matches(map._repr_html_(), "color-linear-map")

def test_color_linear_map_color():
  map = toyplot.color.LinearMap(toyplot.color.Palette(["red", "blue"]), domain_min=0, domain_max=1)
  assert_color_equal(map.color(-1), (1, 0, 0, 1))
  assert_color_equal(map.color(0), (1, 0, 0, 1))
  assert_color_equal(map.color(0.5), (0.5, 0, 0.5, 1))
  assert_color_equal(map.color(1), (0, 0, 1, 1))
  assert_color_equal(map.color(2), (0, 0, 1, 1))

def test_color_linear_map_css():
  map = toyplot.color.LinearMap(toyplot.color.Palette(["red", "blue"]), domain_min=0, domain_max=1)
  nose.tools.assert_equal(map.css(-1), "rgba(100%,0%,0%,1)")
  nose.tools.assert_equal(map.css(0), "rgba(100%,0%,0%,1)")
  nose.tools.assert_equal(map.css(0.5), "rgba(50%,0%,50%,1)")
  nose.tools.assert_equal(map.css(1), "rgba(0%,0%,100%,1)")
  nose.tools.assert_equal(map.css(2), "rgba(0%,0%,100%,1)")

def test_color_diverging_map():
  map = toyplot.color.DivergingMap()
  assert_html_matches(map._repr_html_(), "color-diverging-map")

def test_color_diverging_maps():
  def test(name):
    assert_html_matches(toyplot.color.diverging(name)._repr_html_(), "color-diverging-map-%s" % name)
  for name in toyplot.color.diverging.names():
    yield test, name

def test_color_diverging_map_custom():
  map = toyplot.color.DivergingMap(toyplot.color.rgb(0.7, 0, 0), toyplot.color.rgb(0, 0.6, 0))
  assert_html_matches(map._repr_html_(), "color-diverging-map-custom")

def test_color_diverging_map_color():
  map = toyplot.color.DivergingMap(domain_min=0, domain_max=1)
  assert_color_equal(map.color(-1), [ 0.33479085,  0.28308437,  0.75649522,  1.        ])
  assert_color_equal(map.color(0), [ 0.33479085,  0.28308437,  0.75649522,  1.        ])
  assert_color_equal(map.color(0.5), [ 0.86541961,  0.86538428,  0.86533315,  1.        ])
  assert_color_equal(map.color(1), [ 0.69462562,  0.00296461,  0.15458183,  1.        ])
  assert_color_equal(map.color(2), [ 0.69462562,  0.00296461,  0.15458183,  1.        ])

def test_color_diverging_map_css():
  map = toyplot.color.DivergingMap(domain_min=0, domain_max=1)
  nose.tools.assert_equal(map.css(-1), "rgba(33.5%,28.3%,75.6%,1)")
  nose.tools.assert_equal(map.css(0), "rgba(33.5%,28.3%,75.6%,1)")
  nose.tools.assert_equal(map.css(0.5), "rgba(86.5%,86.5%,86.5%,1)")
  nose.tools.assert_equal(map.css(1), "rgba(69.5%,0.296%,15.5%,1)")
  nose.tools.assert_equal(map.css(2), "rgba(69.5%,0.296%,15.5%,1)")

##################################################################################
# toyplot.color.css

def test_color_css_convert():
  nose.tools.assert_equal(toyplot.color.css.convert(toyplot.color.rgba(1, .5, .4, 1)), "rgba(100%,50%,40%,1)")

def test_color_css_parse_name():
  assert_color_equal(toyplot.color.css.parse("red"), (1, 0, 0, 1))
  assert_color_equal(toyplot.color.css.parse("Red"), (1, 0, 0, 1))
  assert_color_equal(toyplot.color.css.parse("RED"), (1, 0, 0, 1))
  assert_color_equal(toyplot.color.css.parse("aqua"), (0, 1, 1, 1))
  assert_color_equal(toyplot.color.css.parse("ivory"), (1, 1, 240/255, 1))
  assert_color_equal(toyplot.color.css.parse("transparent"), (0, 0, 0, 0))
  nose.tools.assert_equal(toyplot.color.css.parse("baloney"), None)

def test_color_css_parse_hex3():
  assert_color_equal(toyplot.color.css.parse("#f0f"), (1, 0, 1, 1))
  assert_color_equal(toyplot.color.css.parse("#F0F"), (1, 0, 1, 1))
  assert_color_equal(toyplot.color.css.parse("#F8F"), (1, 8/15, 1, 1))

def test_color_css_parse_hex6():
  assert_color_equal(toyplot.color.css.parse("#ff00ff"), (1, 0, 1, 1))
  assert_color_equal(toyplot.color.css.parse("#FF00ff"), (1, 0, 1, 1))
  assert_color_equal(toyplot.color.css.parse("#FF88ff"), (1, 8/15, 1, 1))

def test_color_css_parse_rgb():
  assert_color_equal(toyplot.color.css.parse("rgb(255, 128, 3)"), (255/255, 128/255, 3/255, 1))
  assert_color_equal(toyplot.color.css.parse("rgb(76%, 32%, 89%)"), (.76, .32, .89, 1))

def test_color_css_parse_rgba():
  assert_color_equal(toyplot.color.css.parse("rgba(255, 128, 3, 0.45)"), (255/255, 128/255, 3/255, 0.45))
  assert_color_equal(toyplot.color.css.parse("rgba(76%, 32%, 89%, .76)"), (.76, .32, .89, .76))

def test_color_css_parse_hsl():
  assert_color_equal(toyplot.color.css.parse("hsl(0, 100%, 50%)"), (1, 0, 0, 1))

def test_color_css_parse_hsla():
  assert_color_equal(toyplot.color.css.parse("hsla(0, 100%, 50%, 0.32)"), (1, 0, 0, 0.32))

##################################################################################
# toyplot.html

def test_html_render_dom():
  canvas = toyplot.Canvas()
  canvas.axes()
  dom = toyplot.html.render(canvas)

def test_html_render_path():
  canvas = toyplot.Canvas()
  canvas.axes()
  toyplot.html.render(canvas, os.path.join(tempfile.mkdtemp(), "test.html"))

def test_html_render_animation():
  canvas = toyplot.Canvas()
  axes = canvas.axes()
  text = canvas.text(100, 100, "")
  scatterplot = axes.scatterplot(numpy.arange(10))
  def callback(frame):
    frame.set_mark_style(text, {"fill-opacity":frame.time()})
    frame.set_datum_text(text, 0, 0, "frame %s time %s duration %s" % (frame.index(), frame.time(), frame.duration()))
    frame.set_datum_style(scatterplot, 0, frame.index(), {"stroke":"none"})
  canvas.animate(10, callback)
  dom = toyplot.html.render(canvas)

def test_html_ipython_html():
  canvas = toyplot.Canvas()
  canvas.axes()
  canvas._repr_html_()

##################################################################################
# toyplot.mp4

def test_mp4_render():
  if hasattr(toyplot, "mp4"):
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    text = canvas.text(100, 100, "")
    scatterplot = axes.scatterplot(numpy.arange(10))
    def callback(frame):
      frame.set_mark_style(text, {"fill-opacity":frame.time()})
      frame.set_datum_text(text, 0, 0, "frame %s time %s duration %s" % (frame.index(), frame.time(), frame.duration()))
      frame.set_datum_style(scatterplot, 0, frame.index(), {"stroke":"none"})
    canvas.animate(10, callback)
    def progress(frame):
      pass
    toyplot.mp4.render(canvas, os.path.join(tempfile.mkdtemp(), "test.mp4"), progress=progress)

##################################################################################
# toyplot.png

def test_png_render_defaults():
  if hasattr(toyplot, "png"):
    canvas = toyplot.Canvas()
    canvas.axes()
    image = toyplot.png.render(canvas)
    nose.tools.assert_is_instance(image, basestring)
    nose.tools.assert_equal(image[1:4], "PNG")

def test_png_render_buffer():
  if hasattr(toyplot, "png"):
    buffer = StringIO.StringIO()
    canvas = toyplot.Canvas()
    canvas.axes()
    toyplot.png.render(canvas, buffer)
    nose.tools.assert_equal(buffer.getvalue()[1:4], "PNG")

def test_png_render_path():
  if hasattr(toyplot, "png"):
    canvas = toyplot.Canvas()
    canvas.axes()
    toyplot.png.render(canvas, os.path.join(tempfile.mkdtemp(), "test.png"))

def test_png_render_frames():
  if hasattr(toyplot, "png"):
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    text = canvas.text(100, 100, "")
    scatterplot = axes.scatterplot(numpy.arange(10))
    def callback(frame):
      frame.set_mark_style(text, {"fill-opacity":frame.time()})
      frame.set_datum_text(text, 0, 0, "frame %s" % frame.index())
      frame.set_datum_style(scatterplot, 0, frame.index(), {"stroke":"none"})
    canvas.animate(10, callback)
    for frame in toyplot.png.render_frames(canvas):
      nose.tools.assert_is_instance(frame, basestring)
      nose.tools.assert_equal(frame[1:4], "PNG")

def test_cairo_small_font():
  if hasattr(toyplot, "png"):
    canvas = toyplot.Canvas()
    axes = canvas.axes(label="Small Text!")
    axes.label.style={"font-size":"8px"}
    toyplot.png.render(canvas)

##################################################################################
# toyplot.svg

def test_svg_render_path():
  canvas = toyplot.Canvas()
  canvas.axes()
  toyplot.svg.render(canvas, os.path.join(tempfile.mkdtemp(), "test.svg"))

#########################################################################################################################
# High-level tests that combine multiple API calls into whole figures.

def test_basic_api():
  numpy.random.seed(1234)
  x = numpy.linspace(0, 1, 100)
  y = x + (0.1 * x * numpy.random.random(len(x)))

  canvas = toyplot.Canvas()
  axes = canvas.axes(grid=(2, 2, 0, 1, 0, 2))
  axes.plot(x, y, style={"stroke":"steelblue", "stroke-width":1.0}, marker="o")
  axes.x.label.text="1st Axis"
  axes.y.label.text="2nd Axis"

  axes = canvas.axes(grid=(2, 2, 2), label="2nd Axes")
  axes.plot(x, y, style={"stroke":"red"})

  axes = canvas.axes(grid=(2, 2, 3), label="3rd Axes")
  axes.plot(x, y, style={"stroke":"green"})

  canvas.text(300, 30, "Plot Title", style={"font-size":"16px", "font-weight":"bold", "text-anchor":"middle"}, title="The plot's title")

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
  axes.hlines(0, style={"stroke-dasharray":"5,5"}, title="y = 0")
  axes.vlines(0, style={"stroke-dasharray":"5,5"}, title="x = 0")
  for i in numpy.linspace(1, 2, 7):
    axes.plot(x, 0.5 * i * numpy.sin(x * i), title="%s * sin(x * %s)" % (0.5*i, i))
  assert_canvas_matches(canvas, "axes")

def test_axes_layout():
  canvas = toyplot.Canvas()
  axes = canvas.axes(label="Title", xlabel="X Label", ylabel="Y Label", xmin=0, xmax=1, ymin=0, ymax=1)
  axes.text(0.5, 0.5, "Axes Region", style={"fill":"black", "text-anchor":"middle", "alignment-baseline":"middle"})
  assert_canvas_matches(canvas, "axes-layout")

def test_legend():
  x = numpy.linspace(0, 2 * numpy.pi, 200)
  canvas = toyplot.Canvas(800, 600)
  axes = canvas.axes()
  plots = [axes.plot(x, 0.5 * i * numpy.sin(x * i)) for i in numpy.linspace(1, 2, 3)]
  fill = axes.fill(x, numpy.sin(x) * 0.1, numpy.cos(x) * 0.1)
  axes.x.label.text="Time"
  axes.y.label.text="Temp"
  canvas.legend([
    ("Plot 1", plots[0]),
    ("Plot 2", plots[1]),
    ("Plot 3", plots[2]),
    ("Fill", fill),
    ("Explicit Line", "line", {"stroke":"red", "stroke-width":1.0}),
    ("Explicit Rect", "rect", {"fill":"green"}),
    ("Explicit Marker", "^", {"fill":"lightblue", "stroke":"black"}),
    ("Explicit Marker", "o", {"fill":"yellow", "stroke":"black"}),
    ("Explicit Marker", "s", {"fill":"pink", "stroke":"black"})],
    bounds=(100, 200, 350, 550),
    )
  assert_canvas_matches(canvas, "legend")

def test_bounds_placement():
  style = {"stroke":"black"}
  canvas = toyplot.Canvas(800, 600, style={"border":"1px solid black"})
  canvas.legend([], style=style, bounds=(400-100, 400+100, 20, 50))
  canvas.legend([], style=style, bounds=("25%", 400+100, 80, 110))
  canvas.legend([], style=style, bounds=(400-100, "75%", 140, 170))
  canvas.legend([], style=style, bounds=("33%", "66%", 200, 230))
  canvas.legend([], style=style, bounds=(20, 50, 450-20, 450+20))
  canvas.legend([], style=style, bounds=(80, 110, "50%", 450+20))
  canvas.legend([], style=style, bounds=(140, 170, 450-20, "90%"))
  canvas.legend([], style=style, bounds=(200, 230, "50%", "90%"))
  canvas.legend([], style=style, bounds=("66%", "90%", "66%", "90%"))
  assert_canvas_matches(canvas, "bounds-placement")

def test_corner_placement():
  style = {"stroke":"black"}
  canvas = toyplot.Canvas(800, 600, style={"border":"1px solid black"})
  canvas.legend([("top", "^")], style=style, corner=("top", 100, 30, 10))
  canvas.legend([("top-right", "^")], style=style, corner=("top-right", 100, 30, 10))
  canvas.legend([("right", "^")], style=style, corner=("right", 100, 30, 10))
  canvas.legend([("bottom-right", "^")], style=style, corner=("bottom-right", 150, 30, 10))
  canvas.legend([("bottom", "^")], style=style, corner=("bottom", 100, 30, 10))
  canvas.legend([("bottom-left", "^")], style=style, corner=("bottom-left", 100, 30, 10))
  canvas.legend([("left", "^")], style=style, corner=("left", 100, 30, 10))
  canvas.legend([("top-left", "^")], style=style, corner=("top-left", 100, 30, 10))
  canvas.legend([("top-left", "^")], style=style, corner=("top-left", 100, 30, 50))
  canvas.legend([("top-left", "^")], style=style, corner=("top-left", "20%", "10%", 100))
  assert_canvas_matches(canvas, "corner-placement")

def test_grid_placement():
  x = numpy.linspace(0, 2 * numpy.pi, 1000)
  canvas = toyplot.Canvas(800, 600, style={"border":"1px solid black"})
  inset = canvas.axes(grid=(3, 3, 0), label="3x3 Grid")
  inset.plot(x, numpy.sin(x))
  inset = canvas.axes(grid=(3, 3, 0, 1, 1, 2), label="3x3 Grid colspan=2")
  inset.plot(x, numpy.sin(x))
  inset = canvas.axes(grid=(3, 3, 1, 0), gutter=20, label="3x3 Grid gutter=20")
  inset.plot(x, numpy.sin(x))
  inset = canvas.axes(grid=(3, 3, 1, 1), gutter=20, label="3x3 Grid gutter=20")
  inset.plot(x, numpy.sin(x))
  inset = canvas.axes(grid=(3, 3, 1, 2, 2, 1), gutter=20, label="3x3 Grid gutter=20 rowspan=2")
  inset.plot(x, numpy.sin(x))
  assert_canvas_matches(canvas, "grid-placement")

