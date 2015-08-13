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


for module in ["toyplot.cairo", "toyplot.cairo.eps", "toyplot.cairo.pdf", "toyplot.cairo.png", "toyplot.qt", "toyplot.qt.pdf", "toyplot.qt.png"]:
    print_report(module)
