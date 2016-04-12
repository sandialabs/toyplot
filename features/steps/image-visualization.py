# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import os
import skimage.io
import toyplot

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
art_dir = os.path.join(root_dir, "artwork")

@given(u'a 1 bit L image')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a 1 bit L image')

@given(u'an 8 bit L image')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an 8 bit L image')

@given(u'an 8 bit RGB image')
def step_impl(context):
    context.image = skimage.io.imread(os.path.join(art_dir, "toyplot-small.png"))[:,:,:3]
    assert(context.image.shape == (256, 256, 3))

@given(u'an 8 bit RGBA image')
def step_impl(context):
    context.image = skimage.io.imread(os.path.join(art_dir, "toyplot-small.png"))
    assert(context.image.shape == (256, 256, 4))

@when(u'the image is added to the canvas')
def step_impl(context):
    context.canvas.image(context.image)


