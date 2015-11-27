.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _dependencies:

Dependencies
============

Required
--------

To use Toyplot you'll need the following (if you install Toyplot using pip,
these are automatically installed for you):


* Python 2.7 / Python 3 - http://python.org
* colormath - https://github.com/gtaylor/python-colormath
* multipledispatch - https://github.com/mrocklin/multipledispatch
* numpy - http://numpy.org

PDF Export
----------

To generate static PDF versions of your Toyplot figures, the following is
required (if you install Toyplot using pip, it's automatically installed for
you):

* ReportLab - open source PDF toolkit - http://www.reportlab.com/opensource/

PNG Export
----------

To generate static PNG versions of your Toyplot figures,
you'll need the above dependency to generate PDF files, plus Ghostscript:

* Ghostscript - http://www.ghostscript.com

MP4 / WebM Export
-----------------

If you plan to render animated Toyplot figures as MP4 or WebM videos, you'll need
the above dependencies for exporting PNG files, plus ffmpeg:

* ffmpeg - https://www.ffmpeg.org

Qt Interactive Display
----------------------

If you want to display interactive Toyplot figures in a window implemented with
the Qt graphical user interface toolkit, you'll need the following:

* PyQt5 - https://pypi.python.org/pypi/PyQt5

Source Installation
-------------------

If you're installing Toyplot from source, you'll need setuptools to run the
Toyplot setup.py script:

* setuptools - http://pythonhosted.org//setuptools

Regression Testing
------------------

The following are required to run Toyplot's regression tests and view
code coverage:

* arrow - Better dates and times for Python - http://arrow.readthedocs.org
* behave - BDD test framework - http://pythonhosted.org/behave
* coverage - code coverage module - http://nedbatchelder.com/code/coverage
* mock - mocking and testing library - http://www.voidspace.org.uk/python/mock
* nose - unit test framework - https://nose.readthedocs.org/en/latest
* nose-exclude - a nose plugin to simplify excluding directories - https://pypi.python.org/pypi/nose-exclude
* pillow - the friendly Python Imaging Library fork - http://pillow.readthedocs.org/en/3.0.x/

Generating Documentation
------------------------

And you'll need to following to generate this documentation:

* Sphinx - documentation builder - http://sphinx-doc.org
* Sphinx readthedocs theme - https://github.com/snide/sphinx_rtd_theme
* napoleon - http://sphinxcontrib-napoleon.readthedocs.org/en/latest/
* Jupyter - http://ipython.org
* Pandoc - http://johnmacfarlane.net/pandoc

