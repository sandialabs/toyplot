# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import nose.tools

import os
import pkgutil
import subprocess
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

@given(u'pylint')
def step_impl(context):
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, "pylint")):
            context.pylint = os.path.join(path, "pylint")
            return
    context.scenario.skip(reason="The pylint command is not available.")

@then(u'all pylint tests must pass without any messages.')
def step_impl(context):
    command = [context.pylint, package_dir]
    pylint = subprocess.check_call(command)


