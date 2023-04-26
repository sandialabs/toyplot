.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _installation:

Installation
============

Toyplot
-------

To install the latest stable version of Toyplot and its dependencies, use `pip`::

    $ pip install toyplot

... once it completes, you'll be able to use all of Toyplot's core features.


Ghostscript
-----------

To generate static PNG versions of your Toyplot figures, you'll need
Ghostscript, which can't be installed via pip.  If you use `Conda <https://docs.conda.io/en/latest/>`_
(which we strongly recommend), you can install it as follows::

    $ conda install ghostscript

ffmpeg
------

If you plan to render animated Toyplot figures as MP4 files, you'll need
ffmpeg, which also can't be installed via pip.  If you use `Conda <https://docs.conda.io/en/latest/>`_
(again, strongly recommended), you can install it as follows::

    $ conda install ffmpeg

.. _documentation:

Documentation
-------------

We assume that you'll normally access this documentation online, but if you
want a local copy on your own computer, do the following:

First, you'll need the `pandoc <https://pandoc.org>`_ universal document
converter, which can't be installed with pip ... if you use `Conda <https://docs.conda.io/en/latest/>`_
(we cannot recommend it strongly enough), you can install it with the following::

    $ conda install pandoc

Once you have pandoc, install Toyplot along with all of the dependencies needed to build the docs::

    $ pip install toyplot[doc]

Next, do the following to download a tarball to the current directory
containing all of the Toyplot source code, which includes the documentation::

    $ pip download toyplot --no-binary=:all: --no-deps

Now, you can extract the tarball contents and build the documentation (adjust the
following for the version you downloaded)::

    $ tar xzvf toyplot-0.6.1.tar.gz
    $ cd toyplot-0.6.1/docs
    $ make html
