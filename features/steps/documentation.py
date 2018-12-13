# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import nose.tools

import glob
import logging
import os
import pkgutil
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)
log.name = "features.steps.documentation"

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
        if os.path.basename(directory) in ["js"]:
            continue
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


@given(u'the Toyplot documentation notebooks')
def step_impl(context):
    # Make a list of available notebooks.
    context.notebooks = sorted(glob.glob(os.path.join(docs_dir, "*.ipynb")))


@then(u'every notebook can be converted to a script')
def step_impl(context):
    # Convert notebook paths to script paths.
    context.scripts = [os.path.splitext(notebook)[0] + ".py" for notebook in context.notebooks]
    context.scripts = context.scripts

    # Convert each notebook to a script.
    for notebook, script in zip(context.notebooks, context.scripts):
        command = ["jupyter", "nbconvert", "--to", "python", notebook, "--output", script]
        log.info(" ".join(command))
        subprocess.check_call(command)


@then(u'every notebook script can be run without error')
def step_impl(context):
    # Run each notebook script, keeping track of failures.
    failures = {}
    for notebook, script in zip(context.notebooks, context.scripts):
        try:
            command = ["python", script]
            log.info(" ".join(command))
            subprocess.check_call(command, cwd=docs_dir)
            # Remove the script (we only do this if execution succeeded)
            os.remove(script)
        except Exception as e:
            failures[notebook] = e

    if failures:
        message = ""
        for notebook_path, exception in failures.items():
            message += notebook_path + " exception:\n\n" + exception + "\n\n"
        raise AssertionError(message)

