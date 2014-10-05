.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

Installation
============

Using Your OS Package Manager
-----------------------------

Your operating system package manage manager (apt, yum, MacPorts, etc) should
be your first stop for installing Toyplot - using your package manager will
make it easy to install Toyplot and its dependencies, keep them up-to-date, and
even (gasp!) uninstall them cleanly.  If your package manager doesn't support
Toyplot yet, drop them a line and let them know you'd like them to add it!

MacPorts-Specific Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There isn't a MacPorts port for Toyplot yet, but you can still use MacPorts
to install Toyplot's :ref:`dependencies` before installing
Toyplot using pip::

    $ sudo port install python27
    $ sudo port select --set python python27
    $ sudo port install py27-colormath
    $ sudo port install py27-multipledispatch
    $ sudo port install py27-numpy
    $ sudo port install py27-pygtk
    $ sudo port install ffmpeg
    $ sudo port install py27-pip
    $ sudo port select --set pip pip27
    $ sudo pip install toyplot

If you want to run regression tests / view test coverage::

    $ sudo port install py27-nose
    $ sudo port install py27-coverage

If you want to generate documentation::

    $ sudo port install py27-ipython +notebook +parallel
    $ sudo port select --set sphinx py27-sphinx
    $ sudo port select --set ipython ipython27
    $ sudo port install pandoc
    $ sudo pip install sphinx_rtd_theme
    $ sudo pip install sphinxcontrib-napoleon

Using Pip / Easy Install
------------------------

If your package manager doesn't support Toyplot, or doesn't have the latest
version, your next option should be Python setup tools like `pip`.  You can
always install the latest stable version of toyplot and its **required**
dependencies with::

    $ pip install toyplot

To install Toyplot's **optional** :ref:`Dependencies`, you'll need to use a combination
of pip and your system package manager.

.. _From Source:

From Source
-----------

Finally, if you want to work with the latest, bleeding-edge Toyplot goodness,
you can install it using the source code::

    $ git clone https://github.com/sandialabs/toyplot
    $ cd toyplot
    $ sudo python setup.py install

The setup script copies Toyplot into your Python site-packages directory, and
it's ready to go.
