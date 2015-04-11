# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import os
import re
import shutil
import subprocess

root_dir = os.path.abspath(os.path.join(__file__, "..", ".."))
docs_dir = os.path.join(root_dir, "docs")

def convert_notebook(name):
  # Convert the notebook into restructured text suitable for the documentation.
  subprocess.check_call(["ipython", "nbconvert", "--to", "rst", os.path.join(docs_dir, "%s.ipynb" % name), "--output", os.path.join(docs_dir, name)])

  # Unmangle Sphinx cross-references in the tutorial that get mangled by markdown.
  with open(os.path.join(docs_dir, "%s.rst" % name), "r") as file:
    content = file.read()
    content = re.sub(":([^:]+):``([^`]+)``", ":\\1:`\\2`", content)
    content = re.sub("[.][.].*(_[^:]+):", ".. \\1:", content)

    content = """
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  """ + content

  with open(os.path.join(docs_dir, "%s.rst" % name), "w") as file:
    file.write(content)

# Always build the documentation from scratch.
build_dir = os.path.join(docs_dir, "_build")
if os.path.exists(build_dir):
  shutil.rmtree(build_dir)

for name in ["axes", "color", "data-tables", "markers", "rendering", "table-axes", "text", "tutorial", "units"]:
  convert_notebook(name)

# Generate the HTML documentation.
subprocess.check_call(["make", "html"], cwd=docs_dir)
