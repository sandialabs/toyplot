from behave import *

import mock
import nose.tools
import numpy
import sys
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

@then(u'the canvas can be displayed in a web browser using selenium')
def step_impl(context):
  selenium = mock.Mock()
  selenium_webdriver = mock.Mock()

  sys.modules["selenium"] = selenium
  sys.modules["selenium.webdriver"] = selenium_webdriver

  import toyplot.selenium
  toyplot.selenium.show(context.canvas)

  nose.tools.assert_equal(selenium.mock_calls[0], ("webdriver.Firefox", (), {}))
  nose.tools.assert_equal(selenium.mock_calls[1], ("webdriver.Firefox().set_window_size", (900.0, 900.0), {}))
  nose.tools.assert_equal(selenium.mock_calls[2][0], "webdriver.Firefox().get")
  nose.tools.assert_true(selenium.mock_calls[2][1][0], "file://")

