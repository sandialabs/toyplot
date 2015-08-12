
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _labels-and-legends:

Labels and Legends
==================

Of course, most figures require proper labels before they can be of
value, so Toyplot provides several labelling mechanisms to help:

Axes Labels
-----------

First, both :ref:`cartesian-axes` and :ref:`table-axes` provide
labelling parameters that can be specified when they are created. In
either case the ``label`` parameter provides a top-level label for the
set of axes:

.. code:: python

    import numpy
    import toyplot
    
    canvas = toyplot.Canvas(width=600, height=300)
    canvas.axes(grid=(1,2,0), label="Cartesian Axes").plot(numpy.linspace(0, 1)**2)
    canvas.table(grid=(1,2,1), label="Table Axes", data = numpy.random.random((4, 3)));


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-935eb36c469c> in <module>()
          1 import numpy
    ----> 2 import toyplot
          3 
          4 canvas = toyplot.Canvas(width=600, height=300)
          5 canvas.axes(grid=(1,2,0), label="Cartesian Axes").plot(numpy.linspace(0, 1)**2)


    ImportError: No module named toyplot


Naturally, some axes - such as Cartesian axes - allow you to specify
additional, axis-specific labels:

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes(label="Cartesian Axes", xlabel="Days", ylabel="Users")
    axes.plot(numpy.linspace(0, 1)**2);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-ac2c16112477> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, height=300)
          2 axes = canvas.axes(label="Cartesian Axes", xlabel="Days", ylabel="Users")
          3 axes.plot(numpy.linspace(0, 1)**2);


    NameError: name 'toyplot' is not defined


Axes Text
---------

Another option for labelling a plot is to insert text labels using the
same domain as the data:

.. code:: python

    def series(x):
        return numpy.cumsum(numpy.random.normal(loc=0.05, size=len(x)))
    
    numpy.random.seed(1234)
    x = numpy.arange(100)
    y = numpy.column_stack([series(x) for i in range(5)])

.. code:: python

    label_style = {"text-anchor":"start", "-toyplot-anchor-shift":"5px"}
    canvas, axes, mark = toyplot.plot(x, y)
    for i in range(y.shape[1]):
        axes.text(x[-1], y[-1,i], "Series %s" % i, style=label_style)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-7ba4aab28ce6> in <module>()
          1 label_style = {"text-anchor":"start", "-toyplot-anchor-shift":"5px"}
    ----> 2 canvas, axes, mark = toyplot.plot(x, y)
          3 for i in range(y.shape[1]):
          4     axes.text(x[-1], y[-1,i], "Series %s" % i, style=label_style)


    NameError: name 'toyplot' is not defined


Note that we are using the last coordinate in each series as the text
label coordinate - by default, Toyplot renders text centered on its
coordinate, so in this case we've chosen a text style that left-aligns
the text and offsets it slightly for clarity.

Canvas Text
-----------

When adding text to axes, you specify the text coordinates using the
same domain as your data. Naturally, this limits the added text to the
bounds defined by the axes. For the ultimate in labeling flexibility,
you can add text to the canvas directly, using canvas units, outside
and/or overlapping axes:

.. code:: python

    label_style={"font-size":"18px", "font-weight":"bold"}
    
    canvas = toyplot.Canvas(width=600, height=300)
    canvas.axes(grid=(1,2,0)).plot(numpy.linspace(1, 0)**2)
    canvas.axes(grid=(1,2,1), yshow=False).plot(numpy.linspace(0, 1)**2)
    canvas.text(300, 120, "This label overlaps two sets of axes!", style=label_style);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-addbc225d458> in <module>()
          1 label_style={"font-size":"18px", "font-weight":"bold"}
          2 
    ----> 3 canvas = toyplot.Canvas(width=600, height=300)
          4 canvas.axes(grid=(1,2,0)).plot(numpy.linspace(1, 0)**2)
          5 canvas.axes(grid=(1,2,1), yshow=False).plot(numpy.linspace(0, 1)**2)


    NameError: name 'toyplot' is not defined


Please keep in mind when placing labels in canvas coordinates that,
unlike Cartesian coordinates, canvas coordinates increase from
top-to-bottom.

Canvas Legends
--------------

Last-but-not-least, Toyplot provides (currently experimental) support
for graphical legends:

.. code:: python

    observations = numpy.random.power(2, size=(50, 50))
    
    x = numpy.arange(len(observations))
    
    boundaries = numpy.column_stack(
        (numpy.min(observations, axis=1),
         numpy.percentile(observations, 25, axis=1),
         numpy.percentile(observations, 50, axis=1),
         numpy.percentile(observations, 75, axis=1),
         numpy.max(observations, axis=1)))
    
    fill = ["blue", "blue", "red", "red"]
    opacity = [0.1, 0.2, 0.2, 0.1]
    
    canvas = toyplot.Canvas(800, 400)
    axes = canvas.axes(grid=(1,5,0,1,0,4))
    fill = axes.fill(x, boundaries, fill=fill, opacity=opacity)
    mean = axes.plot(x, numpy.mean(observations, axis=1), color="blue")
    
    canvas.legend([
        ("Mean", mean),
        ("First Quartile", "rect", {"fill":"blue", "opacity":0.1}),
        ("Second Quartile", "rect", {"fill":"blue", "opacity":0.2}),
        ("Third Quartile", "rect", {"fill":"red", "opacity":0.2}),
        ("Fourth Quartile", "rect", {"fill":"red", "opacity":0.1}),
        ],
        corner=("right", 100, 100, 125),
        );



::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-01797081633c> in <module>()
         13 opacity = [0.1, 0.2, 0.2, 0.1]
         14 
    ---> 15 canvas = toyplot.Canvas(800, 400)
         16 axes = canvas.axes(grid=(1,5,0,1,0,4))
         17 fill = axes.fill(x, boundaries, fill=fill, opacity=opacity)


    NameError: name 'toyplot' is not defined


The call to :func:`toyplot.canvas.Canvas.legend` always includes an
explicit list of items to add to the legend, plus a
:ref:`canvas-layout` specification of where the layout should appear
on the canvas. Currently, each item to be displayed should be either:

-  A (label, mark) tuple, which will get its appearance from the mark,
   or:
-  A (label, marker, style) tuple, which will render the given marker
   with the given style.

Of course, ``label`` is the text to be displayed next to an item in the
legend, while ``mark`` is a mark that has been added to the canvas.
However, not all marks can provide an unambiguous legend representation
- what to do when a mark represents multiple series, or has per-datum
colors, markers, or styles? In these cases there isn't a one-to-one
correspondence between marks and legend items, leading to the second
form of legend item with explicit ``marker`` and ``style`` parameters.
The ``marker`` parameter currently can be any of the following:

-  "line" - draw a line in the same style that would be used for a line
   plot.
-  "rect" - draw a filled rect in the same style that would be used for
   a fill plot.
-  marker - draw a marker shape using any of the :ref:`markers` that
   are available for line and scatter plots.

As is the case throughout Toyplot, the ``style`` parameter uses CSS
styles to control the appearance of the item.

There are some subtleties here worth noting, many of which are driven by
Toyplot's deliberate embrace of the philosophy that *explicit is better
than implicit*:

-  You can have as many or as few legends on your canvas as you like.
-  Callers explicitly specify the order and contents of each legend.
-  There is no relationship between axes and legends - you could combine
   marks from multiple axes in a single legend, for example.

Here's an example of all these ideas at work:

.. code:: python

    x = numpy.linspace(0, 1)
    y1 = (1 - x) ** 2
    y2 = numpy.column_stack((1 - (x ** 2), x ** 2))
    
    canvas = toyplot.Canvas(width=600, height=300)
    m1 = canvas.axes(grid=(1,2,0), gutter=15).scatterplot(x, y1, marker="o", color="rgb(255,0,0)")
    m2 = canvas.axes(grid=(1,2,1), gutter=15, yshow=False).scatterplot(x, y2, marker="s", color=["green", "blue"])
    
    canvas.legend([
        ("Experiment 1", "o", {"fill":"rgb(255,0,0)", "stroke": "none"}),
        ("Experiment 2", "s", {"fill":"green", "stroke": "none"}),
        ("Experiment 3", "s", {"fill":"blue", "stroke": "none"}),
    
        ],
        corner=("top", 100, 100, 70),
        );
    



::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-3161d49fcfcf> in <module>()
          3 y2 = numpy.column_stack((1 - (x ** 2), x ** 2))
          4 
    ----> 5 canvas = toyplot.Canvas(width=600, height=300)
          6 m1 = canvas.axes(grid=(1,2,0), gutter=15).scatterplot(x, y1, marker="o", color="rgb(255,0,0)")
          7 m2 = canvas.axes(grid=(1,2,1), gutter=15, yshow=False).scatterplot(x, y2, marker="s", color=["green", "blue"])


    NameError: name 'toyplot' is not defined


