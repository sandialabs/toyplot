.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _macports-installation:

MacPorts Installation
=====================

Required
--------

There isn't a MacPorts package for Toyplot yet, but you can still use MacPorts
to install the :ref:`dependencies` before installing Toyplot using pip::

    $ sudo port install py-colormath
    $ sudo port install py-multipledispatch
    $ sudo port install py-numpy
    $ sudo port install py-pip
    $ sudo port install py-reportlab
    $ sudo port select --set pip pip27
    $ sudo pip install toyplot

PNG Export
----------

To generate static PNG versions of your Toyplot figures,
you'll need Ghostscript::

    $ sudo port install ghostscript

MP4 / WebM Export
-----------------

If you plan to render animated Toyplot figures as  MP4 / WebM files, you'll
need all the above for exporting PNG images, plus ffmpeg::

    $ sudo port install ffmpeg

