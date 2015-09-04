.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _macports-installation:

MacPorts Installation
=====================

There isn't a MacPorts port for Toyplot yet, but you can still use MacPorts
to install Toyplot's :ref:`dependencies` before installing
Toyplot using pip::

    $ sudo port install python27
    $ sudo port select --set python python27
    $ sudo port install py27-colormath
    $ sudo port install py27-multipledispatch
    $ sudo port install py27-numpy
    $ sudo port install py27-pip
    $ sudo port select --set pip pip27
    $ sudo pip install toyplot

If you want to generate PDF / PNG files using PyQt5::

    $ sudo port install py27-pyqt5

If you want to generate PDF / PNG files using cairo::

    $ sudo port install py27-pygtk

If you want to generate MP4 / WebM files::

    $ sudo port install ffmpeg

If you want to run regression tests / view test coverage::

    $ sudo port install py27-nose
    $ sudo port install py27-coverage
    $ sudo pip install nose-exclude
    $ sudo pip install behave

If you want to generate documentation::

    $ sudo port install py27-ipython +notebook
    $ sudo port select --set sphinx py27-sphinx
    $ sudo port select --set ipython ipython27
    $ sudo port install pandoc
    $ sudo pip install sphinx_rtd_theme
    $ sudo pip install sphinxcontrib-napoleon

