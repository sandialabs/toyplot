.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _release-notes:

Release Notes
=============

Toyplot 0.10.0 - January 12, 2016
---------------------------------

* Added rich text support, using a limited subset of HTML markup.
* Added a tick locator for displaying timestamp data with properly formatted times.
* Created a new, pure-Python PDF backend using ReportLab.
* Created a new PNG backend that renders by rasterizing PDFs with Ghostscript.
* Removed deprecated PDF and PNG backends.
* Added numberline axes, for displaying one-dimensional data.
* Refactored the scatterplot mark to support data with any number of dimensions.
* Added one-dimensional scatterplot support to numberlines.
* Completely redesigned the color scale implementation to use numberlines.
* Added API for easily adding color scales to axes and matrix visualizations.
* Provided both size and area parameters to specify marker sizes.
* Moved log scales to a dedicated section of the user guide.
* Optimized graph layout when every vertex already has a position.
* Removed the GraphViz graph layout strategy.
* Use consistent naming for matrix visualization parameters.
* toyplot.data.read_csv() can optionally convert string values to numeric values.
* Replaced toyplot.color.lighten() with toyplot.color.spread(), which is more flexible.
* Display toyplot color values as swatches in Jupyter notebooks.
* Expanded the color documentation in the user guide.
* Reduced regression test boilerplate code.
* Test coverage improvements.

Toyplot 0.9.0 - November 22, 2015
---------------------------------

* Documented installation for Anaconda and FreeBSD.
* Experimental support for graph visualization, with flexible layout algorithms, shared layouts and node "pinning".
* Allow cartesian axes to fill the available range while maintaining their aspect ratio.
* Axis ticks can extend above or below the axis spine.
* Positioning an axis spine positions its ticks and tick labels as well.
* Added support for shared axes / multiple axes, to display multiple overlapping domains in a single plot.
* Format specifiers are available for the Extended and Heckbert tick locators, courtesy of Johann du Toit.
* Began using pylint as a regular code quality check.
* Pandas data frames are automatically converted when creating data tables / table axes.
* Created a new default PDF backend using the ReportLab library.
* Switched to toyplot.qt.png as the default PNG backend.
* Provide better feedback when using the toyplot.pdf and toyplot.png meta backends.

Toyplot 0.8.0 - September 7, 2015
---------------------------------

* Removed deprecated colormap and palette parameters from the API.
* Allow simplified color mapping specifications.
* Improved test coverage.
* Fix a problem embedding embedding axes in tables using more than one merged cell.
* Add table cell width / height support for real-world units.
* Hide masked values in table axes.
* Reorganize the installation documentation.
* Add support for rotated text in table cells.
* Add top/bottom/left/right label support for matrix visualizations.
* Add new toyplot.locator.Null do-nothing tick locator.
* Add matrix visualization support for right / bottom ticks.
* Add custom locator support for matrix visualizations.
* Make matrix visualization color parameters consistent with the rest of the API.
* Add missing reference documentation for toyplot.projection module.
* Cleanup the toyplot.color.broadcast(...) API and implementation.
* Make the API for specifying color mapping consistent across all visualization types.
* Allow per-datum titles on line plots and scatterplots.
* Expand the color section in the user guide to cover color mapping.
* Add a new section on null data to the user guide.
* Eliminate nuisance warnings from numpy.
* Automatically validate source notebooks as part of the documentation build.

Toyplot 0.7.0 - August 12, 2015
-------------------------------

* Added a user guide section on embedding plots.
* Added a user guide example of datetime objects as tick labels.
* Make the Toyplot sourcecode fully PEP-8 conforming - thanks to Chris Morgan.
* Worked around problems with numpy.broadcast_arrays() in numpy 1.8.
* Removed LaTeX table formatting functionality that was replaced by table axes.
* Added a new backend to display figures in a standalone Qt window.
* Switched to the Python logger module for warnings / errors.
* Updated the public API for specifying scalar color palettes / maps, and deprecated separate color palette / map API parameters.
* Changed the way we encode opacities, for compatibility with Inkscape and Adobe Illustrator.
* Removed the obsolete toyplot.selenium backend.
* Treat hlines() and vlines() as annotation (so they don't affect the data domain), unless the caller specifies otherwise.
* Created new Qt backends to generate PDF and PNG figures.
* Figures can be resized consistently across all browsers, particularly Firefox and IE.
* Reorganized the backend documentation, and explicitly documented the distinction between backends and displays.
* Fixed a case where canvas resizing didn't handle explicit units correctly.
* Added a new section on interaction to the user guide.
* Allow figure creators to override the default filename when users export data from an interactive figure.
* Significant changes to our travis-ci.org test environment.
* toyplot.data.Table.matrix() didn't work in Python 3.
* Removed toyplot.data.Table.to_csv(), we want to discourage people from using Toyplot for data manipulation.
* Many objects didn't render properly in Jupyter notebooks with Python 3.
* Added parameters to disable the row and column labels in matrix visualizations.

Toyplot 0.6.0 - July 13, 2015
-----------------------------

* Unicode text wasn't handled correctly by text marks.
* Added an experimental matrix visualization using table axes.
* Added a "title" property for table cells.
* Fix inconsistencies in our use of alignment-baseline and text-anchor CSS properties.
* Added a new section to the user guide on the convenience API.
* Allow real-world units for canvas layouts, and tweak the parameter order for corner layouts.
* Expanded user guide documentation on canvas layouts.
* Added table axes regions for all four sides and corners, plus a property to access every cell in a region.
* Added automatic conversion from numpy NpzFile to toyplot.data.Table.
* Added experimental support for graph visualization.
* Allow toyplot.data.Table initialization from a sequence of 2-tuples.
* Cairo backends were ignoring -toyplot-anchor-shift.
* Cairo backends didn't handle all supported alignment-baseline values.
* Added matrix and table visualizations to the convenience API.
* Added accessors for shape, row count, and column count for table axes and regions.
* Added toyplot.locator.Integer, and a step parameter to control labelling for matrix visualizations.
* Always return a unicode string from toyplot.canvas.Canvas._repr_html_(), for compatibility with Jupyter / IPython notebooks running Python 3 kernels.
* Assign a sensible default filename for CSV downloads, for browsers that support it.
* Added a contributed Conda build recipe.
* Allow toyplot.data.Table to be initialized from a 2D numpy array.
* Rename the toyplot.axes.Table "title" parameter to "label" for consistency with the other axes.
* Added a new "Labels and Legends" section to the user guide.
* Added a new "Tick Locators" section to the user guide.
* Added experimental toyplot.data.contiguous() function to identify contiguous ranges in an array.
* Fix a problem with interactive Y coordinates when using a log scale that straddled the origin.

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
