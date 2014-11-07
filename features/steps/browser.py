from behave import *

import mock
import nose.tools
import numpy
import toyplot.browser
import toyplot.testing
import webbrowser

@given(u'a sample Toyplot canvas')
def step_impl(context):
  context.canvas, axes, mark = toyplot.plot(numpy.sin(numpy.linspace(0, 10)))

@then(u'the canvas can be displayed in a web browser')
def step_impl(context):
  with mock.patch("webbrowser.open") as webbrowser_open:
    toyplot.browser.show(context.canvas)
  nose.tools.assert_equal(webbrowser_open.call_count, 1)
  nose.tools.assert_true(webbrowser_open.call_args[0][0].startswith("file://"))
  nose.tools.assert_equal(webbrowser_open.call_args[1]["new"], 1)
  nose.tools.assert_equal(webbrowser_open.call_args[1]["autoraise"], True)
