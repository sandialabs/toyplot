.. _portability:

.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

Portability
===========

Past versions of Toyplot up-to 0.18 supported Python 2 and Python 3 with a
single code base.  However, you should be aware that Python 2 will no longer be
maintained past 2020 (https://pythonclock.org), and Toyplot is one of many
projects to pledge an end to support for Python 2
(https://python3statement.org).  In particular, Toyplot no longer supports
Python 2 as of December 31st, 2018.

What this means
---------------

The Toyplot 0.18 branch was the final release that included Python 2 support.
Starting with Toyplot 0.19, portability code has been removed and our automated
regression tests are only run using Python 3.  Of course, developers are free
to continue working with the 0.18 branch if they need to support Python 2, and
we will consider pull requests for the 0.18 branch on a case-by-case basis.
