# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for displaying a Toyplot canvas in a web browser."""


import collections

def show(canvases, title="Toyplot Figure"):
    """Display one or more canvases in a web browser.

    Uses Toyplot's preferred HTML+SVG+Javascript backend to display one-or-more
    interactive canvases in a web browser window.

    Because the canvases are displayed in a separate web browser process, this
    function returns immediately.

    Parameters
    ----------
    canvases: :class:`toyplot.canvas.Canvas` instance or sequence of :class:`toyplot.canvas.Canvas` instances.
      The canvases to be displayed.

    title: string, optional
      Optional page title to be displayed by the browser.
    """

    import os
    import tempfile
    import toyplot.canvas
    import toyplot.html
    import xml.etree.ElementTree as xml
    import webbrowser

    if not isinstance(canvases, (toyplot.canvas.Canvas, collections.abc.Iterable)):
        raise ValueError("Expected one or more instances of %s, received %s." % (toyplot.canvas.Canvas, type(canvases))) # pragma: no cover

    if isinstance(canvases, toyplot.canvas.Canvas):
        canvases = [canvases]

    html = xml.Element("html")
    head = xml.SubElement(html, "head")
    xml.SubElement(head, "title").text = title
    body = xml.SubElement(html, "body")
    for canvas in canvases:
        body.append(toyplot.html.render(canvas))

    fd, path = tempfile.mkstemp(suffix=".html")
    with os.fdopen(fd, "wb") as stream:
        stream.write(xml.tostring(html, method="html"))
    webbrowser.open("file://" + path, new=1, autoraise=True)
