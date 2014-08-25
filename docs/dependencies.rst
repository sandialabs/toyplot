.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _Toyplot Dependencies:

Toyplot Dependencies
====================

Toyplot has the following required dependencies:

* Python 2.7 - http://python.org
* numpy - http://numpy.org
* colormath - https://github.com/gtaylor/python-colormath

You'll need the following if you intend to generate PDF, PNG, Encapsulated
Postscript, or MP4 versions of your Toyplot figures:

* pycairo - http://cairographics.org/pycairo
* python pango bindings - typically distributed as part of pygtk - http://www.pygtk.org
* ffmpeg - https://www.ffmpeg.org - required to generate MP4 videos.

The following isn't needed to run Toyplot once it's installed, but it's required
to run the setup script when installing Toyplot from source:

* setuptools - http://pythonhosted.org//setuptools

The following are required to run regression tests / view test coverage:

* nose - unit test framework - https://nose.readthedocs.org/en/latest/
* coverage - code coverage module - http://nedbatchelder.com/code/coverage/

And the following are needed to generate this documentation:

* Sphinx - documentation builder - http://sphinx-doc.org
* Sphinx readthedocs theme - https://github.com/snide/sphinx_rtd_theme
* napoleon - http://sphinxcontrib-napoleon.readthedocs.org/en/latest/
* IPython - http://ipython.org

