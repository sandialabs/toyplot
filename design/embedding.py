from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtNetwork import *
from PySide.QtWebKit import *

import numpy
import os
import sys
import toyplot.png

application = QApplication(sys.argv)

canvas, axes, mark = toyplot.plot(numpy.linspace(0, 1) ** 2)

window = QWebView()
window.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
#window.setHtml(canvas._repr_html_())
window.setContent(toyplot.png.render(canvas), "image/png")
window.show()

application.exec_()
