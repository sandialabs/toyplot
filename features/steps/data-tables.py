# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import nose.tools
import numpy.testing

import collections
import io
import numpy
import os
import sys
import tempfile

import toyplot.data

import testing


try:
    import pandas
except:
    pass


def pandas_available(context):
    if "pandas" in sys.modules:
        return True

    context.scenario.skip(reason="The pandas library is not available.")
    return False

root_dir = os.path.dirname(os.path.dirname(__file__))


@given(u'a new toyplot.data.table')
def step_impl(context):
    context.data = toyplot.data.Table()


@then(u'the table should be empty')
def step_impl(context):
    nose.tools.assert_equal(len(context.data), 0)
    nose.tools.assert_equal(context.data.shape, (0, 0))
    nose.tools.assert_equal(list(context.data.items()), [])
    nose.tools.assert_equal(list(context.data.keys()), [])
    nose.tools.assert_equal(list(context.data.values()), [])


@then(u'adding columns should change the table')
def step_impl(context):
    context.data["a"] = numpy.arange(10)
    nose.tools.assert_equal(list(context.data.keys()), ["a"])
    nose.tools.assert_equal(context.data.shape, (10, 1))

    context.data["b"] = context.data["a"] ** 2
    nose.tools.assert_equal(list(context.data.keys()), ["a", "b"])
    nose.tools.assert_equal(context.data.shape, (10, 2))

    context.data["c"] = numpy.zeros(10)
    nose.tools.assert_equal(list(context.data.keys()), ["a", "b", "c"])
    nose.tools.assert_equal(context.data.shape, (10, 3))


@then(u'columns can be retrieved by name')
def step_impl(context):
    numpy.testing.assert_array_equal(context.data["a"], numpy.arange(10))


@then(u'partial columns can be retrieved by name and index')
def step_impl(context):
    nose.tools.assert_equal(context.data["a", 5], 5)


@then(u'partial columns can be retrieved by name and slice')
def step_impl(context):
    numpy.testing.assert_array_equal(context.data["a", 5:7], [5, 6])


@then(u'partial tables can be retrieved by row index')
def step_impl(context):
    table = context.data[5]
    nose.tools.assert_equal(list(table.keys()), ["a", "b", "c"])
    nose.tools.assert_equal(table.shape, (1, 3))
    numpy.testing.assert_array_equal(table["a"], [5])

@then(u'partial tables can be retrieved by row slice')
def step_impl(context):
    table = context.data[5:7]
    nose.tools.assert_equal(list(table.keys()), ["a", "b", "c"])
    nose.tools.assert_equal(table.shape, (2, 3))
    numpy.testing.assert_array_equal(table["a"], [5,6])

@then(u'partial tables can be retrieved by row index and column name')
def step_impl(context):
    table = context.data[5, "b"]
    nose.tools.assert_equal(list(table.keys()), ["b"])
    nose.tools.assert_equal(table.shape, (1, 1))
    numpy.testing.assert_array_equal(table["b"], [25])


@then(u'partial tables can be retrieved by row slice and column name')
def step_impl(context):
    table = context.data[5:7, "b"]
    nose.tools.assert_equal(list(table.keys()), ["b"])
    nose.tools.assert_equal(table.shape, (2, 1))
    numpy.testing.assert_array_equal(table["b"], [25,36])


@then(u'partial tables can be retrieved by row index and column names')
def step_impl(context):
    table = context.data[5, ["b", "a"]]
    nose.tools.assert_equal(list(table.keys()), ["b", "a"])
    nose.tools.assert_equal(table.shape, (1, 2))
    numpy.testing.assert_array_equal(table["a"], [5])


@then(u'partial tables can be retrieved by row slice and column names')
def step_impl(context):
    table = context.data[5:7, ["b", "a"]]
    nose.tools.assert_equal(list(table.keys()), ["b", "a"])
    nose.tools.assert_equal(table.shape, (2, 2))
    numpy.testing.assert_array_equal(table["a"], [5,6])


@then(u'partial tables can be retrieved by column names')
def step_impl(context):
    table = context.data[["b", "a"]]
    nose.tools.assert_equal(list(table.keys()), ["b", "a"])
    nose.tools.assert_equal(table.shape, (10, 2))


@then(u'partial tables can be retrieved by row indices')
def step_impl(context):
    table = context.data[[5, 7]]
    nose.tools.assert_equal(list(table.keys()), ["a", "b", "c"])
    nose.tools.assert_equal(table.shape, (2, 3))
    numpy.testing.assert_array_equal(table["a"], [5, 7])


@then(u'columns can be replaced by name')
def step_impl(context):
    context.data["c"] = numpy.ones(10)
    nose.tools.assert_equal(list(context.data.keys()), ["a", "b", "c"])
    nose.tools.assert_equal(context.data.shape, (10, 3))
    numpy.testing.assert_array_equal(context.data["c"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


@then(u'partial columns can be modified by name and separate index')
def step_impl(context):
    context.data["c"][0] = 0
    numpy.testing.assert_array_equal(context.data["c"], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1])


@then(u'partial columns can be modified by name and separate slice')
def step_impl(context):
    context.data["c"][1:4] = [1, 2, 3]
    numpy.testing.assert_array_equal(context.data["c"], [0, 1, 2, 3, 1, 1, 1, 1, 1, 1])


@then(u'partial columns can be modified by name and index')
def step_impl(context):
    context.data["c", 4] = 4
    numpy.testing.assert_array_equal(context.data["c"], [0, 1, 2, 3, 4, 1, 1, 1, 1, 1])


@then(u'partial columns can be modified by name and slice')
def step_impl(context):
    context.data["c", 5:8] = [5, 6, 7]
    numpy.testing.assert_array_equal(context.data["c"], [0, 1, 2, 3, 4, 5, 6, 7, 1, 1])


@then(u'partial columns can be masked by name and index')
def step_impl(context):
    context.data["c", 3] = numpy.ma.masked
    nose.tools.assert_is(context.data["c"][3], numpy.ma.masked)


@then(u'partial columns can be masked by name and slice')
def step_impl(context):
    context.data["c", 8:10] = numpy.ma.masked
    nose.tools.assert_is(context.data["c"][8], numpy.ma.masked)
    nose.tools.assert_is(context.data["c"][9], numpy.ma.masked)


@then(u'deleting columns should change the table')
def step_impl(context):
    del context.data["c"]
    nose.tools.assert_equal(list(context.data.keys()), ["a", "b"])
    nose.tools.assert_equal(context.data.shape, (10, 2))


@then(u'new columns must have a string name')
def step_impl(context):
    with nose.tools.assert_raises(ValueError):
        context.data[3] = numpy.arange(10)


@then(u'new columns must have the same number of rows as existing columns')
def step_impl(context):
    with nose.tools.assert_raises(ValueError):
        context.data["c"] = numpy.random.random(4)


@then(u'new columns must be one-dimensional')
def step_impl(context):
    with nose.tools.assert_raises(ValueError):
        context.data["c"] = numpy.random.random((10, 4))


@then(u'per-column metadata can be specified')
def step_impl(context):
    nose.tools.assert_equal(context.data.metadata("b"), {})
    context.data.metadata("b")["foo"] = True
    nose.tools.assert_equal(context.data.metadata("b"), {"foo": True})

    with nose.tools.assert_raises(ValueError):
        context.data.metadata("c")


@then(u'the table can be converted to a numpy matrix')
def step_impl(context):
    matrix = context.data.matrix()
    numpy.testing.assert_array_equal(matrix, [[0,0],[1,1],[2,4],[3,9],[4,16],[5,25],[6,36],[7,49],[8,64],[9,81]])


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


@when(
    u'toyplot.data.Table is initialized with an OrderedDict containing columns')
def step_impl(context):
    context.data = collections.OrderedDict(
        [("a", numpy.arange(10)), ("b", numpy.arange(10) ** 2)])


@then(u'the toyplot.data.Table contains the columns')
def step_impl(context):
    table = toyplot.data.Table(context.data)
    nose.tools.assert_equal(list(table.keys()), ["a", "b"])
    numpy.testing.assert_array_equal(
        table["a"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    numpy.testing.assert_array_equal(
        table["b"], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])


@when(u'toyplot.data.Table is initialized with a dict containing columns')
def step_impl(context):
    context.data = {"b": numpy.arange(10) ** 2, "a": numpy.arange(10)}


@then(u'the toyplot.data.Table contains the columns, sorted by key')
def step_impl(context):
    table = toyplot.data.Table(context.data)
    nose.tools.assert_equal(list(table.keys()), ["a", "b"])
    numpy.testing.assert_array_equal(
        table["a"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    numpy.testing.assert_array_equal(
        table["b"], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

@when(u'toyplot.data.Table is initialized with a sequence of name, column tuples')
def step_impl(context):
    context.data = [("a", numpy.arange(10)), ("b", numpy.arange(10) ** 2)]

@when(u'toyplot.data.Table is initialized with a matrix')
def step_impl(context):
    context.data = numpy.arange(16).reshape((4, 4))

@then(u'the toyplot.data.Table contains the matrix columns with generated keys')
def step_impl(context):
    table = toyplot.data.Table(context.data)
    nose.tools.assert_equal(list(table.keys()), ["0", "1", "2", "3"])
    numpy.testing.assert_array_equal(
        table["0"], [0, 4, 8, 12])
    numpy.testing.assert_array_equal(
        table["1"], [1, 5, 9, 13])
    numpy.testing.assert_array_equal(
        table["2"], [2, 6, 10, 14])
    numpy.testing.assert_array_equal(
        table["3"], [3, 7, 11, 15])


@when(u'toyplot.data.Table is initialized with an array')
def step_impl(context):
   context.data = numpy.arange(16)


@when(u'toyplot.data.Table is initialized with an integer')
def step_impl(context):
  context.data = 5


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
    context.data["baz"] = numpy.random.choice(
        ["red", "green", "blue"], size=10)


@when(u'toyplot.data.Table is initialized with a csv file')
def step_impl(context):
    context.data = toyplot.data.read_csv("docs/temperatures.csv")


@then(u'the toyplot.data.Table contains the csv file columns')
def step_impl(context):
    nose.tools.assert_equal(context.data.shape, (362, 6))
    nose.tools.assert_equal(list(context.data.keys()), ['STATION', 'STATION_NAME', 'DATE', 'TMAX', 'TMIN', 'TOBS'])
    for column in context.data.values():
        nose.tools.assert_true(issubclass(column.dtype.type, numpy.character))


@when(u'toyplot.data.Table is initialized with a csv file and conversion')
def step_impl(context):
    context.data = toyplot.data.read_csv("docs/temperatures.csv", convert=True)


@then(u'the toyplot.data.Table contains the csv file columns with numeric type')
def step_impl(context):
    nose.tools.assert_equal(context.data.shape, (362, 6))
    nose.tools.assert_equal(list(context.data.keys()), ['STATION', 'STATION_NAME', 'DATE', 'TMAX', 'TMIN', 'TOBS'])
    for column, column_type in zip(context.data.values(), [numpy.character, numpy.character, numpy.integer, numpy.integer, numpy.integer, numpy.integer]):
        nose.tools.assert_true(issubclass(column.dtype.type, column_type))


@when(u'toyplot.data.Table is initialized with a pandas dataframe')
def step_impl(context):
    if pandas_available(context):
        context.data = toyplot.data.Table(pandas.read_csv("docs/temperatures.csv"))


@then(u'the toyplot.data.Table contains the data frame columns')
def step_impl(context):
    nose.tools.assert_equal(context.data.shape, (362, 6))
    nose.tools.assert_equal(list(context.data.keys()), ['STATION', 'STATION_NAME', 'DATE', 'TMAX', 'TMIN', 'TOBS'])


@when(u'toyplot.data.Table is initialized with a pandas dataframe with index')
def step_impl(context):
    if pandas_available(context):
        context.data = toyplot.data.Table(pandas.read_csv("docs/temperatures.csv"), index=True)


@then(u'the toyplot.data.Table contains the data frame columns plus an index column')
def step_impl(context):
    nose.tools.assert_equal(context.data.shape, (362, 7))
    nose.tools.assert_equal(list(context.data.keys()), ["index0", 'STATION', 'STATION_NAME', 'DATE', 'TMAX', 'TMIN', 'TOBS'])


@when(u'toyplot.data.Table is initialized with a pandas dataframe with hierarchical index')
def step_impl(context):
    if pandas_available(context):
        index = [numpy.array(["foo", "foo", "bar", "bar"]), numpy.array(["one", "two", "one", "two"])]
        data_frame = pandas.DataFrame(numpy.ones((4, 4)), index=index)
        context.data = toyplot.data.Table(data_frame, index=True)


@then(u'the toyplot.data.Table contains the data frame columns plus multiple index columns')
def step_impl(context):
    nose.tools.assert_equal(context.data.shape, (4, 6))
    nose.tools.assert_equal(list(context.data.keys()), ["index0", 'index1', '0', '1', '2', '3'])


@when(u'toyplot.data.Table is initialized with a pandas dataframe with hierarchical index and custom index format')
def step_impl(context):
    if pandas_available(context):
        index = [numpy.array(["foo", "foo", "bar", "bar"]), numpy.array(["one", "two", "one", "two"])]
        data_frame = pandas.DataFrame(numpy.ones((4, 4)), index=index)
        context.data = toyplot.data.Table(data_frame, index="Index {}")


@then(u'the toyplot.data.Table contains the data frame columns plus multiple custom format index columns')
def step_impl(context):
    nose.tools.assert_equal(context.data.shape, (4, 6))
    nose.tools.assert_equal(list(context.data.keys()), ["Index 0", 'Index 1', '0', '1', '2', '3'])


@when(u'toyplot.data.Table is initialized with a pandas dataframe with duplicate column names')
def step_impl(context):
    if pandas_available(context):
        context.data = toyplot.data.Table(pandas.read_csv("docs/temperatures.csv")[["STATION", "DATE", "STATION", "DATE", "DATE"]])


@then(u'the toyplot.data.Table contains the data frame columns with uniqified column names')
def step_impl(context):
    nose.tools.assert_equal(list(context.data.keys()), ['STATION', 'DATE', 'STATION-1', 'DATE-1', 'DATE-2'])


@then(u'the table can be rendered as format ipython html string')
def step_impl(context):
    html = context.data._repr_html_()
    nose.tools.assert_is_instance(html, toyplot.compatibility.unicode_type)
    testing.assert_html_equal(html, "data-table")


