# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import nose.tools

import os
import pkgutil
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
docs_dir = os.path.join(root_dir, "docs")
package_dir = os.path.join(root_dir, "toyplot")

copyright_notice = """# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""

@given(u'all Toyplot sources.')
def step_impl(context):
    context.sources = []
    for directory, subdirectories, filenames in os.walk(root_dir):
        for filename in filenames:
            if os.path.splitext(filename)[1] not in [".py"]:
                continue
            if os.path.basename(directory) == "design" and filename == "decodegraphics.py":
                continue
            if os.path.basename(directory) == "_test":
                continue

            context.sources.append(os.path.join(directory, filename))
    context.sources = sorted(context.sources)

@then(u'every source must contain a copyright notice.')
def step_impl(context):
    for source in context.sources:
        with open(source, "r") as stream:
            if not stream.read().startswith(copyright_notice):
                raise AssertionError("%s missing copyright notice." % source)

@given(u'all public Toyplot modules.')
def step_impl(context):
    def walk_modules(package, path):
        modules = []
        modules.append(package)
        for loader, name, is_package in pkgutil.iter_modules([path]):
            modules += walk_modules(package + "." + name, os.path.join(path, name))
        return modules
    context.modules = sorted(walk_modules("toyplot", package_dir))

@given(u'the Toyplot reference documentation.')
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

@then(u'every module must have a section in the reference documentation.')
def step_impl(context):
    for module in context.modules:
        if os.path.join(docs_dir, module + ".rst") not in context.references:
            raise AssertionError("No matching documentation found for the %s module." % module)

@then(u'every section in the reference documentation must match a module.')
def step_impl(context):
    modules = [os.path.join(docs_dir, module + ".rst") for module in context.modules]
    for reference in context.references:
        if reference not in modules:
            raise AssertionError("No matching module found for %s." % reference)

