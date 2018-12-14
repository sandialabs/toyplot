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

import IPython
import IPython.core.interactiveshell
import nbformat

import toyplot

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
    context.notebooks = sorted(glob.glob(os.path.join(docs_dir, "*.ipynb")))


@then(u'every notebook runs without error')
def step_impl(context):
    sys.path.append(docs_dir)
    cwd = os.getcwd()
    os.chdir(docs_dir)
    for notebook in context.notebooks:
        context.execute_steps(u"Then notebook %s runs without error" % notebook)
    os.chdir(cwd)
    sys.path.remove(docs_dir)


@then(u'notebook {notebook} runs without error')
def step_impl(context, notebook):
    log.info(notebook)

    with open(notebook) as stream:
        notebook = nbformat.read(stream, as_version=4)

    shell = IPython.core.interactiveshell.InteractiveShell.instance()
    nblocals = dict()

    for cell in notebook.cells:
        if cell.cell_type == "code":
            code = shell.input_transformer_manager.transform_cell(cell.source)
            exec(code, nblocals)
            toyplot.Canvas._ipython_post_execute()

#    # Run each notebook script, keeping track of failures.
#    failures = {}
#    for notebook, script in zip(context.notebooks, context.scripts):
#        try:
#            command = ["coverage", "run", "--source", "toyplot", "--append", script]
#            log.info(" ".join(command))
#            subprocess.check_call(command, cwd=docs_dir)
#            # Remove the script (we only do this if execution succeeded)
#            os.remove(script)
#        except Exception as e:
#            failures[notebook] = e
#
#    if failures:
#        message = ""
#        for notebook_path, exception in failures.items():
#            message += notebook_path + " exception:\n\n" + exception + "\n\n"
#        raise AssertionError(message)

