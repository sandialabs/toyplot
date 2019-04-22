# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Provides global configuration for Toyplot figures.

You can write to the attributes in :mod:`toyplot.config` if you wish to change
the default behaviors for multiple figures.
"""

import os

autorender = True
"""Default value for the :class:`toyplot.canvas.Canvas` autorender feature."""

autoformat = os.environ.get("TOYPLOT_AUTOFORMAT", "html")
"""Default value for the :class:`toyplot.canvas.Canvas` autoformat feature."""

width = None
"""Default value for the :class:`toyplot.canvas.Canvas` width."""

height = None
"""Default value for the :class:`toyplot.canvas.Canvas` height."""
