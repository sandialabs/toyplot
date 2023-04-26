.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

Development
===========

Getting Started
---------------

If you haven't already, you'll want to get familiar with the Toyplot repository
at http://github.com/sandialabs/toyplot ... there, you'll find the Toyplot
source code, issue tracker, discussions, and wiki.

You'll need to install `ffmpeg <http://ffmpeg.org>`_ and `pandoc <https://pandoc.org>`_,
neither of which can be installed via pip.  If you use `Conda <https://docs.conda.io/en/latest/>`_
(which we strongly recommend), you can install them as follows::

    $ conda install ffmpeg pandoc

Next, you'll need to install all of the extra dependencies needed for Toyplot development::

    $ pip install toyplot[all]

Then, you’ll be ready to obtain Toyplot’s source code and install it using
“editable mode”. Editable mode is a feature provided by pip that links the
Toyplot source code into the install directory instead of copying it ... that
way you can edit the source code in your git sandbox, and you don’t have to
keep re-installing it to test your changes::

$ git clone https://github.com/sandialabs/toyplot.git
$ cd toyplot
$ pip install --editable .

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

Many of Toyplot's tests function by comparing the SVG representation of a
:class:`toyplot.canvas.Canvas` against a reference stored in `features/reference`.  These
tests all end with a Behave step along the lines of `Then the figure should match the <test-name> reference image`,
which compares the canvas to the file `tests/reference/test-name.svg`.  The
first time to you run a new test that uses this step, it
will generate and store the new reference file, then fail, prompting you to
examine the reference file to ensure that it's correct.  The next time you run
the test, it will function normally, comparing the canvas against the reference
file.

If you make changes that cause an existing test to fail, the failed SVG will
be written to `features/failed/test-name.svg`, so you can compare it against the
corresponding reference SVG in `features/reference/test-name.svg`.

Test Coverage
-------------

When you run the test suite with `regression.py`, it also automatically
generates code coverage statistics.  To see the coverage results, open
`.cover/index.html` in a web browser.

Building the Documentation
--------------------------

To build the documentation, run::

    $ cd toyplot/docs
    $ make html

Once the documentation is built, you can view it by opening
`docs/_build/html/index.html` in a web browser.
