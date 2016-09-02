# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import nose.tools

import os
import pkgutil
import subprocess
import sys

import toyplot.docs

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
docs_dir = os.path.join(root_dir, "docs")
package_dir = os.path.join(root_dir, "toyplot")

@given(u'all public Toyplot modules')
def step_impl(context):
    def walk_modules(package, path):
        modules = []
        modules.append(package)
        for loader, name, is_package in pkgutil.iter_modules([path]):
            modules += walk_modules(package + "." + name, os.path.join(path, name))
        return modules
    context.modules = sorted(walk_modules("toyplot", package_dir))

@given(u'the Toyplot reference documentation')
def step_impl(context):
    context.references = []
    for directory, subdirectories, filenames in os.walk(docs_dir):
        for filename in filenames:
            if os.path.splitext(filename)[1] not in [".rst"]:
                continue
            if not filename.startswith("toyplot."):
                continue

            context.references.append(os.path.join(directory, filename))
    context.references = sorted(context.references)

@then(u'every module must have a section in the reference documentation')
def step_impl(context):
    for module in context.modules:
        if os.path.join(docs_dir, module + ".rst") not in context.references:
            raise AssertionError("No matching documentation found for the %s module." % module)

@then(u'every section in the reference documentation must match a module')
def step_impl(context):
    modules = [os.path.join(docs_dir, module + ".rst") for module in context.modules]
    for reference in context.references:
        if reference not in modules:
            raise AssertionError("No matching module found for %s." % reference)

@given(u'a collection of linear color maps')
def step_impl(context):
    context.color_maps = toyplot.color.linear.maps()

@then(u'the color maps can be rendered as luma plots')
def step_impl(context):
    context.canvas = toyplot.docs.plot_luma(context.color_maps)

