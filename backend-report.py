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
    "toyplot.cairo",
    "toyplot.cairo.eps",
    "toyplot.cairo.png",
    "toyplot.html",
    "toyplot.mp4",
    "toyplot.pdf",
    "toyplot.png",
    "toyplot.qt",
    "toyplot.qt.png",
    "toyplot.reportlab",
    "toyplot.reportlab.pdf",
    "toyplot.reportlab.png",
    "toyplot.svg",
    "toyplot.webm",
    ]:
    print_report(module)
