# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Generates SVG images.
"""


import xml.etree.ElementTree as xml


import toyplot.html
import toyplot.require


def apply_changes(svg, changes):
    """Modify the SVG DOM representation of a canvas with the given changes."""
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

    canvas = toyplot.require.instance(canvas, toyplot.canvas.Canvas)
    html, html_animation = toyplot.html.render(canvas, animation=True)
    svg = html.find("svg")

    if isinstance(fobj, str):
        with open(fobj, "wb") as stream:
            stream.write(xml.tostring(svg, method="xml"))
    elif fobj is not None:
        fobj.write(xml.tostring(svg, method="xml"))
    else:
        if animation:
            return svg, html_animation
        else:
            return svg
