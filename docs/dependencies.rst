.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _dependencies:

Dependencies
============

To use Toyplot with its default functionality, you'll need the following:

* Python 2.7 / Python 3 - http://python.org
* colormath - https://github.com/gtaylor/python-colormath
* multipledispatch - https://github.com/mrocklin/multipledispatch
* numpy - http://numpy.org

If you intend to generate static versions of your Toyplot figures such as PDF or PNG,
you'll need one of the following:

* PyQt5 - https://pypi.python.org/pypi/PyQt5

or

* pycairo - http://cairographics.org/pycairo
* python pango bindings - typically distributed as part of pygtk - http://www.pygtk.org

If you plan to render animated Toyplot figures as MP4 or WebM videos, you'll need
ffmpeg:

* ffmpeg - https://www.ffmpeg.org

If you're installing Toyplot from source, you'll need setuptools to run the
Toyplot setup.py script:

* setuptools - http://pythonhosted.org//setuptools

The following are required to run Toyplot's regression tests and view
code coverage:

* behave - BDD test framework - http://pythonhosted.org/behave
* coverage - code coverage module - http://nedbatchelder.com/code/coverage
* mock - mocking and testing library - http://www.voidspace.org.uk/python/mock
* nose - unit test framework - https://nose.readthedocs.org/en/latest
* nose-exclude - a nose plugin to simplify excluding directories - https://pypi.python.org/pypi/nose-exclude

And you'll need to following to generate this documentation:

* Sphinx - documentation builder - http://sphinx-doc.org
* Sphinx readthedocs theme - https://github.com/snide/sphinx_rtd_theme
* napoleon - http://sphinxcontrib-napoleon.readthedocs.org/en/latest/
* Jupyter - http://ipython.org
* Pandoc - http://johnmacfarlane.net/pandoc
