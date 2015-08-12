
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _table-axes:

Table Axes
==========

Data tables, with *rows* containing *observations* and *columns*
containing *variables* or *series*, are arguably the cornerstone of
science. Much of the functionality of Toyplot or any other plotting
package can be reduced to a process of mapping data series from tables
to properties like coordinates and colors. Nevertheless, much tabular
information is still best understood in its "native" tabular form, and
we believe that even a humble table benefits from good layout and design
- which is why Toyplot supports rendering tables as data graphics,
treating them as first-class objects instead of specialized markup.

To accomplish this, Toyplot provides :class:`toyplot.axes.Table`,
which is a specialized coordinate system. Just like
:ref:`cartesian-axes`, table axes map domain coordinates to canvas
coordinates. Unlike traditional Cartesian axes, table axes map integer
coordinates that increase from left-to-right and top-to-bottom to
rectangular ``regions`` of the canvas called ``cells``.

Be careful not to confuse the ``table axes`` described in this section
with :ref:`data-tables`, which are purely a data storage mechanism. To
make this distinction clear, let's start by loading some sample data
into a data table:

.. code:: python

    import numpy
    import toyplot.data
    data_table = toyplot.data.read_csv("temperatures.csv")
    data_table = data_table[:10]


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-6b97b2bc5003> in <module>()
          1 import numpy
    ----> 2 import toyplot.data
          3 data_table = toyplot.data.read_csv("temperatures.csv")
          4 data_table = data_table[:10]


    ImportError: No module named toyplot.data


Now, we can use the data table to initialize a set of table axes:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table)
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-1e3859a25e98> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table)
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


With surprisingly little effort, this produces a very clean, easy to
read table. Note that, like regular Cartesian axes, the table axes fill
the available Canvas by default, so you can adjust your canvas width and
height to expand or contract the rows and columns in your table. Also,
each row and column in the table receives an equal amount of the
available space, unless they are individually overridden as we've done
here. Of course, you're free to use all of the mechanisms outlined in
:ref:`canvas-layout` to add multiple sets of table axes to a canvas.

When you load a CSV file using :func:`toyplot.data.read_csv`, the
resulting table columns all contain string values. Note that the columns
in the graphic are left-justified, the default for string data. Let's
see what happens when we convert some of our columns to integers:

.. code:: python

    data_table["TMAX"] = data_table["TMAX"].astype("int32")
    data_table["TMIN"] = data_table["TMIN"].astype("int32")
    data_table["TOBS"] = data_table["TOBS"].astype("int32")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-d8251d0bbefc> in <module>()
    ----> 1 data_table["TMAX"] = data_table["TMAX"].astype("int32")
          2 data_table["TMIN"] = data_table["TMIN"].astype("int32")
          3 data_table["TOBS"] = data_table["TOBS"].astype("int32")


    NameError: name 'data_table' is not defined


.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table)
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-1e3859a25e98> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table)
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


After converting the TMAX, TMIN, and TOBS columns to integers, they are
right-justified within their columns, so their digits all align, making
it easy to judge magnitudes. As it happens, the data in this file is
stored as integers representing tenths-of-a-degree Celsius, so let's
convert them to floating-point Celsius degrees and see what happens:

.. code:: python

    data_table["TMAX"] = data_table["TMAX"] * 0.1
    data_table["TMIN"] = data_table["TMIN"] * 0.1
    data_table["TOBS"] = data_table["TOBS"] * 0.1


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-fdfde9af139f> in <module>()
    ----> 1 data_table["TMAX"] = data_table["TMAX"] * 0.1
          2 data_table["TMIN"] = data_table["TMIN"] * 0.1
          3 data_table["TOBS"] = data_table["TOBS"] * 0.1


    NameError: name 'data_table' is not defined


.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table)
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-1e3859a25e98> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table)
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


Now, all of the decimal points are properly aligned within each column,
even for values without a decimal point! If you wanted to, you could
switch to a fixed number of decimal points:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table)
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100
    table.column(3).format = toyplot.format.FloatFormatter("{:.1f}")
    table.column(4).format = toyplot.format.FloatFormatter("{:.1f}")
    table.column(5).format = toyplot.format.FloatFormatter("{:.1f}")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-4d393bb8a3f5> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table)
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


Next, let's title our figure. Just like regular axes, table axes have a
``label`` property that can be set at construction time:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, label="Temperature Readings")
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-b51da9d63294> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table, label="Temperature Readings")
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


And although we don't recommend it, you can go crazy with gridlines:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, label="Temperature Readings")
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100
    table.grid.hlines[...] = "single"
    table.grid.vlines[...] = "single"
    table.grid.hlines[1,...] = "double"


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-b6d8e1badadf> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table, label="Temperature Readings")
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


... for a table with :math:`M` rows and :math:`N` columns, the
``table.grid.hlines`` matrix will control the appearance of
:math:`M+1 \times N` horizontal lines, while ``table.grid.vlines`` will
control :math:`M \times N+1` vertical lines. Use "single" for single
lines, "double" for double lines, or any value that evaluates to False
to hide the lines.

Suppose you wanted to highlight the observations in the dataset with the
highest high temperature and the lowest low temperature. You could do so
by changing the style of the given rows:

.. code:: python

    low_index = numpy.argsort(data_table["TMIN"])[0]
    high_index = numpy.argsort(data_table["TMAX"])[-1]
    
    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, label="Temperature Readings")
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100
    table.row(low_index).style = {"font-weight":"bold", "fill":"blue"}
    table.row(high_index).style = {"font-weight":"bold", "fill":"red"}


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-753ba029ab50> in <module>()
    ----> 1 low_index = numpy.argsort(data_table["TMIN"])[0]
          2 high_index = numpy.argsort(data_table["TMAX"])[-1]
          3 
          4 canvas = toyplot.Canvas(width=700, height=400)
          5 table = canvas.table(data_table, label="Temperature Readings")


    NameError: name 'data_table' is not defined


Wait a second ... those colored rows are both off-by-one! The actual
minimum and maximum values are in the rows immediately following the
colored rows. What happened? Note that the table has an "extra" row for
the column headers, so row zero in the data is actually row one in the
table, making the data rows "one-based" instead of "zero-based" the way
all good programmers are accustomed. We could fix the problem by
offsetting the indices we calculated from the raw data, but that would
be error-prone and annoying. The offset would also change if we ever
changed the number of header rows (we'll see how this is done in a
moment).

What we really need is a way to refer to the "header" rows and the
"body" rows in the table separately, using zero-based indices.
Fortunately, Toyplot does just that - we can use a pair of special
accessors to target our changes to the header or the body, using
coordinates that won't be affected by changes to other parts of the
table:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, label="Temperature Readings")
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100
    table.body.row(low_index).style = {"font-weight":"bold", "fill":"blue"}
    table.body.row(high_index).style = {"font-weight":"bold", "fill":"red"}


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-b536559588fe> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table, label="Temperature Readings")
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


Now the correct rows have been highlighted. Let's change the number of
header rows to verify that the highlighting isn't affected:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, hrows=2, label="Temperature Readings")
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100
    table.body.row(low_index).style = {"font-weight":"bold", "fill":"blue"}
    table.body.row(high_index).style = {"font-weight":"bold", "fill":"red"}


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-e52ad01ec3be> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table, hrows=2, label="Temperature Readings")
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


Sure enough, the correct rows are still highlighted, and while it isn't
obvious, the header does contain a second row. Let's make it obvious
with some grid lines, and provide some top-level labels of our own:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, hrows=2, label="Temperature Readings")
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100
    table.body.row(low_index).style = {"font-weight":"bold", "fill":"blue"}
    table.body.row(high_index).style = {"font-weight":"bold", "fill":"red"}
    table.header.grid.hlines[...] = "single"
    table.header.grid.vlines[...] = "single"
    table.header.cell(0, 0, colspan=2).merge().data = "Location"
    table.header.cell(0, 3, colspan=3).merge().data = u"Temperature \u00b0C"


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-b732f42356bd> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table, hrows=2, label="Temperature Readings")
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


Note that by accessing the grid via the "header" accessor, we were able
to easily set lines just for the header cells, and that we can use the
``data`` attribute to assign arbitrary cell contents, in this case to a
pair of merged header cells.

Also, you may have noticed that the merged cells took on the attributes
(alignment, style, etc.) of the cells that were merged, which is why the
"Location" label is left-justified, while the "Temperature" label is
centered. Let's center-justify the Location label, make both a little
more prominent, and lose the gridlines:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, hrows=2, label="Temperature Readings")
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 100
    table.body.row(low_index).style = {"font-weight":"bold", "fill":"blue"}
    table.body.row(high_index).style = {"font-weight":"bold", "fill":"red"}
    merged = table.header.cell(0, 0, colspan=2).merge()
    merged.data = "Location"
    merged.align = "center"
    merged.style = {"font-size":"14px"}
    merged = table.header.cell(0, 3, colspan=3).merge()
    merged.data = u"Temperature \u00b0C"
    merged.style = {"font-size":"14px"}


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-14-87a51471cd02> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table, hrows=2, label="Temperature Readings")
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 100


    NameError: name 'toyplot' is not defined


Finally, let's finish-off our grid by plotting the minimum and maximum
temperatures vertically along the right-hand side. This will provide an
intuitive guide to trends in the data. To do this, we'll add an extra
column to the table, merge it into a single cell, and then embed a set
of axes into the cell:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, columns=7, hrows=2, label="Temperature Readings")
    table.column(0).width = 150
    table.column(1).width = 150
    table.column(2).width = 70
    table.column(6).width = 80
    table.body.row(low_index).style = {"font-weight":"bold", "fill":"blue"}
    table.body.row(high_index).style = {"font-weight":"bold", "fill":"red"}
    merged = table.header.cell(0, 0, colspan=2).merge()
    merged.data = "Location"
    merged.align = "center"
    merged.style = {"font-size":"14px"}
    merged = table.header.cell(0, 3, colspan=3).merge()
    merged.data = u"Temperature \u00b0C"
    merged.style = {"font-size":"14px"}
    axes = table.body.column(6).merge().axes(show=False, padding=14)
    axes.plot(data_table["TMIN"][::-1], along="y", marker="o", color="blue", style={"stroke-width":1.0})
    axes.plot(data_table["TMAX"][::-1], along="y", marker="o", color="red", style={"stroke-width":1.0});


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-dc44ba91b92a> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700, height=400)
          2 table = canvas.table(data_table, columns=7, hrows=2, label="Temperature Readings")
          3 table.column(0).width = 150
          4 table.column(1).width = 150
          5 table.column(2).width = 70


    NameError: name 'toyplot' is not defined


Note that we hid the cartesian axes completely to avoid visual clutter,
and adjusted the axis padding to take-up just enough space in the merged
cell so the datum markers are aligned with the corresponding table rows.
Finally, note that we had to reverse the order of the plotted data
(using an index of ``[::-1]`` with the table columns) so the first datum
would be plotted at the top of the cell rather than the bottom, as would
be customary for a cartesian plot.

