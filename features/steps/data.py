from behave import *
import nose.tools
import numpy.testing

import collections
import io
import numpy
import os
import tempfile
import toyplot.data
import toyplot.latex
import toyplot.testing

root_dir = os.path.dirname(os.path.dirname(__file__))

@given(u'a new toyplot.data.table')
def step_impl(context):
  context.data = toyplot.data.Table()

@then(u'the table should be empty')
def step_impl(context):
  nose.tools.assert_equal(len(context.data), 0)
  nose.tools.assert_equal(context.data.shape, (0, 0))
  nose.tools.assert_equal(context.data.items(), [])
  nose.tools.assert_equal(list(context.data.keys()), [])
  nose.tools.assert_equal(context.data.values(), [])

@then(u'adding columns should change the table')
def step_impl(context):
  context.data["a"] = numpy.arange(10)
  nose.tools.assert_equal(list(context.data.keys()), ["a"])
  nose.tools.assert_equal(context.data.shape, (10, 1))

  context.data["b"] = context.data["a"] ** 2
  nose.tools.assert_equal(list(context.data.keys()), ["a", "b"])
  nose.tools.assert_equal(context.data.shape, (10, 2))
  numpy.testing.assert_array_equal(context.data["b"], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

  context.data["c"] = numpy.zeros(10)
  nose.tools.assert_equal(list(context.data.keys()), ["a", "b", "c"])
  nose.tools.assert_equal(context.data.shape, (10, 3))
  numpy.testing.assert_array_equal(context.data["c"], [0] * 10)

@then(u'extracting columns should return a new table')
def step_impl(context):
  table = context.data.columns(["b", "a"])
  nose.tools.assert_equal(list(table.keys()), ["b", "a"])
  nose.tools.assert_equal(table.shape, (10, 2))

@then(u'deleting columns should change the table')
def step_impl(context):
  del context.data["c"]
  nose.tools.assert_equal(list(context.data.keys()), ["a", "b"])
  nose.tools.assert_equal(context.data.shape, (10, 2))

@then(u'indexing should return a new table with one row')
def step_impl(context):
  table = context.data[5]
  nose.tools.assert_equal(list(table.keys()), ["a", "b"])
  nose.tools.assert_equal(table.shape, (1, 2))
  numpy.testing.assert_array_equal(table["a"], [5])

@then(u'slicing should return a new table with a range of rows')
def step_impl(context):
  table = context.data[slice(0, 6, 2)]
  nose.tools.assert_equal(list(table.keys()), ["a", "b"])
  nose.tools.assert_equal(table.shape, (3, 2))
  numpy.testing.assert_array_equal(table["a"], [0, 2, 4])

@then(u'extracting rows by index should return a new table with one row')
def step_impl(context):
  table = context.data.rows(8)
  nose.tools.assert_equal(list(table.keys()), ["a", "b"])
  nose.tools.assert_equal(table.shape, (1, 2))
  numpy.testing.assert_array_equal(table["a"], [8])

@then(u'extracting rows using multiple indices should return a new table with the specified rows')
def step_impl(context):
  table = context.data.rows([1, 2, 3])
  nose.tools.assert_equal(list(table.keys()), ["a", "b"])
  nose.tools.assert_equal(table.shape, (3, 2))
  numpy.testing.assert_array_equal(table["a"], [1, 2, 3])

@then(u'new columns must have a string name')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    context.data[3] = numpy.arange(10)

@then(u'new column names must be ascii, or a unicode string')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    context.data[toyplot.compatibility.bytes_type("T\xefm")] = numpy.arange(10)

@then(u'new columns must have the same number of rows as existing columns')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    context.data["c"] = numpy.random.random(4)

@then(u'new columns must be one-dimensional')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    context.data["c"] = numpy.random.random((10, 4))

@when(u'toyplot.data.Table is initialized with nothing')
def step_impl(context):
  context.data = toyplot.data.Table()

@then(u'the toyplot.data.Table is empty')
def step_impl(context):
  nose.tools.assert_equal(len(context.data), 0)
  nose.tools.assert_equal(context.data.shape, (0, 0))
  nose.tools.assert_equal(list(context.data.items()), [])
  nose.tools.assert_equal(list(context.data.keys()), [])
  nose.tools.assert_equal(list(context.data.values()), [])

@when(u'toyplot.data.Table is initialized with a toyplot.data.Table')
def step_impl(context):
  table = toyplot.data.Table()
  table["a"] = numpy.arange(10)
  table["b"] = table["a"] ** 2
  context.data = table

@when(u'toyplot.data.Table is initialized with an OrderedDict containing columns')
def step_impl(context):
  context.data = collections.OrderedDict([("a", numpy.arange(10)), ("b", numpy.arange(10) ** 2)])

@then(u'the toyplot.data.Table contains the columns')
def step_impl(context):
  table = toyplot.data.Table(context.data)
  nose.tools.assert_equal(list(table.keys()), ["a", "b"])
  numpy.testing.assert_array_equal(table["a"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  numpy.testing.assert_array_equal(table["b"], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

@when(u'toyplot.data.Table is initialized with a dict containing columns')
def step_impl(context):
  context.data = {"b" : numpy.arange(10) ** 2, "a" : numpy.arange(10)}

@then(u'the toyplot.data.Table contains the columns, sorted by key')
def step_impl(context):
  table = toyplot.data.Table(context.data)
  nose.tools.assert_equal(list(table.keys()), ["a", "b"])
  numpy.testing.assert_array_equal(table["a"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  numpy.testing.assert_array_equal(table["b"], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

@then(u'the toyplot.data.Table raises ValueError')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    toyplot.data.Table(context.data)

@given(u'a toyplot.data.table with some data')
def step_impl(context):
  numpy.random.seed(1234)
  context.data = toyplot.data.Table()
  context.data["foo"] = numpy.arange(10)
  context.data["bar"] = numpy.random.random(10)
  context.data["baz"] = numpy.random.choice(["red", "green", "blue"], size=10)

@then(u'the table can be rendered as format latex string')
def step_impl(context):
  toyplot.testing.assert_latex_equal(toyplot.latex.render(context.data), "data-table")

@then(u'the table can be rendered as format latex fobj')
def step_impl(context):
  buffer = io.BytesIO()
  toyplot.latex.render(context.data, buffer)
  toyplot.testing.assert_latex_equal(toyplot.compatibility.unicode_type(buffer.getvalue(), "utf-8"), "data-table")

@then(u'the table can be rendered as format latex file')
def step_impl(context):
  path = os.path.join(tempfile.mkdtemp(), "test.tex")
  toyplot.latex.render(context.data, path)
  toyplot.testing.assert_latex_equal(open(path, "r").read(), "data-table")

@then(u'the table can be rendered as format latex string with hline')
def step_impl(context):
  toyplot.testing.assert_latex_equal(toyplot.latex.render(context.data, hlines=[5]), "data-table-with-hline")

@then(u'the table can be rendered as format ipython html string')
def step_impl(context):
  toyplot.testing.assert_html_equal(context.data._repr_html_(), "data-table")


