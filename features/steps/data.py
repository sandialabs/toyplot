from behave import *
import nose.tools
import numpy.testing

import collections
import numpy
import os
import tempfile
import toyplot.data
import toyplot.latex
import StringIO

@given(u'a new toyplot.data.table')
def step_impl(context):
  context.value = toyplot.data.Table()

@then(u'the table should be empty')
def step_impl(context):
  nose.tools.assert_equal(len(context.value), 0)
  nose.tools.assert_equal(context.value.shape, (0, 0))
  nose.tools.assert_equal(context.value.items(), [])
  nose.tools.assert_equal(context.value.keys(), [])
  nose.tools.assert_equal(context.value.values(), [])

@then(u'adding columns should change the table')
def step_impl(context):
  context.value["a"] = numpy.arange(10)
  nose.tools.assert_equal(context.value.keys(), ["a"])
  nose.tools.assert_equal(context.value.shape, (10, 1))

  context.value["b"] = numpy.arange(10) ** 2
  nose.tools.assert_equal(context.value.keys(), ["a", "b"])
  nose.tools.assert_equal(context.value.shape, (10, 2))
  numpy.testing.assert_array_equal(context.value["b"], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

  context.value["c"] = numpy.zeros(10)
  nose.tools.assert_equal(context.value.keys(), ["a", "b", "c"])
  nose.tools.assert_equal(context.value.shape, (10, 3))
  numpy.testing.assert_array_equal(context.value["c"], [0] * 10)

@then(u'extracting columns should return a new table')
def step_impl(context):
  value = context.value.columns(["b", "a"])
  nose.tools.assert_equal(value.keys(), ["b", "a"])
  nose.tools.assert_equal(value.shape, (10, 2))

@then(u'deleting columns should change the table')
def step_impl(context):
  del context.value["c"]
  nose.tools.assert_equal(context.value.keys(), ["a", "b"])
  nose.tools.assert_equal(context.value.shape, (10, 2))

@then(u'indexing should return a new table with one row')
def step_impl(context):
  value = context.value[5]
  nose.tools.assert_equal(value.keys(), ["a", "b"])
  nose.tools.assert_equal(value.shape, (1, 2))
  numpy.testing.assert_array_equal(value["a"], [5])

@then(u'slicing should return a new table with a range of rows')
def step_impl(context):
  value = context.value[slice(0, 6, 2)]
  nose.tools.assert_equal(value.keys(), ["a", "b"])
  nose.tools.assert_equal(value.shape, (3, 2))
  numpy.testing.assert_array_equal(value["a"], [0, 2, 4])

@then(u'extracting rows by index should return a new table with one row')
def step_impl(context):
  value = context.value.rows(8)
  nose.tools.assert_equal(value.keys(), ["a", "b"])
  nose.tools.assert_equal(value.shape, (1, 2))
  numpy.testing.assert_array_equal(value["a"], [8])

@then(u'extracting rows using multiple indices should return a new table with the specified rows')
def step_impl(context):
  value = context.value.rows([1, 2, 3])
  nose.tools.assert_equal(value.keys(), ["a", "b"])
  nose.tools.assert_equal(value.shape, (3, 2))
  numpy.testing.assert_array_equal(value["a"], [1, 2, 3])

@then(u'new columns must have a string name')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    context.value[3] = numpy.arange(10)

@then(u'new columns must have the same number of rows as existing columns')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    context.value["c"] = numpy.random.random(4)

@then(u'new columns must be one-dimensional')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    context.value["c"] = numpy.random.random((10, 4))

@when(u'toyplot.data.Table is initialized with nothing')
def step_impl(context):
  context.value = toyplot.data.Table()

@then(u'the toyplot.data.Table is empty')
def step_impl(context):
  nose.tools.assert_equal(len(context.value), 0)
  nose.tools.assert_equal(context.value.shape, (0, 0))
  nose.tools.assert_equal(context.value.items(), [])
  nose.tools.assert_equal(context.value.keys(), [])
  nose.tools.assert_equal(context.value.values(), [])

@when(u'toyplot.data.Table is initialized with an OrderedDict containing columns')
def step_impl(context):
  context.value = collections.OrderedDict([("ones", numpy.ones(10)), ("zeros", numpy.zeros(10))])

@then(u'the toyplot.data.Table contains the columns')
def step_impl(context):
  value = toyplot.data.Table(context.value)
  nose.tools.assert_equal(value.keys(), ["ones", "zeros"])
  numpy.testing.assert_array_equal(value["ones"], [1] * 10)
  numpy.testing.assert_array_equal(value["zeros"], [0] * 10)

@when(u'toyplot.data.Table is initialized with a dict containing columns')
def step_impl(context):
  context.value = {"ones" : numpy.ones(10), "zeros" : numpy.zeros(10)}

@then(u'the toyplot.data.Table raises ValueError')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    toyplot.data.Table(context.value)

@given(u'a toyplot.data.table with some data')
def step_impl(context):
  numpy.random.seed(1234)
  context.value = toyplot.data.Table()
  context.value["foo"] = numpy.arange(10)
  context.value["bar"] = numpy.random.random(10)
  context.value["baz"] = numpy.random.choice(["red", "green", "blue"], size=10)

latex_without_hline = r"""\begin{tabular}{l l l}
foo & bar & baz \\
\hline
0 & 0.192 & blue \\
1 & 0.622 & red \\
2 & 0.438 & red \\
3 & 0.785 & red \\
4 & 0.78 & green \\
5 & 0.273 & red \\
6 & 0.276 & green \\
7 & 0.802 & blue \\
8 & 0.958 & blue \\
9 & 0.876 & blue \\
\end{tabular}
"""

@then(u'the table can be rendered as a latex string')
def step_impl(context):
  nose.tools.assert_equal(toyplot.latex.render(context.value), latex_without_hline)

@then(u'the table can be rendered as a latex fobj')
def step_impl(context):
  buffer = StringIO.StringIO()
  toyplot.latex.render(context.value, buffer)
  nose.tools.assert_equal(buffer.getvalue(), latex_without_hline)

@then(u'the table can be rendered as a latex file')
def step_impl(context):
  path = os.path.join(tempfile.mkdtemp(), "test.tex")
  toyplot.latex.render(context.value, path)
  nose.tools.assert_equal(open(path, "r").read(), latex_without_hline)

latex_with_hline = r"""\begin{tabular}{l l l}
foo & bar & baz \\
\hline
0 & 0.192 & blue \\
1 & 0.622 & red \\
2 & 0.438 & red \\
3 & 0.785 & red \\
4 & 0.78 & green \\
\hline
5 & 0.273 & red \\
6 & 0.276 & green \\
7 & 0.802 & blue \\
8 & 0.958 & blue \\
9 & 0.876 & blue \\
\end{tabular}
"""

@then(u'the table can be rendered as a latex string with hline')
def step_impl(context):
  nose.tools.assert_equal(toyplot.latex.render(context.value, hlines=[5]), latex_with_hline)


