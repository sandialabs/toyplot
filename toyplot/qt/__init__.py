# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

# Note: we prefer PyQt5 only because we've had issues embedding our HTML output
# with specific versions (Qt 4.8.7 on a Mac) of QWebView.  Otherwise, the
# functionality is equivalent.

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import *

import numpy
import sys
import toyplot.html
import xml.etree.ElementTree as xml

def application():
    if application.instance is None:
        application.instance = QApplication.instance()
        if application.instance is None:
            application.instance = QApplication(sys.argv)
    return application.instance
application.instance = None

def show(canvas, title="Toyplot Figure"):
    """Display a canvas in a Qt window.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      The canvas to be displayed.

    title: string, optional
      Optional page title to be displayed in the window.

    Notes
    -----
    The output HTML is generated using :func:`toyplot.html.render`.
    """

    qapplication = application()

    window = QWebView()
    window.windowTitle = title
    window.setHtml(xml.tostring(toyplot.html.render(canvas), method="html"))
    window.show()

    qapplication.exec_()
