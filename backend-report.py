# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import importlib
import logging
import sys

logging.basicConfig()

def print_report(module):
    try:
        sys.stdout.write("Loading %s ... " % module)
        importlib.import_module(module)
        sys.stdout.write("ok\n")
    except Exception as e:
        sys.stdout.write("failed\n")
        sys.stdout.write("  %s\n" % e)


for module in [
    "toyplot.browser",
    "toyplot.html",
    "toyplot.mp4",
    "toyplot.pdf",
    "toyplot.png",
    "toyplot.reportlab",
    "toyplot.reportlab.pdf",
    "toyplot.reportlab.png",
    "toyplot.svg",
    ]:
    print_report(module)
