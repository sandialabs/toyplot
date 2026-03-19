# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import unittest.mock
import xml.etree.ElementTree as xml

import test
import toyplot.reportlab


@given(u'an SVG path with move, line, cubic, and close commands')
def step_impl(context):
    context.svg = xml.Element(
        "svg",
        width="10px",
        height="10px",
        style="border-style:none",
        )
    xml.SubElement(
        context.svg,
        "path",
        d="M 0 0 L 1 1 C 2 3 4 5 6 7 Z",
        style="fill:none;stroke:black;stroke-width:1",
        )


@when(u'the SVG path is rendered with the ReportLab backend')
def step_impl(context):
    context.path = unittest.mock.Mock()
    context.canvas = unittest.mock.Mock()
    context.canvas.beginPath.return_value = context.path
    toyplot.reportlab.render(context.svg, context.canvas)


@then(u'the ReportLab path should receive the expected drawing commands')
def step_impl(context):
    test.assert_equal(context.canvas.beginPath.call_count, 1)
    test.assert_sequence_equal(
        context.path.moveTo.call_args_list,
        [unittest.mock.call(0.0, 0.0)],
        )
    test.assert_sequence_equal(
        context.path.lineTo.call_args_list,
        [unittest.mock.call(1.0, 1.0)],
        )
    test.assert_sequence_equal(
        context.path.curveTo.call_args_list,
        [unittest.mock.call(2.0, 3.0, 4.0, 5.0, 6.0, 7.0)],
        )
    test.assert_equal(context.path.close.call_count, 1)
    test.assert_sequence_equal(
        context.canvas.drawPath.call_args_list,
        [unittest.mock.call(context.path)],
        )
