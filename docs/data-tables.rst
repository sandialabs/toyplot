
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _data-tables:

Data Tables
===========

Data tables, with *rows* containing *observations* and *columns*
containing *variables* or *series*, are arguably the cornerstone of
science. Much of the functionality of Toyplot or any other plotting
package can be reduced to a process of mapping data series from tables
to properties like coordinates and colors. To facilitate this, Toyplot
provides :class:`toyplot.data.Table` - an ordered, heterogeneous
collection of named, equal-length *columns*, where each column is a
Numpy *masked array*. Toyplot data tables are used for internal storage
and manipulation by all of the individual types of plot, and can be
useful for managing data prior to ingestion into Toyplot.

Be careful not to confuse the data tables described in this section with
:ref:`table-axes`, which are used to visualize tabular data.

.. code:: python

    import toyplot.data
    import numpy


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-59967ba4e40c> in <module>()
    ----> 1 import toyplot.data
          2 import numpy


    ImportError: No module named toyplot.data


.. code:: python

    table = toyplot.data.Table()
    table["x"] = numpy.arange(10)
    table["x*2"] = table["x"] * 2
    table["x^2"] = table["x"] ** 2
    table


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-502a6af714e6> in <module>()
    ----> 1 table = toyplot.data.Table()
          2 table["x"] = numpy.arange(10)
          3 table["x*2"] = table["x"] * 2
          4 table["x^2"] = table["x"] ** 2
          5 table


    NameError: name 'toyplot' is not defined


You can see from this small example that Toyplot tables provide
automatic pretty-printing when used with Jupyter notebooks, like other
Toyplot objects (Jupyter pretty-printing is provided as a convenience -
to create tabular data graphics, you will likely want the additional
control provided by :ref:`table-axes`).

Tables behave much like Python dicts, allowing you to assign and access
columns using indexing notation with column names. The ``keys()``,
``values()``, and ``items()`` methods also act like their standard
library counterparts, providing column-oriented access to the table
contents ... but note that, unlike a normal Python dict, a Toyplot table
remembers the order in which columns were added to the table, and always
returns them in the same order:

.. code:: python

    for name in table.keys():
        print name


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-31747e4febf2> in <module>()
    ----> 1 for name in table.keys():
          2     print name


    NameError: name 'table' is not defined


.. code:: python

    for column in table.values():
        print column


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-d7555a39873d> in <module>()
    ----> 1 for column in table.values():
          2     print column


    NameError: name 'table' is not defined


.. code:: python

    for name, column in table.items():
        print name, column


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-3587923f920d> in <module>()
    ----> 1 for name, column in table.items():
          2     print name, column


    NameError: name 'table' is not defined


However, tables also behave similarly to Python lists, providing length
and slicing operations for row-oriented access to their contents:

.. code:: python

    len(table)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-bfb8bb9a6394> in <module>()
    ----> 1 len(table)
    

    NameError: name 'table' is not defined


.. code:: python

    table[2:5]


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-e1ab09316fc8> in <module>()
    ----> 1 table[2:5]
    

    NameError: name 'table' is not defined


Note from above that slicing a table returns another table, with the
same set of columns but fewer rows. Similarly, you can create a new
table using a subset of an existing table's columns:

.. code:: python

    table.columns(["x*2", "x"])


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-05470d7b54ee> in <module>()
    ----> 1 table.columns(["x*2", "x"])
    

    NameError: name 'table' is not defined


... this also allows you to reorder the columns in a table.

Finally, as a convenience for documentation and tutorials only, Toyplot
provides basic functionality to load a table from a CSV file - but
please note that Toyplot is emphatically *not* a data manipulation
library! For real work you should use the Python standard library
:mod:`csv` module to load data, or functionality provided by libraries
such as ``Numpy`` or ``Pandas``.

In the following example, we load a set of temperature readings:

.. code:: python

    table = toyplot.data.read_csv("temperatures.csv")
    table[0:10]


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-0c96fcf46d76> in <module>()
    ----> 1 table = toyplot.data.read_csv("temperatures.csv")
          2 table[0:10]


    NameError: name 'toyplot' is not defined


Then, we convert the readings from Celsius to Fahrenheit and plot them
over time:

.. code:: python

    table["TMAX_F"] = ((table["TMAX"].astype("float64") * 0.1) * 1.8) + 32
    table["TMIN_F"] = ((table["TMIN"].astype("float64") * 0.1) * 1.8) + 32


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-9fb5649efc2c> in <module>()
    ----> 1 table["TMAX_F"] = ((table["TMAX"].astype("float64") * 0.1) * 1.8) + 32
          2 table["TMIN_F"] = ((table["TMIN"].astype("float64") * 0.1) * 1.8) + 32


    NameError: name 'table' is not defined


.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes(xlabel="Day", ylabel=u"Temperature \u00b0F")
    axes.plot(table["TMAX_F"], color="red", stroke_width=1)
    axes.plot(table["TMIN_F"], color="blue", stroke_width=1);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-a73fe7917563> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=600, height=300)
          2 axes = canvas.axes(xlabel="Day", ylabel=u"Temperature \u00b0F")
          3 axes.plot(table["TMAX_F"], color="red", stroke_width=1)
          4 axes.plot(table["TMIN_F"], color="blue", stroke_width=1);


    NameError: name 'toyplot' is not defined


