.. _compatibility:

.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

Compatibility
=============

A quick disclaimer on backwards-compatibility for Toyplot users:

Toyplot follows the `Semantic Versioning <http://semver.org>`_ standard for
assigning version numbers in a way that has specific meaning.  Toyplot version
numbers use *<major>.<minor>.<patch>* numbering.  Releases with different
major API numbers are API incompatible.  Minor version numbers signify new
features that are backwards-compatible with the current major version.  Patch
numbers indicate bug fixes and documentation changes that are
backwards-compatible with the current major and minor version.

Python Versions
---------------

Past versions of Toyplot supported Python 2 and Python 3 with a single code
base.  However, Python 2 has not been maintained since 2020
(https://pythonclock.org), and Toyplot stopped supporting Python 2 on December
31st, 2018.  The Toyplot 0.18 branch was the final release that included Python
2 support ... beginning with Toyplot 0.19, the portability code was removed and
our automated regression tests are only run using Python 3.  Of course,
developers are free to continue working with the 0.18 branch if they need to
support Python 2, and we will consider pull requests for the 0.18 branch if
they arise.
