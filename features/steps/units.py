# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import test

import toyplot.units


@when(
    u'converting "0" without default units to points the response should be 0.0')
def step_impl(context):
    test.assert_equal(toyplot.units.convert("0", "pt"), 0.0)


@when(
    u'converting 0 without default units to points the response should be 0.0')
def step_impl(context):
    test.assert_equal(toyplot.units.convert(0, "pt"), 0.0)


@when(
    u'converting 72 without default units to points the response should be raise ValueError')
def step_impl(context):
    with test.assert_raises(ValueError):
        toyplot.units.convert(72, "pt")


@when(u'converting 72 with default units pt to in the response should be 1.0')
def step_impl(context):
    test.assert_equal(toyplot.units.convert(72, "in", default="pt"), 1.0)


@when(u'converting "72pt" to in the response should be 1.0')
def step_impl(context):
    test.assert_equal(toyplot.units.convert("72pt", "in"), 1.0)


@when(u'converting (72, "pt") to in the response should be 1.0')
def step_impl(context):
    test.assert_equal(toyplot.units.convert((72, "pt"), "in"), 1.0)


@when(
    u'converting "100%" without reference to in the response should be raise ValueError')
def step_impl(context):
    with test.assert_raises(ValueError):
        toyplot.units.convert("100%", "in")


@when(u'converting "100%" with reference 1.0 to in the response should be 1.0')
def step_impl(context):
    test.assert_equal(
        toyplot.units.convert("100%", "in", reference=1.0), 1.0)


@when(u'converting "40%" with reference 1.0 to in the response should be 0.4')
def step_impl(context):
    test.assert_equal(
        toyplot.units.convert("40%", "in", reference=1.0), 0.4)


@when(u'converting "96px" to in the response should be 1.0')
def step_impl(context):
    test.assert_equal(toyplot.units.convert("96px", "in"), 1.0)


@when(u'converting "96px" to pt the response should be 72.0')
def step_impl(context):
    test.assert_equal(toyplot.units.convert("96px", "pt"), 72.0)


@when(u'converting ".5in" to pt the response should be 36.0')
def step_impl(context):
    test.assert_equal(toyplot.units.convert(".5in", "pt"), 36.0)


@when(u'converting "1in" to cm the response should be 2.54')
def step_impl(context):
    test.assert_almost_equal(toyplot.units.convert("1in", "cm"), 2.54)


@when(u'converting "1furlong" to in the response should be raise ValueError')
def step_impl(context):
    with test.assert_raises(ValueError):
        toyplot.units.convert("1furlong", "in")

@when(u'converting ("72pt",) to in the response should be raise ValueError')
def step_impl(context):
    with test.assert_raises(ValueError):
        toyplot.units.convert(("72pt",), "in")

@when(u'converting "1in" to furlong the response should be raise ValueError')
def step_impl(context):
    with test.assert_raises(ValueError):
        toyplot.units.convert("1in", "furlong")

@when(u'converting [] to in the response should be raise ValueError')
def step_impl(context):
    with test.assert_raises(ValueError):
        toyplot.units.convert([], "in")

@when(u'converting ("1","cm") to in the response should be raise ValueError')
def step_impl(context):
    with test.assert_raises(ValueError):
        toyplot.units.convert(("1", "cm"), "in")

@when(u'converting (1,2) to in the response should be raise ValueError')
def step_impl(context):
    with test.assert_raises(ValueError):
        toyplot.units.convert((1, 2), "in")

