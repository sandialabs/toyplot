.. image:: ../artwork/toyplot.png
  :width: 200px
  :align: right

.. _release-notes:

Release Notes
=============

Toyplot 0.15.0 - July 27, 2017
------------------------------

* Markers can be embedded in any text, including tick marks, legends, labels, and table contents.
* Hyperlinks can be embedded in any text using the <a href="..."> tag.
* Legends are implemented using table coordinates, so legends can be customized using any table feature.
* Started a new documentation section for case-studies, with graph community and neural network examples.
* Started a new section in the documentation for projects using Toyplot.
* Callers can define their own custom marks, and modify rendering for existing marks, using the new rendering API.
* Defined a new API for embedding Javascript in HTML markup, for use with custom marks.
* Graph visualizations can export vertex and edge data as CSV tables.
* Added support for head, middle, and tail markers on graph edges.
* Added an `offset` property for Cartesian axis labels.
* Toyplot colors are allowed as style property values.
* Per-series and per-datum colors can be specified using Python sequences as well as numpy arrays.
* Error messages specify which CSS properties are allowed.
* Deprecated the `gutter` parameter in favor of `margin`, which can specify separate left / right / top / bottom margins, if desired.
* Added `toyplot.html.tostring()` to simplify generating HTML.
* Added a style option to `toyplot.html.render()` and `toyplot.html.tostring()`.
* Added a `palette` argument to override the default series palette when creating axes.
* Text markup didn't include units for font-size, causing incorrect results on Firefox.

Toyplot 0.14.0 - April 17, 2017
-------------------------------

* Completely new text layout that explicitly positions all text.
* Experimental support for hyperlinks in table cells.
* Return a scalar instead of an array when accessing toyplot.data.Table using a single column name and row index.
* Correct a bug that caused text baselines to be computed incorrectly in PDF output.
* Add pylint to the regression test suite.
* Allow font-family to be used in inline rich text styles.
* Created an API to retrieve font metrics.
* Disable obnoxious colormath logging by default.
* Mention XML escaping for rich text in the user guide.
* The "<" and ">" markers were rendered reversed.
* Eliminate warnings using a Pandas series as the baseline for a bar plot.
* Make it easier to disable graph vertex labels.
* Allow stroke-linecap for CSS line styles.
* Improve rasterized PNG output quality.
* Warn when using older versions of ghostscript that produce lower-quality PNG output.
* Suppress the "No handlers could be found for logger toyplot" warning.
* Rewrote the logic for detecting Ghostscript.

Toyplot 0.13.0 - July 22, 2016
------------------------------

* Allow fill marks to be used as annotation.
* Explicitly disable data export from annotation marks.
* Add an experimental `<axis>.domain.show` parameter to control whether the domain is displayed using axis spines.
* `toyplot.data.read_csv(convert=True)` will try to parse integer as well as floating-point types.
* Completely rewrote the table coordinates implementation.
* Table coordinates support advanced, numpy-style indexing for all rows, columns, cells, gridlines, and gaps.
* Added API to delete table coordinate rows and columns.
* Added API to insert table coordinate rows and columns.
* By default, all table cells are vertically and horizontally centered with a default font.
* Matrix visualizations no longer bold row and column indices by default.
* End-users can export CSV data from table coordinates and matrix visualizations.
* Added table-cell bar plots and line plots that use the data already contained in the table.

Toyplot 0.12.0 - May 27, 2016
-----------------------------

* Pandas data frame indices (including hierarchical indices) can optionally be included when converting to `toyplot.data.Table`.
* Fixed a Python 3 portability issue.
* Table coordinates didn't format NaN values properly when using a custom formatting string.
* The `arrow` module is only imported when needed.
* New documentation on grouping table rows.
* Documented platform-specific timezone naming issues.
* Improved documentation of the color factory objects in `toyplot.color`.
* Use consistent naming for numberline coordinates.
* Made it easier to iterate over `toyplot.data.Table` rows.
* Interactive mouse coordinates work correctly with numberlines and shared axes, and are only displayed by click / touch events.
* Position ticks relative to axes with a `location` property, and deprecate the tick labels `location` property.
* Fixed a problem rendering bars with a log scale and nonzero domain minimum.
* Removed the API to change text during animation.
* Significant cleanup and organization of HTML backend code and generated markup.
* Renamed the `toyplot.axes` module to `toyplot.coordinates` for consistency, clarity.
* Added `toyplot.canvas.Canvas.cartesian()` and deprecated `toyplot.canvas.Canvas.axes()`.
* Added `toyplot.locator.Uniform` and deprecated `toyplot.locator.Basic`.
* Added documentation links to external libraries, where practical.
* Added `text-shadow` to the list of valid CSS text attributes.
* Updated dependencies to require numpy >= 1.8.0, and eliminated code that inadvertently depended on numpy >= 1.9.
* Experimental support for displaying `PIL` and `scikit-image` images.
* Added a `style` property to `toyplot.canvas.Canvas`.
* Deprecated implicit conversion from palettes to colormaps for matrix visualization.
* Provide better error messages if a caller passes anything but a canvas to a rendering backend.
* Add support for multi-series marks in legends.
* Updated links to point to our new documentation domain, `http://toyplot.readthedocs.io`.
* Axis labels support the same `location` and `offset` parameterization as axis ticks / tick labels.

Toyplot 0.11.0 - February 18, 2016
----------------------------------

* Added more complex indexing / slicing options to toyplot.data.Table.
* Deprecated `toyplot.data.Table.rows()` and `toyplot.data.Table.columns()`.
* Removed support for custom markers.
* `-toyplot-anchor-shift` didn't work correctly with rotated text.
* Documented text alignment behavior for rotated text.
* Added `location` parameter for axis labels.
* Improved text alignment defaults for rotated and unrotated axis labels.
* Don't alter the axis domain if tick labels aren't visible.
* Change the default linear color map to a diverging blue-red palette.
* Pandas data frames with duplicate column names can be converted to `toyplot.data.Table`.
* Allow callers to suppress NaNs in table visualization cells.
* Render color arrays as swatches in Jupyter notebooks.
* Added `toyplot.color.brewer.palette()`, `toyplot.color.brewer.map()`, and `toyplot.color.diverging.map()`.
* Deprecated `toyplot.color.brewer()` and `toyplot.color.diverging()`.
* `toyplot.color.LinearMap` color stops can be explicitly positioned.
* Added `toyplot.color.linear.map()` with "Blackbody", "ExtendedBlackbody", "Kindlmann" and "ExtendedKindlmann" color maps.
* Deprecated implicit conversions from color palettes to color maps during color mapping.
* Split color-related documentation into separate "Color" and "Color Mapping" sections of the user guide.
* Improved debugging output when a regression test fails.
* Many code coverage improvements.

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

a Initial Release
