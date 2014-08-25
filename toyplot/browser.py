# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

def show(canvas, title="Toyplot Figure"):
  """Display a canvas in a web browser.

  Parameters
  ----------
  canvas : :class:`toyplot.Canvas`
    The canvas to be displayed.

  title : string, optional
    Optional page title to be displayed in the browser.

  Notes
  -----
  The output HTML is generated using :func:`toyplot.html.render`.
  """

  import os
  import tempfile
  import toyplot.html
  import xml.etree.ElementTree as xml
  import webbrowser

  figure = toyplot.html.render(canvas)
  html = xml.Element("html")
  head = xml.SubElement(html, "head")
  xml.SubElement(head, "title").text = title
  body = xml.SubElement(html, "body")
  body.append(figure)

  fd, path = tempfile.mkstemp(suffix=".html")
  with os.fdopen(fd, "w") as file:
    file.write(xml.tostring(html, method="html"))
  webbrowser.open("file://" + path, new=1, autoraise=True)
