.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _release-notes:

Release Notes
=============

Toyplot 0.5.0 - May 26, 2015
----------------------------

* Switched to https://travis-ci.org/sandialabs/toyplot for continuous integration testing.
* Switched to https://coveralls.io/r/sandialabs/toyplot to track test coverage.
* Added a custom CSS style `-toyplot-anchor-shift` for controlling horizontal text offsets.
* Added new documentation on color, text alignment, units, data tables, and table axes to the user guide.
* Callers can increase the number of table rows and columns when creating table axes from a data table.
* Overhauled Toyplot's handling of real-world units, allowing arbitrary units throughout the API, and made it explicit that the default canvas units are CSS pixels.
* Added axis visibility options to the convenience API.
* `toyplot.data.Table` can be converted to a `numpy` matrix.
* Positive angles yield counterclockwise rotation throughout the API, for consistency with trigonometry.
* Rendered text automatically expands a plot's domain to avoid clipping.
* Fixed a longstanding problem displaying mouse coordinates outside the data domain for a plot.
* Moved interaction-specific markup from the SVG backend to the HTML backend.
* When exporting data from a figure, only the caller-supplied data is exported.
* The API makes an explicit distinction between text used for "annotation" and text used for data.
* Many small fixes.

Toyplot 0.4.0 - January 27, 2015
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
