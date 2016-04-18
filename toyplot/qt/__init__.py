# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

# Note: we prefer PyQt5 only because we've had issues embedding our HTML output
# with specific versions (Qt 4.8.7 on a Mac) of QWebView.  Otherwise, the
# functionality is equivalent.

"""Support functions for rendering using Qt.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import *

import numpy
import sys
import toyplot.html
import toyplot.require
import xml.etree.ElementTree as xml

def application():
    """Return a singleton QApplication instance.

    If an instance of :class:`QApplication` has already been created, returns
    it.  Otherwise, an instance of QApplication is created and returned.

    Returns
    -------
    qapplication: :class:`QApplication`
        The Qt global singleton application object.
    """

    if application.instance is None:
        application.instance = QApplication.instance()
        if application.instance is None:
            application.instance = QApplication(sys.argv)
    return application.instance
application.instance = None

def show(canvas, title="Toyplot Figure"):
    """Display a canvas in a Qt window.

    Displays a Toyplot canvas in a popup Qt window, using Toyplot's preferred
    interactive HTML+SVG+Javascript backend.

    Note: this function blocks until the user closes the figure window.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      The canvas to be displayed.

    title: string, optional
      Optional page title to be displayed in the window.
    """

    canvas = toyplot.require.instance(canvas, toyplot.canvas.Canvas)

    qapplication = application()

    window = QWebView()
    window.windowTitle = title
    window.setHtml(xml.tostring(toyplot.html.render(canvas), method="html"))
    window.show()

    qapplication.exec_()
