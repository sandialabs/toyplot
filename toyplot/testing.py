# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import io
import os
import numpy.testing

root_dir = os.path.dirname(os.path.dirname(__file__))
failed_dir = os.path.join(root_dir, "features", "failed")
reference_dir = os.path.join(root_dir, "features", "reference")

def _assert_content_equal(content, test_file, reference_file):
  if os.path.exists(test_file):
    os.remove(test_file)
  if os.path.exists(reference_file):
    reference_html = open(reference_file, "rb").read()
    if content != reference_html:
      if not os.path.exists(failed_dir):
        os.mkdir(failed_dir)
      with open(test_file, "wb") as file:
        file.write(content)
      raise AssertionError("Test output %s doesn't match %s." % (test_file, reference_file))
  else:
    with open(reference_file, "wb") as file:
      file.write(content)
    raise AssertionError("Created new reference file %s.  You should verify its contents before re-running the test." % (reference_file))

def assert_color_equal(a, b):
  """Raise an exception if a toyplot color doesn't match a reference.

  Parameters
  ----------
  a: toyplot RGBA color, required
  b: 4-tuple
  """
  if a is None and b is None:
    return
  numpy.testing.assert_array_almost_equal((a["r"], a["g"], a["b"], a["a"]), b)

def assert_html_equal(html, name):
  """Raise an exception if HTML content doesn't match a reference.

  Parameters
  ----------
  html: string, required
    The HTML content to be compared.
  name: string, required
    Unique identifier of the reference file to use as a comparison.
    The reference file will be located at toyplot/features/reference/<name>.html
  """
  test_file = os.path.join(failed_dir, "%s.html" % name)
  reference_file = os.path.join(reference_dir, "%s.html" % name)
  _assert_content_equal(html, test_file, reference_file)

def assert_latex_equal(latex, name):
  """Raise an exception if LaTeX content doesn't match a reference.

  Parameters
  ----------
  latex: string, required
    The LaTeX content to be compared.
  name: string, required
    Unique identifier of the reference file to use as a comparison.
    The reference file will be located at toyplot/features/reference/<name>.tex
  """

  test_file = os.path.join(failed_dir, "%s.tex" % name)
  reference_file = os.path.join(reference_dir, "%s.tex" % name)
  _assert_content_equal(latex, test_file, reference_file)
