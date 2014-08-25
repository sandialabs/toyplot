.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right
  :class: logo-important

Installing Toyplot
==================

.. important:: **The Toyplot Sources Aren't Available Yet**

  This is embarassing, but we're still waiting for our lawyer-gnomes to
  finalize the copyright on Toyplot's source code.  Toyplot will be released
  under a BSD-style license as soon as that happens, but in the meantime,
  the following instructions won't work ... apologies!

  Contact Timothy M. Shead <tshead@sandia.gov> if you have questions or
  would like to be notified when Toyplot is released.

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
to install Toyplot's :ref:`dependencies<Toyplot Dependencies>` before installing
:ref:`from source<From Source>`::

    $ sudo port install python27
    $ sudo port select --set python python27
    $ sudo port install py27-numpy
    $ sudo port install py27-pygtk
    $ sudo port install ffmpeg
    $ sudo port install py27-pip
    $ sudo port select --set pip pip27
    $ sudo pip install colormath

If you want to run regression tests / view test coverage::

    $ sudo port install py27-nose
    $ sudo port install py27-coverage

If you want to generate documentation::

    $ sudo port install py27-ipython +notebook +parallel
    $ sudo port select --set sphinx py27-sphinx
    $ sudo port select --set ipython ipython27
    $ sudo pip install sphinx_rtd_theme
    $ sudo pip install sphinxcontrib-napoleon

Using Pip / Easy Install
------------------------

If your package manager doesn't support Toyplot, or doesn't have the latest
version, your next option should be Python setup tools like `pip` (preferred)
or `easy_install`.  You can always install the latest stable version of toyplot
and its dependencies with::

    $ pip install toyplot

or::

    $ easy_install toyplot

.. _From Source:

From Source
-----------

Finally, if you want to work with the latest, bleeding-edge Toyplot goodness,
you can install it using the source code::

    $ git clone https://github.com/sandialabs/toyplot
    $ cd toyplot
    $ python setup.py install

The setup script copies Toyplot into your Python site-packages directory, and
it's ready to go.  Note that you may need root / sudo access to run setup.py,
if you're installing using a system-wide Python instance.
