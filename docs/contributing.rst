.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

Contributing
============

Getting Started
---------------

If you haven't already, you'll want to get familiar with the Toyplot repository
at http://github.com/sandialabs/toyplot ... there, you'll find the Toyplot
sources, issue tracker, and wiki.

Next, you'll need to install Toyplot's :ref:`dependencies`.  Then, you'll be
ready to get Toyplot's source code and use setuptools to install it. To do
this, you'll almost certainly want to use "develop mode".  Develop mode is a a
feature provided by setuptools that links the Toyplot source code into the
install directory instead of copying it ... that way you can edit the source
code in your git sandbox, and you don't have to re-install it to test your
changes::

    $ git clone https://github.com/sandialabs/toyplot.git
    $ cd toyplot
    $ python setup.py develop

Versioning
----------

Toyplot version numbers follow the `Semantic Versioning <http://semver.org>`_ standard.

Coding Style
------------

The Toyplot source code follows the `PEP-8 Style Guide for Python Code <http://legacy.python.org/dev/peps/pep-0008>`_.

Running Regression Tests
------------------------

To run the Toyplot test suite, simply run `regression.py` from the
top-level source directory::

    $ cd toyplot
    $ python regression.py

The tests will run, providing feedback on successes / failures.

Writing Regression Tests
--------------------------

.. note::

  Toyplot has been gradually transitioning from `nose <https://nose.readthedocs.org/en/latest/>`_
  to `behave <http://pythonhosted.org/behave>`_ for implementing regression tests.  New tests should
  be added to the `features` directory using behave.  The following outlines how the old tests
  were written, and will remain as a reference until they are all replaced.

Existing tests are located in `tests/tests.py`.

Many of the tests function by comparing the SVG representation of a
:class:`toyplot.canvas.Canvas` against a reference stored in `tests/reference`.  These
tests all end with a call to `assert_canvas_matches(canvas, "test-name")`,
which compares the canvas to the file `tests/reference/test-name.svg`.  The
first time to you run a new test that uses :func:`assert_canvas_matches`, it
will generate and store the new reference file, then fail, prompting you to
examine the reference file to ensure that it's correct.  The next time you run
the test, it will function normally, comparing the canvas against the reference
file.

If you make changes that cause an existing test to fail, the failed SVG will
be written to `tests/failed/test-name.svg`, so you can compare it against the
corresponding reference SVG in `tests/reference/test-name.svg`.

Test Coverage
-------------

When you run the test suite with `regression.py`, it also automatically
generates code coverage statistics.  To see the coverage results, open
`.cover/index.html` in a web browser.

Building the Documentation
--------------------------

To build the documentation, run::

    $ cd toyplot
    $ python docs/setup.py

Note that significant subsets of the documentation are written using Jupyter
notebooks, so the docs/setup.py script requires Jupyter to convert the
notebooks into restructured text files for inclusion with the rest of the
documentation.

Once the documentation is built, you can view it by opening
`docs/_build/html/index.html` in a web browser.
