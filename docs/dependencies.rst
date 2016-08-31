.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _dependencies:

Dependencies
============

Minimum Requirements
--------------------

To use Toyplot you will need, at a minimum, Python 2 or 3 (duh):

* Python 2.7 / Python 3 - http://python.org

plus the following (if you install Toyplot
using pip, these are automatically installed for you):

* colormath - https://github.com/gtaylor/python-colormath
* multipledispatch - https://github.com/mrocklin/multipledispatch
* numpy >= 1.8.0 - http://numpy.org

Timestamp Labels
----------------

To display datetime information using the
:class:`toyplot.locator.Timestamp` locator, the following is required (if you
install Toyplot using pip, it's automatically installed for you):

* arrow - Better dates and times for Python - http://arrow.readthedocs.io

Bitmap Images
-------------

To add bitmap images to your figures, you'll need the following (if you install Toyplot
using pip, it's automatically installed for you):

* pypng - Python PNG IO library - https://pythonhosted.org/pypng/index.html

PDF Export
----------

Generating static PDF versions of your Toyplot figures requires the following
(if you install Toyplot using pip, it's automatically installed for you):

* ReportLab - open source PDF toolkit - http://www.reportlab.com/opensource/

If your Toyplot figures contain bitmap images, ReportLab also requires the following:

* Pillow - the friendly Python Imaging Library fork - http://pillow.readthedocs.io/en/3.0.x/

PNG Export
----------

To generate static PNG versions of your Toyplot figures,
you'll need the PDF Export dependencies, plus Ghostscript:

* Ghostscript - Postscript / PDF interpreter - http://www.ghostscript.com

MP4 / WebM Export
-----------------

If you plan to render animated Toyplot figures as MP4 or WebM videos, you'll need
the PNG Export dependencies for exporting PNG files, plus ffmpeg:

* ffmpeg - cross-platform video conversion - https://www.ffmpeg.org

Source Installation
-------------------

If you're installing Toyplot from source, you'll need setuptools to run the
Toyplot setup.py script:

* setuptools - http://pythonhosted.org//setuptools

Regression Testing
------------------

The following are required to run Toyplot's regression tests and view
code coverage:

* behave - BDD test framework - http://pythonhosted.org/behave
* coverage - code coverage module - http://nedbatchelder.com/code/coverage
* mock - mocking and testing library - http://www.voidspace.org.uk/python/mock
* nose - unit test framework - https://nose.readthedocs.io/en/latest
* nose-exclude - a nose plugin to simplify excluding directories - https://pypi.python.org/pypi/nose-exclude
* Pillow - the friendly Python Imaging Library fork - http://pillow.readthedocs.io/en/3.0.x/
* xmldiff - print differences between XML files - https://pypi.python.org/pypi/xmldiff

Generating Documentation
------------------------

And you'll need to following to generate this documentation:

* Sphinx - documentation builder - http://sphinx-doc.org
* Sphinx readthedocs theme - https://github.com/snide/sphinx_rtd_theme
* napoleon - http://sphinxcontrib-napoleon.readthedocs.io/en/latest/
* Jupyter - http://ipython.org
* Pandoc - http://johnmacfarlane.net/pandoc

