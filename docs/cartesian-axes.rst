
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _cartesian-axes:

Cartesian Axes
==============

In Toyplot, :class:`cartesian axes<toyplot.axes.Cartesian>` provide a
traditional mapping of two-dimensional data values on the plane to
canvas coordinates. The axes *range* (the area on the canvas that they
occupy) is specified when they are created (see :ref:`canvas-layout`).
Their *domain* is implicitly defined to include all of the data in the
plot (but can be manually overridden by the caller if desired).

Cartesian axes are either created for you implicitly when using the
:ref:`convenience-api`:

.. code:: python

    import numpy
    y = numpy.linspace(0, 1, 20) ** 2

.. code:: python

    import toyplot
    canvas, axes, mark = toyplot.plot(y, width=300)


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-2-717cc21dfede> in <module>()
    ----> 1 import toyplot
          2 canvas, axes, mark = toyplot.plot(y, width=300)


    ImportError: No module named toyplot


... or explicitly using :meth:`toyplot.canvas.Canvas.axes`:

.. code:: python

    canvas = toyplot.Canvas(width=300)
    axes = canvas.axes()
    axes.plot(y);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-aa714fa8a256> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300)
          2 axes = canvas.axes()
          3 axes.plot(y);


    NameError: name 'toyplot' is not defined


Properties
----------

Axes objects contain sets of nested properties that can be used to
adjust behavior. The list of available properties includes the
following:

-  axes.show - set to *False* to hide the axes completely (the plotted
   data will still be visible).
-  axes.padding - a small gap between the axes and their contents.
   Defaults to CSS pixels, supports all :ref:`units`.
-  axes.label.text - optional label at the top of the axes.
-  axes.label.style - styles the axes label text.
-  axes.coordinates.show - set to *False* to disable interactive mouse
   coordinates.
-  axes.coordinates.style - styles the interactive mouse coordinates
   background.
-  axes.coordinates.label.style - styles the interactive mouse
   coordinates text.
-  axes.x.show - set to *False* to hide the X axis completely.
-  axes.x.scale - "linear", "log" (base 10), "log10", "log2", or a
   ("log", base) tuple.
-  axes.x.domain.min - override the minimum domain value for the axis.
-  axes.x.domain.max - override the maximum domain value for the axis.
-  axes.x.label.text - optional label below the X axis.
-  axes.x.label.style - styles the X axis label.
-  axes.x.spine.show - set to *False* to hide the X axis spine.
-  axes.x.spine.position - set to "low", "high", or a Y axis domain
   value to position the spine. Defaults to "low".
-  axes.x.spine.style - styles the X axis spine.
-  axes.x.ticks.show - set to *True* to display X axis tick marks.
-  axes.x.ticks.locator - assign an instance of
   :py:class:`toyplot.locator.Basic`,
   :py:class:`toyplot.locator.Explicit`,
   :py:class:`toyplot.locator.Extended`,
   :py:class:`toyplot.locator.Heckbert`, or
   :py:class:`toyplot.locator.Log` to control the positioning and
   formatting of ticks and tick labels. By default, an appropriate
   locator is automatically chosen based on the axis scale and domain.
-  axes.x.ticks.length - length of X axis ticks. Defaults to CSS pixels,
   supports all :ref:`units`.
-  axes.x.ticks.style - styles the X axis ticks.
-  axes.x.ticks.labels.show - set to *False* to hide X axis tick labels.
-  axes.x.ticks.labels.angle - set the angle of X axis tick labels in
   degrees.
-  axes.x.ticks.labels.offset - offsets labels from the axis. Defaults
   to CSS pixels, supports all :ref:`units`.
-  axes.x.ticks.labels.style - style X axis tick label text.
-  ... and equivalent properties for the Y axis.

In the following example we override several of the defaults:

.. code:: python

    x = numpy.linspace(0, 2 * numpy.pi)
    y = numpy.sin(x)

.. code:: python

    import toyplot.locator
    
    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes()
    axes.label.text = "Trigonometry 101"
    axes.x.label.text = "x"
    axes.y.label.text = "sin(x)"
    axes.x.ticks.show = True
    axes.x.ticks.locator = toyplot.locator.Explicit(
        [0, numpy.pi / 2, numpy.pi, 3 * numpy.pi / 2, 2 * numpy.pi],
        ["0", u"\u03c0 / 2", u"\u03c0", u"3 \u03c0 / 2", u"2 \u03c0"])
    mark = axes.plot(x, y)


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-5-5610908d5b0c> in <module>()
    ----> 1 import toyplot.locator
          2 
          3 canvas = toyplot.Canvas(width=600, height=300)
          4 axes = canvas.axes()
          5 axes.label.text = "Trigonometry 101"


    ImportError: No module named toyplot.locator


As a convenience, some of the most common properties can also be set
when the axes are created:

.. code:: python

    x = numpy.linspace(0, 10, 100)
    y = 40 + x ** 2

.. code:: python

    canvas = toyplot.Canvas(300, 300)
    axes = canvas.axes(label="Toyplot Users", xlabel="Days", ylabel="Users")
    mark = axes.plot(x, y)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-609820878bc6> in <module>()
    ----> 1 canvas = toyplot.Canvas(300, 300)
          2 axes = canvas.axes(label="Toyplot Users", xlabel="Days", ylabel="Users")
          3 mark = axes.plot(x, y)


    NameError: name 'toyplot' is not defined


And the same properties can be used with the :ref:`convenience-api`,
as in the following example where we specify a minimum value for an axis
- for example, if we wanted the previous figure to include
:math:`y = 0`:

.. code:: python

    toyplot.plot(x, y, label="Toyplot Users", xlabel="Days", ylabel="Users", ymin=0, width=300);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-ba8ec2ce33c5> in <module>()
    ----> 1 toyplot.plot(x, y, label="Toyplot Users", xlabel="Days", ylabel="Users", ymin=0, width=300);
    

    NameError: name 'toyplot' is not defined


Scale
-----

An important property of each axis is its scale, used to specify linear
or logarithmic mappings from *domain* to *range*:

.. code:: python

    x = numpy.linspace(-1000, 1000)

.. code:: python

    canvas = toyplot.Canvas(width=700)
    
    axes = canvas.axes(grid=(2, 2, 0, 0), xscale="linear", yscale="linear")
    axes.plot(x, x, marker="o")
    
    axes = canvas.axes(grid=(2, 2, 0, 1), xscale="log", yscale="linear")
    axes.plot(x, x, marker="o")
    
    axes = canvas.axes(grid=(2, 2, 1, 0), xscale="linear", yscale="log")
    axes.plot(x, x, marker="o")
    
    axes = canvas.axes(grid=(2, 2, 1, 1), xscale="log", yscale="log")
    axes.plot(x, x, marker="o");


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-8e9d86fd7fae> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700)
          2 
          3 axes = canvas.axes(grid=(2, 2, 0, 0), xscale="linear", yscale="linear")
          4 axes.plot(x, x, marker="o")
          5 


    NameError: name 'toyplot' is not defined


Note that Toyplot handles negative values correctly, and provides
sensible results for values near zero by rendering them using a small
linear region around the origin.

The scale can be specified in two ways:

-  As a string - "linear", "log" (base 10), "log10" (base 10), or "log2"
   (base 2).
-  As a tuple - ("log", 2), ("log", 10).

For example, the following are all equivalent

.. code:: python

    canvas = toyplot.Canvas(width=700)
    axes = canvas.axes(grid=(2,2,0), xscale="log")
    axes.plot(x, x)
    axes = canvas.axes(grid=(2,2,1), xscale="log10")
    axes.plot(x, x)
    axes = canvas.axes(grid=(2,2,2), xscale=("log", 10))
    axes.plot(x, x);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-8d6d71033a0d> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=700)
          2 axes = canvas.axes(grid=(2,2,0), xscale="log")
          3 axes.plot(x, x)
          4 axes = canvas.axes(grid=(2,2,1), xscale="log10")
          5 axes.plot(x, x)


    NameError: name 'toyplot' is not defined


Of course, you are free to specify any base you like, using the tuple
notation:

.. code:: python

    toyplot.plot(x, x, xscale=("log", 4), width=400);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-6a12a9f97ea6> in <module>()
    ----> 1 toyplot.plot(x, x, xscale=("log", 4), width=400);
    

    NameError: name 'toyplot' is not defined


