.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _installation:

Installation
============

Using Your OS Package Manager
-----------------------------

Your operating system package manage manager (apt, yum, MacPorts, etc) should
be your first stop for installing Toyplot - using your package manager will
make it easy to install Toyplot and its dependencies, keep them up-to-date, and
even (gasp!) uninstall them cleanly.  If your package manager doesn't support
Toyplot yet, drop them a line and let them know you'd like them to add it!

.. toctree::
  :maxdepth: 2

  conda-installation.rst
  freebsd-installation.rst
  macports-installation.rst

Using Pip / Easy Install
------------------------

If your package manager doesn't support Toyplot, or doesn't have the latest
version, your next option should be Python setup tools like `pip`.  You can
always install the latest stable version of toyplot and its **required**
:ref:`dependencies` with::

    $ pip install toyplot

To install Toyplot's **optional** :ref:`dependencies`, you'll need to use a combination
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
