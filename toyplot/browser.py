# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for displaying a Toyplot canvas in a web browser."""

from __future__ import division

def show(canvas, title="Toyplot Figure"):
    """Display a canvas in a web browser.

    Uses Toyplot's preferred HTML+SVG+Javascript backend to display an
    interactive canvas in a web browser window.

    Because the canvas is displayed in a separate web browser process,
    this function returns immediately.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      The canvas to be displayed.

    title: string, optional
      Optional page title to be displayed by the browser.
    """

    import os
    import tempfile
    import toyplot.html
    import xml.etree.ElementTree as xml
    import webbrowser

    html = xml.Element("html")
    head = xml.SubElement(html, "head")
    xml.SubElement(head, "title").text = title
    body = xml.SubElement(html, "body")
    body.append(toyplot.html.render(canvas))

    fd, path = tempfile.mkstemp(suffix=".html")
    with os.fdopen(fd, "wb") as stream:
        stream.write(xml.tostring(html, method="html"))
    webbrowser.open("file://" + path, new=1, autoraise=True)
