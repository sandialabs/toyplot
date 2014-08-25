# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import absolute_import

def show(canvas, title="Toyplot Figure"):
  """Display a canvas in a web browser.

  Parameters
  ----------
  canvas : :class:`toyplot.Canvas`
    The canvas to be displayed.

  title : string, optional
    Optional page title to be displayed in the browser.

  Returns
  -------
  browser : selenium webdriver object that can be used to control the browser.

  Notes
  -----
  The output HTML is generated using :func:`toyplot.html.render`.
  """

  import os
  import selenium.webdriver
  import tempfile
  import toyplot.html
  import xml.etree.ElementTree as xml

  figure = toyplot.html.render(canvas)
  html = xml.Element("html")
  head = xml.SubElement(html, "head")
  xml.SubElement(head, "title").text = title
  body = xml.SubElement(html, "body")
  body.append(figure)

  fd, path = tempfile.mkstemp(suffix=".html")
  with os.fdopen(fd, "w") as file:
    file.write(xml.tostring(html, method="html"))

  browser = selenium.webdriver.Firefox()
  browser.set_window_size(canvas._width * 1.5, canvas._height * 1.5)
  browser.get("file://" + path)

  return browser
