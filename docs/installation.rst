.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _installation:

Installation
============

Using a Package Manager
-----------------------------

A package manager (conda, apt, yum, MacPorts, etc) should generally be your
first stop for installing Toyplot - it will make it easy to install Toyplot and
its dependencies, keep them up-to-date, and even (gasp!) uninstall them
cleanly.  If your package manager doesn't support Toyplot yet, drop them a line
and let them know you'd like them to add it!

If you're new to Python or unsure where to start, we strongly recommend taking
a look at :ref:`Anaconda <anaconda-installation>`, which the Toyplot developers
use during their day-to-day work.

.. toctree::
  :maxdepth: 2

  anaconda-installation.rst
  freebsd-installation.rst
  macports-installation.rst

Using Pip / Easy Install
------------------------

If your package manager doesn't support Toyplot, or doesn't have the latest
version, your next option should be Python setup tools like `pip`.  You can
always install the latest stable version of toyplot and its required
dependencies using::

    $ pip install toyplot

... following that, you'll be able to use all of Toyplot's features, and export
figures to all of Toyplot's preferred file formats, including HTML, SVG, and PDF.

For export to other formats like PNG or MP4, you'll have to install additional resources
listed in the :ref:`dependencies` section of the manual.

.. _From Source:

From Source
-----------

Finally, if you want to work with the latest, bleeding-edge Toyplot goodness,
you can install it using the source code::

    $ git clone https://github.com/sandialabs/toyplot
    $ cd toyplot
    $ sudo python setup.py install

The setup script installs Toyplot's required dependencies and copies Toyplot into
your Python site-packages directory, ready to go.

Once again, export to other formats like PNG or MP4, wil require additional resources
listed in :ref:`dependencies`.

