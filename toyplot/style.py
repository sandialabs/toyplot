# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for working with CSS style information."""

from __future__ import division

def combine(*styles):
    """Combine multiple style specifications into one.

    Parameters
    ----------
    styles: sequence of :class:`dict` instances
        A collection of dicts containing CSS-compatible name-value pairs.

    Returns
    -------
    styles: :class:`dict` containing CSS-compatible name-value pairs.
    """
    computed_style = {}
    for style in styles:
        if style is not None:
            computed_style.update(style)
    return computed_style
