
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _canvas-layout:

Canvas Layout
=============

In Toyplot, ``axes`` (including :ref:`cartesian-axes`,
:ref:`table-axes`, and others) are used to map data values into canvas
coordinates. The axes *range* (the area on the canvas that they occupy)
is specified when they are created. By default, axes are sized to fill
the entire canvas:

.. code:: python

    import numpy
    y = numpy.linspace(0, 1, 20) ** 2

.. code:: python

    import toyplot
    toyplot.plot(y, width=300);


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-2-878d16a49021> in <module>()
    ----> 1 import toyplot
          2 toyplot.plot(y, width=300);


    ImportError: No module named toyplot


If you need greater control over the positioning of the axes within the
canvas, or want to add multiple axes to one canvas, it's necessary to
create the canvas and axes explicitly, then use the axes to plot your
data. For example, you can use the *bounds* argument to specify explicit
(xmin, xmax, ymin, ymax) bounds for the axes using canvas coordinates
(note that canvas coordinates always *increase* from top to bottom,
unlike cartesian coordinates):

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(bounds=(20, 280, 20, 280))
    axes1.plot(y)
    axes2 = canvas.axes(bounds=(320, 580, 20, 280))
    axes2.plot(1 - y);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-a1f6f91064d1> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=600, height=300)
          2 axes1 = canvas.axes(bounds=(20, 280, 20, 280))
          3 axes1.plot(y)
          4 axes2 = canvas.axes(bounds=(320, 580, 20, 280))
          5 axes2.plot(1 - y);


    NameError: name 'toyplot' is not defined


You can also use *negative* values to specify values relative to the
right and bottom sides of the canvas, instead of the (default) left and
top sides, greatly simplifying the layout:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(bounds=(20, 280, 20, -20))
    axes1.plot(y)
    axes2 = canvas.axes(bounds=(-280, -20, 20, -20))
    axes2.plot(1 - y);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-174255bd925d> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=600, height=300)
          2 axes1 = canvas.axes(bounds=(20, 280, 20, -20))
          3 axes1.plot(y)
          4 axes2 = canvas.axes(bounds=(-280, -20, 20, -20))
          5 axes2.plot(1 - y);


    NameError: name 'toyplot' is not defined


Furthermore, the bounds parameters can use any :ref:`units`, including
"%" units, so you can use real-world units and relative dimensioning in
any combination that makes sense:

.. code:: python

    canvas = toyplot.Canvas(width="20cm", height="2in")
    axes1 = canvas.axes(bounds=("1cm", "5cm", "10%", "90%"))
    axes1.plot(y)
    axes2 = canvas.axes(bounds=("6cm", "-1cm", "10%", "90%"))
    axes2.plot(1 - y);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-5e2b3f818f83> in <module>()
    ----> 1 canvas = toyplot.Canvas(width="20cm", height="2in")
          2 axes1 = canvas.axes(bounds=("1cm", "5cm", "10%", "90%"))
          3 axes1.plot(y)
          4 axes2 = canvas.axes(bounds=("6cm", "-1cm", "10%", "90%"))
          5 axes2.plot(1 - y);


    NameError: name 'toyplot' is not defined


Of course, most of the time this level of control isn't necessary.
Instead, the *grid* argument allows us to easily position each set of
axes on a regular grid that covers the canvas. Note that you can control
the axes position on the grid in a variety of ways:

-  (rows, columns, n)

   -  fill cell :math:`n` (in left-to-right, top-to-bottom order) of an
      :math:`M \times N` grid.

-  (rows, columns, i, j)

   -  fill cell :math:`i,j` of an :math:`M \times N` grid.

-  (rows, columns, i, rowspan, j, colspan)

   -  fill cells :math:`[i, i + rowspan), [j, j + colspan)` of an
      :math:`M \times N` grid.

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(grid=(1, 2, 0))
    axes1.plot(y)
    axes2 = canvas.axes(grid=(1, 2, 1))
    axes2.plot(1 - y);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-5e4b5d9d5168> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=600, height=300)
          2 axes1 = canvas.axes(grid=(1, 2, 0))
          3 axes1.plot(y)
          4 axes2 = canvas.axes(grid=(1, 2, 1))
          5 axes2.plot(1 - y);


    NameError: name 'toyplot' is not defined


You can also use the *gutter* argument to control the space between
cells in the grid:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(grid=(1, 2, 0), gutter=15)
    axes1.plot(y)
    axes2 = canvas.axes(grid=(1, 2, 1), gutter=15)
    axes2.plot(1 - y);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-0b35ef816d70> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=600, height=300)
          2 axes1 = canvas.axes(grid=(1, 2, 0), gutter=15)
          3 axes1.plot(y)
          4 axes2 = canvas.axes(grid=(1, 2, 1), gutter=15)
          5 axes2.plot(1 - y);


    NameError: name 'toyplot' is not defined


Sometimes, particularly when embedding axes to produce a
figure-within-a-figure, the *corner* argument can be used to position
axes relative to one of eight "corner" positions within the canvas. The
corner argument takes a (position, inset, width, height) tuple:

.. code:: python

    x = numpy.random.normal(size=100)
    y = numpy.random.normal(size=100)

.. code:: python

    canvas = toyplot.Canvas(width="5in")
    canvas.axes().plot(numpy.linspace(0, 1) ** 0.5)
    canvas.axes(corner=("bottom-right", "1in", "1.5in", "1.5in")).scatterplot(x, y);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-d05525492329> in <module>()
    ----> 1 canvas = toyplot.Canvas(width="5in")
          2 canvas.axes().plot(numpy.linspace(0, 1) ** 0.5)
          3 canvas.axes(corner=("bottom-right", "1in", "1.5in", "1.5in")).scatterplot(x, y);


    NameError: name 'toyplot' is not defined


Here are all the positions supported by the *corner* argument:

.. code:: python

    canvas = toyplot.Canvas(width="10cm")
    for position in ["top-left", "top", "top-right", "right", "bottom-right", "bottom", "bottom-left", "left"]:
        canvas.axes(corner=(position, "1cm", "2cm", "2cm"), label=position)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-96974f0e4d7b> in <module>()
    ----> 1 canvas = toyplot.Canvas(width="10cm")
          2 for position in ["top-left", "top", "top-right", "right", "bottom-right", "bottom", "bottom-left", "left"]:
          3     canvas.axes(corner=(position, "1cm", "2cm", "2cm"), label=position)


    NameError: name 'toyplot' is not defined

