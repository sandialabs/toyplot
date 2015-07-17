# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import argparse
import os
import re
import shutil
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--clean", action="store_true", help="Force a clean rebuild of the documentation.")
arguments = parser.parse_args()

root_dir = os.path.abspath(os.path.join(__file__, "..", ".."))
docs_dir = os.path.join(root_dir, "docs")
build_dir = os.path.join(docs_dir, "_build")

def convert_notebook(name):
  # Convert the notebook into restructured text suitable for the documentation.
  source = os.path.join(docs_dir, "%s.ipynb" % name)
  target = os.path.join(docs_dir, "%s.rst" % name)

  if os.path.exists(target) and os.path.getmtime(target) >= os.path.getmtime(source) and not arguments.clean:
    return

  subprocess.check_call(["ipython", "nbconvert", "--execute", "--to", "rst", source, "--output", os.path.join(docs_dir, name)])

  # Unmangle Sphinx cross-references in the tutorial that get mangled by markdown.
  with open(target, "r") as file:
    content = file.read()
    content = re.sub(":([^:]+):``([^`]+)``", ":\\1:`\\2`", content)
    content = re.sub("[.][.].*(_[^:]+):", ".. \\1:", content)

    content = """
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  """ + content

  with open(target, "w") as file:
    file.write(content)

# Always build the documentation from scratch.
if os.path.exists(build_dir):
  shutil.rmtree(build_dir)

for name in ["canvas-layout", "cartesian-axes", "color", "convenience", "data-tables", "labels-and-legends", "markers", "matrix-visualization", "rendering", "table-axes", "text", "tick-locators", "tutorial", "units"]:
  convert_notebook(name)

# Generate the HTML documentation.
subprocess.check_call(["make", "html"], cwd=docs_dir)
