import importlib
import sys
import traceback

def print_report(module):
    try:
        sys.stdout.write("Loading %s ... " % module)
        importlib.import_module(module)
        sys.stdout.write("ok\n")
    except Exception as e:
        sys.stdout.write("failed\n\n")
        traceback.print_exc()
        sys.stdout.write("%s\n\n" % e)


for module in [
    "toyplot.browser",
    "toyplot.cairo",
    "toyplot.cairo.eps",
    "toyplot.cairo.pdf",
    "toyplot.cairo.png",
    "toyplot.html",
    "toyplot.mp4",
    "toyplot.pdf",
    "toyplot.png",
    "toyplot.qt",
    "toyplot.qt.pdf",
    "toyplot.qt.png",
    "toyplot.reportlab.pdf",
    "toyplot.svg",
    "toyplot.webm",
    ]:
    print_report(module)
