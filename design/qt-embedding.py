# Note: we prefer PyQt5 only because we've had issues embedding our HTML output
# with specific versions (Qt 4.8.7 on a Mac) of QWebView.  Otherwise, the
# functionality is equivalent.

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtWebKitWidgets import *
except:
    from PySide.QtGui import *
    from PySide.QtWebKit import *

import numpy
import sys
import toyplot.html
import toyplot.png
import toyplot.svg
import xml.etree.ElementTree as xml

application = QApplication(sys.argv)
window = QWebView()

canvas, axes, mark = toyplot.plot(numpy.linspace(0, 1) ** 2)

# Embed Toyplot HTML output in a QWebView.  This is the best option because it
# retains figure interaction.
window.setHtml(xml.tostring(toyplot.html.render(canvas), method="html"))

# Embed Toyplot SVG in a QWebView.  This retains the figure quality, but no
# interaction.
#window.setContent(xml.tostring(toyplot.svg.render(canvas)), "image/svg+xml")

# Embed Toyplot PNG in a QWebView.  This requires additional Python
# dependencies, doesn't scale cleanly, and has no interaction.
#window.setContent(toyplot.png.render(canvas), "image/png")

#window.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
window.show()
application.exec_()
