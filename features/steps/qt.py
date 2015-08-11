from behave import *

import mock
import nose.tools
import numpy
import toyplot.qt

import PyQt5.QtWidgets


@given(u'a sample Toyplot canvas, the canvas can be displayed in a Qt window')
def step_impl(context):
    canvas, axes, mark = toyplot.plot(numpy.linspace(0, 1) ** 2)
    with mock.patch("PyQt5.QtWidgets.QApplication.exec_") as qapplication_exec:
        toyplot.qt.show(canvas)
    nose.tools.assert_equal(qapplication_exec.call_count, 1)

