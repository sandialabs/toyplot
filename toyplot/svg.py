# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import toyplot.html
import toyplot.compatibility
import xml.etree.ElementTree as xml


def apply_changes(svg, changes):
    toyplot.html.apply_changes(svg, changes)


def render(canvas, fobj=None, animation=False):
    """Render the SVG representation of a canvas.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      The canvas to be rendered.

    fobj: file-like object or string, optional
      The file to write.  Use a string filepath to write data directly to disk.
      If `None` (the default), the SVG tree will be returned to the caller
      instead.

    animation: boolean, optional
      If `True`, return a representation of the changes to be made to the SVG
      tree for animation.

    Returns
    -------
    svg: xml.etree.ElementTree.Element or `None`
      SVG representation of `canvas`, as a DOM tree, or `None` if the caller
      specifies the `fobj` parameter.

    changes: JSON-compatible data structure, or `None`
      JSON-compatible representation of the animated changes to `canvas`.
    """

    html, html_animation = toyplot.html.render(canvas, animation=True)
    svg = html.find("svg")

    if isinstance(fobj, toyplot.compatibility.string_type):
        with open(fobj, "wb") as file:
            file.write(xml.tostring(svg, method="xml"))
    elif fobj is not None:
        fobj.write(xml.tostring(svg, method="xml"))
    else:
        if animation:
            return svg, html_animation
        else:
            return svg
