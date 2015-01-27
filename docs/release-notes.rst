.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _release-notes:

Release Notes
=============

Toyplot 0.4.0 - January 27, 2014
--------------------------------

* Began continuous integration testing.
* Switched from ost.io to https://gitter.im/sandialabs/toyplot for support requests.
* Made the HTML backend the primary renderer.
* Improved logarithmic tick formatting and customization.
* Increased consistency between the fill() and plot() APIs.
* Simplified the way colors are inherited for line plots and scatter plots.
* Added basic functionality for reading and writing CSV files.

  * Note: for pedagical purposes only - Toyplot is *not* a data manipulation tool!

* Ongoing improvements to the table axes API:

  * Added support for table titles.
  * Added support for hiding table headers.
  * Table headers can have multiple rows.
  * Ensure that visible cells are rendered in a deterministic order.
  * Create a default grid line between table header and body.
  * Added support for user-configurable gaps between cells.

Toyplot 0.3.0 - November 5, 2014
--------------------------------

* Switched to toyplot.data.Table for all internal data storage.
* Reorganized the codebase into smaller, more focused modules.
* Added a new backend to produce WebM video.
* Data tables can be rendered to LaTeX.
* New table axes for rendering tables as data graphics.

Toyplot 0.2.0 - September 2, 2014
---------------------------------

* Introduced support for Python 3.
* Removed pure black from the default styling.
* Allow regression tests to run without optional dependencies.

Toyplot 0.1.0 - August 25, 2014
-------------------------------

* Initial Release
