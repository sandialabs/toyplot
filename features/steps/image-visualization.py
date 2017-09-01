# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import os

import nose.tools
import numpy
import PIL.Image
import toyplot.color

import testing


art_dir = os.path.abspath(os.path.dirname(__file__))


@given(u'a numpy 1 bit L image')
def step_impl(context):
    context.image = testing.read_png(os.path.join(art_dir, "toyplot-8-L.png"))
    context.image = context.image > 128
    nose.tools.assert_equal(context.image.shape, (256, 256, 1))
    nose.tools.assert_equal(context.image.dtype, "bool")


@given(u'a numpy 8 bit L image')
def step_impl(context):
    context.image = testing.read_png(os.path.join(art_dir, "toyplot-8-L.png"))
    nose.tools.assert_equal(context.image.shape, (256, 256, 1))
    nose.tools.assert_equal(context.image.dtype, "uint8")


@given(u'a numpy 8 bit L image with colormap')
def step_impl(context):
    context.image = testing.read_png(os.path.join(art_dir, "toyplot-8-L.png"))
    nose.tools.assert_equal(context.image.shape, (256, 256, 1))
    nose.tools.assert_equal(context.image.dtype, "uint8")
    context.image = (context.image, toyplot.color.brewer.map("BlueRed"))


@given(u'a numpy 8 bit LA image')
def step_impl(context):
    context.image = testing.read_png(os.path.join(art_dir, "toyplot-8-LA.png"))
    nose.tools.assert_equal(context.image.shape, (256, 256, 2))
    nose.tools.assert_equal(context.image.dtype, "uint8")


@given(u'a numpy 8 bit RGB image')
def step_impl(context):
    context.image = testing.read_png(os.path.join(art_dir, "toyplot-8-RGB.png"))
    nose.tools.assert_equal(context.image.shape, (256, 256, 3))
    nose.tools.assert_equal(context.image.dtype, "uint8")


@given(u'a numpy 8 bit RGBA image')
def step_impl(context):
    context.image = testing.read_png(os.path.join(art_dir, "toyplot-8-RGBA.png"))
    nose.tools.assert_equal(context.image.shape, (256, 256, 4))
    nose.tools.assert_equal(context.image.dtype, "uint8")


@given(u'a pillow 8 bit L image')
def step_impl(context):
    context.image = PIL.Image.open(os.path.join(art_dir, "toyplot-8-L.png"))
    nose.tools.assert_equal(context.image.size, (256, 256))
    nose.tools.assert_equal(context.image.mode, "L")


@given(u'a pillow 8 bit L image with colormap')
def step_impl(context):
    context.image = PIL.Image.open(os.path.join(art_dir, "toyplot-8-L.png"))
    nose.tools.assert_equal(context.image.size, (256, 256))
    nose.tools.assert_equal(context.image.mode, "L")
    context.image = (context.image, toyplot.color.brewer.map("BlueRed"))


@given(u'a pillow 8 bit RGB image')
def step_impl(context):
    context.image = PIL.Image.open(os.path.join(art_dir, "toyplot-8-RGB.png"))
    nose.tools.assert_equal(context.image.size, (256, 256))
    nose.tools.assert_equal(context.image.mode, "RGB")


@given(u'a pillow 8 bit RGBA image')
def step_impl(context):
    context.image = PIL.Image.open(os.path.join(art_dir, "toyplot-8-RGBA.png"))
    nose.tools.assert_equal(context.image.size, (256, 256))
    nose.tools.assert_equal(context.image.mode, "RGBA")


@given(u'a non-square numpy 8 bit L image')
def step_impl(context):
    numpy.random.seed(1234)
    context.image = numpy.random.uniform(0, 1, size=(10, 5)).repeat(50, axis=0).repeat(50, axis=1)
    nose.tools.assert_equal(context.image.shape, (500, 250))
    nose.tools.assert_equal(context.image.dtype, "float64")


@given(u'a non-square numpy 8 bit L image with colormap')
def step_impl(context):
    numpy.random.seed(1234)
    context.image = numpy.random.uniform(0, 1, size=(10, 5)).repeat(50, axis=0).repeat(50, axis=1)
    nose.tools.assert_equal(context.image.shape, (500, 250))
    nose.tools.assert_equal(context.image.dtype, "float64")
    context.image = (context.image, toyplot.color.linear.map("Blackbody"))


@given(u'a canvas background color')
def step_impl(context):
    context.canvas.style = {"background-color":"lightgray"}


@when(u'the image is added to the canvas')
def step_impl(context):
    context.canvas.image(context.image)


