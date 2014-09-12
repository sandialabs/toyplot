# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import numpy
import toyplot.data

def render(table, fobj=None):
  """Render the LaTeX representation of a table.

  Parameters
  ----------
  table: :class:`toyplot.data.Table`
    The table to be rendered.

  fobj: file-like object or string, optional
    The file to write.  Use a string filepath to write data directly to disk.
    If `None` (the default), the LaTeX markup will be returned to the caller
    instead.

  Returns
  -------
  latex: string or `None`
    LaTeX representation of `table`, as a string, or `None` if the caller
    specifies the `fobj` parameter.
  """
  table = toyplot._require_instance(table, toyplot.data.Table)

  # Setup formatters for each column.
  formatters = []
  for column in table.values():
    if column.dtype.kind == "f":
      formatters.append("{:.3g}".format)
    else:
      formatters.append(str)

  # Setup iterators for each column.
  iterators = [iter(column) for column in table.values()]

  latex = "\\begin{tabular}"
  latex += "{" + " ".join(["l" for key in table.keys()]) + "}\n"
  latex += " & ".join(table.keys()) + " \\\\\n"
  latex += "\\hline\n"

  try:
    while True:
      for index, (iterator, formatter) in enumerate(zip(iterators, formatters)):
        value = iterator.next()
        if index != 0:
          latex += " & "
        latex += formatter(value)
      latex += " \\\\\n"
  except StopIteration:
    pass

  latex += "\\end{tabular}\n"

  if isinstance(fobj, toyplot.string_type):
    with open(fobj, "wb") as file:
      file.write(latex)
  elif fobj is not None:
    fobj.write(latex)
  else:
    return latex

