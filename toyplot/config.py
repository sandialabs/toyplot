# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Provides global configuration for toyplot figures."""

from __future__ import division
import os

autorender = True
autoformat = os.environ.get("TOYPLOT_AUTOFORMAT", "html")

