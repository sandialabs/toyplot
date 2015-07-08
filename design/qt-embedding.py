from PySide.QtGui import *
from PySide.QtWebKit import *

import numpy
import sys
import toyplot.html, toyplot.png, toyplot.svg
import xml.etree.ElementTree as xml

application = QApplication(sys.argv)
window = QWebView()

canvas, axes, mark = toyplot.plot(numpy.linspace(0, 1) ** 2)
# Embed SVG in the QWebView - this works.
window.setContent(xml.tostring(toyplot.svg.render(canvas)), "image/svg+xml")
# Embed PNG in the QWebView - this works.
#window.setContent(toyplot.png.render(canvas), "image/png")
# Embed HTML in the QWebView - for unknown reasons, this doesn't work for me.
#window.setHtml(xml.tostring(toyplot.html.render(canvas), method="html"))

window.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
window.show()
application.exec_()
