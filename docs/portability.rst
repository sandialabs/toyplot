.. _portability:

.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

Portability
===========

Toyplot has supported Python 2 and Python 3 with a single code base
since very early in its development, and the current release (0.18.0 as of this
writing) is no exception.

However, you should be aware that Python 2 will no longer be maintained past
2020 (https://pythonclock.org), and Toyplot is a member of a significant group
of projects that have pledged to end support for Python 2 soon
(https://python3statement.org).  In particular, Toyplot will no longer support
Python 2 after December 31st, 2018.

What this means
---------------

The Toyplot 0.18 branch will be the final release with Python 2 support.
Toyplot releases after December 31st, 2018 will have portability code removed,
and our automated regression testing will be Python 3 only after that date.  We
will consider pull requests for the 0.18 branch on a case-by-case basis.
