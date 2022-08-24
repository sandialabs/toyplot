.. _portability:

.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

Portability
===========

Past versions of Toyplot supported Python 2 and Python 3 with a
single code base.  However, Python 2 has not been maintained since 2020
(https://pythonclock.org), and Toyplot is one of many projects that pledged to
end support for Python 2 (https://python3statement.org).

What this means
---------------

Toyplot stopped supporting Python 2 on December 31st, 2018.  The Toyplot 0.18
branch was the final release that included Python 2 support.  Starting with
Toyplot 0.19, the portability code was removed and our automated regression
tests are only run using Python 3.  Of course, developers are free to continue
working with the 0.18 branch if they need to support Python 2, and we will
consider pull requests for the 0.18 branch if they arise.
