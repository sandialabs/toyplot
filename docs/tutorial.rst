
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
The Toyplot Tutorial
====================

Getting Started
---------------

Welcome! This tutorial will introduce you to the basics of working with
Toyplot.

Note: this tutorial was created in a
`Jupyter <http://www.ipython.org>`__ notebook and assumes that you're
following-along in a notebook of your own. If you aren't using a
notebook, you should read the user guide section on :ref:`rendering`
for some important information on how to display your figures.

To begin, we're going to import numpy (so we can create data to use for
our figures), and the main toyplot module:

.. code:: python

    import numpy
    import toyplot


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-c5ec9c1ff9f0> in <module>()
          1 import numpy
    ----> 2 import toyplot
    

    ImportError: No module named toyplot


For our first figure, let's create a simple set of X and Y coordinates
that we can plot:

.. code:: python

    x = numpy.linspace(0, 10)
    y = x ** 2

Now, let's put Toyplot to work ...

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes()
    mark = axes.plot(x, y)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-808f6ac3d3ca> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, height=300)
          2 axes = canvas.axes()
          3 mark = axes.plot(x, y)


    NameError: name 'toyplot' is not defined


Short as it is, this example demonstrates several key features of
Toyplot:

-  Toyplot figures are beautiful, scalable, embeddable, and interactive.
   For example:

   -  Mouse over the figure, and note the cursor coordinates that update
      in the upper-right-hand corner.
   -  Carefully place the cursor on top of the plotted line, and open a
      context menu - in the popup that appears, you can choose to save
      the figure data to a CSV file from your browser.
   -  Note that Toyplot produces a clean, aesthetically pleasing figure
      that is crisp at any scale and free of chartjunk "out-of-the-box".

-  Every Toyplot figure begins with a
   :class:`canvas <toyplot.canvas.Canvas>` - a drawing area upon which
   the caller adds *marks*. Note that the width and height of the canvas
   have been specified in *CSS pixels*, which are always equal to 1/96th
   of an inch, and converted to device units when the canvas is
   :ref:`rendered <rendering>`.
-  A Toyplot figure typically contains one-or-more sets of
   :class:`axes <toyplot.axes.Cartesian>` which map a data *domain* to
   a *range* of canvas pixels.
-  Marks are added to axes using factory functions provided by the axes.
   In this example, the :meth:`plot <toyplot.axes.Cartesian.plot>`
   function adds a :class:`plot <toyplot.mark.Plot>` mark using the
   supplied coordinates. Note that the axes have been automatically
   sized to the data's domain.

Styles
------

Let's say that you wanted to alter the above figure to make the plotted
line blue and dashed. To do so, simply override the default *style*
information when creating the plot:

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes()
    mark = axes.plot(x, y, style={"stroke":"blue", "stroke-dasharray":"2, 2"})


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-22d21c28c5e7> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, height=300)
          2 axes = canvas.axes()
          3 mark = axes.plot(x, y, style={"stroke":"blue", "stroke-dasharray":"2, 2"})


    NameError: name 'toyplot' is not defined


In this case, you can see that the style information is a dictionary of
key-value properties that alter how a mark is rendered. To avoid
reinventing the wheel, Toyplot uses `Cascading Style Sheets
(CSS) <https://developer.mozilla.org/en-US/docs/Web/CSS>`__ to specify
styles. If you're familiar with web development, you already know CSS.
If not, this tutorial will cover many of most useful CSS properties for
Toyplot as we go, and there are many learning resources for CSS online.

Every mark you add to a figure will have at least one (and possibly more
than one) set of styles that control its appearance.

Plotting
--------

Let's continue with the previous example. As a shortcut, you can omit
the X coordinates when using the
:func:`plot <toyplot.axes.Cartesian.plot>` command, and a set of
coordinates in the range :math:`[0, M)` will be provided (compare the
following X axis with the previous two plots to see the difference):

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes()
    mark = axes.plot(y)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-93f8e4ae779f> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, height=300)
          2 axes = canvas.axes()
          3 mark = axes.plot(y)


    NameError: name 'toyplot' is not defined


If you add multiple plots, each automatically receives a different
color:

.. code:: python

    x = numpy.linspace(0, 10, 100)
    y1 = numpy.sin(x)
    y2 = numpy.cos(x)
    y3 = numpy.sin(x) + numpy.cos(x)

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes()
    mark1 = axes.plot(x, y1)
    mark2 = axes.plot(x, y2)
    mark3 = axes.plot(x, y3)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-b403e44a763b> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=600, height=300)
          2 axes = canvas.axes()
          3 mark1 = axes.plot(x, y1)
          4 mark2 = axes.plot(x, y2)
          5 mark3 = axes.plot(x, y3)


    NameError: name 'toyplot' is not defined


As we've already seen, we can use the "stroke" style to override the
default color of each plot; in addition, the "stroke-width" and
"stroke-opacity" styles are useful properties for (de)emphasizing
individual plots:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes()
    mark1 = axes.plot(x, y1, style={"stroke-width":1, "stroke-opacity":0.6})
    mark2 = axes.plot(x, y2, style={"stroke-width":1, "stroke-opacity":0.6})
    mark3 = axes.plot(x, y3, style={"stroke":"blue"})


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-00567e0dce7e> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=600, height=300)
          2 axes = canvas.axes()
          3 mark1 = axes.plot(x, y1, style={"stroke-width":1, "stroke-opacity":0.6})
          4 mark2 = axes.plot(x, y2, style={"stroke-width":1, "stroke-opacity":0.6})
          5 mark3 = axes.plot(x, y3, style={"stroke":"blue"})


    NameError: name 'toyplot' is not defined


Palettes
--------

Before proceeding, let's take a moment to look at how the default color
for a mark is assigned. When we add multiple marks to a set of axes,
each mark gets a different color. These default colors are all drawn
from a :class:`palette <toyplot.color.Palette>` - an ordered
collection of RGBA colors. For example, here's Toyplot's default
palette:

.. code:: python

    import toyplot.color
    toyplot.color.Palette()


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-9-594bc2e88ee5> in <module>()
    ----> 1 import toyplot.color
          2 toyplot.color.Palette()


    ImportError: No module named toyplot.color


Note: Like canvases, palettes are automatically rendered in Jupyter
notebooks, in this case as a collection of color swatches.

You should observe that the order of colors in the palette match the
order of the colors that were assigned to our plots as they were added
to their axes. You could create a custom palette by passing a sequence
of colors to the :class:`toyplot.color.Palette` constructor, but
Toyplot already comes with a builtin collection of high-quality palettes
from `Color Brewer <http://colorbrewer2.org>`__, which we will use in
the examples that follow.

For more detail on colors in Toyplot, see the :ref:`color` section of
the user guide.

Filled Regions
--------------

You can use :meth:`fill<toyplot.axes.Cartesian.fill>` to display a
region bounded by two sets of Y coordinates. This can be a handy way to
visualize data distributions:

.. code:: python

    numpy.random.seed(1234)
    observations = numpy.random.normal(size=(50, 50))
    
    x = numpy.linspace(0, 1, len(observations))
    y1 = numpy.min(observations, axis=1)
    y2 = numpy.max(observations, axis=1)

.. code:: python

    canvas = toyplot.Canvas(width=400, height=300)
    axes = canvas.axes()
    mark = axes.fill(x, y1, y2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-34207d8e83e1> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=400, height=300)
          2 axes = canvas.axes()
          3 mark = axes.fill(x, y1, y2)


    NameError: name 'toyplot' is not defined


Use the "fill" style (not to be confused with the fill command) to
control the color of the shaded region. You might also want to change
the fill-opacity or add a stroke using styles:

.. code:: python

    canvas = toyplot.Canvas(width=400, height=300)
    axes = canvas.axes()
    mark = axes.fill(x, y1, y2, style={"fill":"steelblue", "fill-opacity":0.5, "stroke":toyplot.color.near_black})


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-ed9e3bf805fc> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=400, height=300)
          2 axes = canvas.axes()
          3 mark = axes.fill(x, y1, y2, style={"fill":"steelblue", "fill-opacity":0.5, "stroke":toyplot.color.near_black})


    NameError: name 'toyplot' is not defined


If you omit one of the boundaries it will default to :math:`y = 0`:

.. code:: python

    canvas = toyplot.Canvas(width=400, height=300)
    axes = canvas.axes()
    mark = axes.fill(x, y2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-37ae9acab1c7> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=400, height=300)
          2 axes = canvas.axes()
          3 mark = axes.fill(x, y2)


    NameError: name 'toyplot' is not defined


As with plots, if you omit the X coordinates, they will default to the
range :math:`[0, M)`:

.. code:: python

    canvas = toyplot.Canvas(width=400, height=300)
    axes = canvas.axes()
    mark = axes.fill(y2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-14-36509c76ca47> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=400, height=300)
          2 axes = canvas.axes()
          3 mark = axes.fill(y2)


    NameError: name 'toyplot' is not defined


Toyplot also makes it easy to define multiple sets of boundaries, by
passing an :math:`M \times N` matrix as input, where :math:`M` is the
number of observations, and :math:`N` is the number of boundaries:

.. code:: python

    boundaries = numpy.column_stack(
        (numpy.min(observations, axis=1),
         numpy.percentile(observations, 25, axis=1),
         numpy.percentile(observations, 50, axis=1),
         numpy.percentile(observations, 75, axis=1),
         numpy.max(observations, axis=1)))

.. code:: python

    canvas = toyplot.Canvas(width=400, height=300)
    axes = canvas.axes()
    mark = axes.fill(boundaries)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-44b8170b71fc> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=400, height=300)
          2 axes = canvas.axes()
          3 mark = axes.fill(boundaries)


    NameError: name 'toyplot' is not defined


This introduces an important new concept: you can think of fill (and
other types of) marks as containers for collections of *series*, where
in this case, :math:`N` boundaries define :math:`N-1` series.

This distinction is important because we can control the styles of
individual series, not just the mark as a whole. So, if we want to
override the default colors for the fill regions, we can do it using the
mark's global "fill" style (with a contrasting stroke to display the
boundaries between series):

.. code:: python

    canvas = toyplot.Canvas(width=400, height=300)
    axes = canvas.axes()
    mark = axes.fill(boundaries, style={"fill":"steelblue", "stroke":"white"})


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-ac9e748e91a6> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=400, height=300)
          2 axes = canvas.axes()
          3 mark = axes.fill(boundaries, style={"fill":"steelblue", "stroke":"white"})


    NameError: name 'toyplot' is not defined


... or we can do it using the "fill" argument:

.. code:: python

    canvas = toyplot.Canvas(width=400, height=300)
    axes = canvas.axes()
    mark = axes.fill(boundaries, fill="steelblue", style={"stroke":"white"})


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-eb662e639b08> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=400, height=300)
          2 axes = canvas.axes()
          3 mark = axes.fill(boundaries, fill="steelblue", style={"stroke":"white"})


    NameError: name 'toyplot' is not defined


The advantage of the latter is that the "fill" argument can specify a
single color value as we've seen, or a sequence of color values,
one-per-series. And, you can combine those per-series fill values with
global styles in intuitive ways:

.. code:: python

    fill = ["red", "green", "blue", "yellow"]

.. code:: python

    canvas = toyplot.Canvas(width=400, height=300)
    axes = canvas.axes()
    mark = axes.fill(boundaries, fill=fill, style={"stroke":toyplot.color.near_black})


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-1a5311126d38> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=400, height=300)
          2 axes = canvas.axes()
          3 mark = axes.fill(boundaries, fill=fill, style={"stroke":toyplot.color.near_black})


    NameError: name 'toyplot' is not defined


The "opacity" and "title" arguments can also be specified on a
per-series basis (hover the mouse over the fill regions in the following
figure to see the title as a popup):

.. code:: python

    fill = ["blue", "blue", "red", "red"]
    opacity = [0.1, 0.2, 0.2, 0.1]
    title = ["1st Quartile", "2nd Quartile", "3rd Quartile", "4th Quartile"]

.. code:: python

    canvas = toyplot.Canvas(width=400, height=300)
    axes = canvas.axes()
    mark = axes.fill(boundaries, fill=fill, opacity=opacity, title=title, style={"stroke":toyplot.color.near_black})


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-22-448524a89f0f> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=400, height=300)
          2 axes = canvas.axes()
          3 mark = axes.fill(boundaries, fill=fill, opacity=opacity, title=title, style={"stroke":toyplot.color.near_black})


    NameError: name 'toyplot' is not defined


In the preceding examples you defined the fill regions by explicitly
specifying their *boundaries* ... as an alternative, you can generate
fills by specifying the *magnitudes* (the heights) of each region (note
that in this case :math:`N` heights define :math:`N` series):

.. code:: python

    numpy.random.seed(1234)
    
    heights = []
    x = numpy.linspace(0, 4 * numpy.pi, 100)
    for i in range(10):
        heights.append(numpy.random.uniform(0.1, 1) * (2 + numpy.sin(numpy.random.normal() + (numpy.random.normal() * x))))
    heights = numpy.column_stack(heights)

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    m = axes.fill(heights, baseline="stacked")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-24-189ef62f6579> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=500, height=300)
          2 axes = canvas.axes()
          3 m = axes.fill(heights, baseline="stacked")


    NameError: name 'toyplot' is not defined


If you pass a sequence of scalar values instead of colors to the "fill"
argument, the values will be mapped to colors using a linear mapping and
a default sequential palette:

.. code:: python

    fill = numpy.arange(heights.shape[1])

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    m = axes.fill(heights, baseline="stacked", fill=fill)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-26-678cb8fafad9> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=500, height=300)
          2 axes = canvas.axes()
          3 m = axes.fill(heights, baseline="stacked", fill=fill)


    NameError: name 'toyplot' is not defined


Of course, you're free to supply your own palette for the mapping:

.. code:: python

    palette = toyplot.color.brewer("BlueRed")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-27-c0460e079b98> in <module>()
    ----> 1 palette = toyplot.color.brewer("BlueRed")
    

    NameError: name 'toyplot' is not defined


.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    m = axes.fill(heights, baseline="stacked", fill=(fill, palette))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-28-8cd1ca076a79> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=500, height=300)
          2 axes = canvas.axes()
          3 m = axes.fill(heights, baseline="stacked", fill=(fill, palette))


    NameError: name 'toyplot' is not defined


... note that the ``baseline`` parameter is what signals that the inputs
are magnitudes instead of boundaries. You can also change the baseline
parameter to create various types of
`streamgraph <http://www.leebyron.com/else/streamgraph>`__:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    m = axes.fill(heights, baseline="symmetric", fill=(fill, palette))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-29-0d6bfbf2e406> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=500, height=300)
          2 axes = canvas.axes()
          3 m = axes.fill(heights, baseline="symmetric", fill=(fill, palette))


    NameError: name 'toyplot' is not defined


.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    m = axes.fill(heights, baseline="wiggle", fill=(fill, palette))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-30-d5b56a3a4610> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=500, height=300)
          2 axes = canvas.axes()
          3 m = axes.fill(heights, baseline="wiggle", fill=(fill, palette))


    NameError: name 'toyplot' is not defined


Barplots
--------

Of course, you can't have a plotting library without
:meth:`barplots <toyplot.axes.Cartesian.bars>` ...

.. code:: python

    heights = numpy.linspace(1, 10, 10) ** 2

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes()
    mark = axes.bars(heights)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-32-fd6f77fdae06> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, height=300)
          2 axes = canvas.axes()
          3 mark = axes.bars(heights)


    NameError: name 'toyplot' is not defined


By default the bars are centered on integer X coordinates in the range
:math:`[0, M)` - but we can specify our own X coordinates to suit:

.. code:: python

    x = numpy.linspace(-2, 2, 20)
    y = 5 - (x ** 2)
    
    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes()
    mark = axes.bars(x, y)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-33-636232e50472> in <module>()
          2 y = 5 - (x ** 2)
          3 
    ----> 4 canvas = toyplot.Canvas(width=300, height=300)
          5 axes = canvas.axes()
          6 mark = axes.bars(x, y)


    NameError: name 'toyplot' is not defined


As a convenience, you can pass the output from
:func:`numpy.histogram()` directly to
:meth:`toyplot.axes.Cartesian.bars`:

.. code:: python

    numpy.random.seed(1234)
    population = numpy.random.normal(size=10000)

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes()
    bars = axes.bars(numpy.histogram(population, 20))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-35-67fda4caf983> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, height=300)
          2 axes = canvas.axes()
          3 bars = axes.bars(numpy.histogram(population, 20))


    NameError: name 'toyplot' is not defined


As with fill marks, Toyplot allows you to stack multiple sets of bars by
passing an :math:`M \times N` matrix as input, where :math:`M` is the
number of observations, and :math:`N` is the number of series:

.. code:: python

    heights1 = numpy.linspace(1, 10, 10) ** 1.1
    heights2 = numpy.linspace(1, 10, 10) ** 1.3
    heights3 = numpy.linspace(1, 10, 10) ** 1.4
    heights4 = numpy.linspace(1, 10, 10) ** 1.5
    heights = numpy.column_stack((heights1, heights2, heights3, heights4))

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes()
    mark = axes.bars(heights)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-37-fd6f77fdae06> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, height=300)
          2 axes = canvas.axes()
          3 mark = axes.bars(heights)


    NameError: name 'toyplot' is not defined


As before, we can style the bars globally and use the "fill", "opacity",
and "title" arguments to specify constant or per-series behavior:

.. code:: python

    fill = ["red", "green", "blue", "yellow"]
    title = ["Series 1", "Series 2", "Series 3", "Series 4"]
    style = {"stroke":toyplot.color.near_black}


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-38-a17e67dee029> in <module>()
          1 fill = ["red", "green", "blue", "yellow"]
          2 title = ["Series 1", "Series 2", "Series 3", "Series 4"]
    ----> 3 style = {"stroke":toyplot.color.near_black}
    

    NameError: name 'toyplot' is not defined


.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes()
    bars = axes.bars(heights, fill=fill, title=title, style=style)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-39-e42ed6ad7826> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, height=300)
          2 axes = canvas.axes()
          3 bars = axes.bars(heights, fill=fill, title=title, style=style)


    NameError: name 'toyplot' is not defined


However, with bars we can take these concepts even further to specify
*per-datum* quantities. That is, the fill, opacity, and title arguments
can accept data that will apply to every individual bar in the plot. For
the following example, we generate a per-datum set of random values to
map to the fill color, and also use them as the bar titles (hover over
the bars to see the titles):

.. code:: python

    fill = numpy.random.random(heights.shape)
    colormap = toyplot.color.diverging("BlueRed")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-40-1a7d292c3aeb> in <module>()
          1 fill = numpy.random.random(heights.shape)
    ----> 2 colormap = toyplot.color.diverging("BlueRed")
    

    NameError: name 'toyplot' is not defined


.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes()
    bars = axes.bars(heights, fill=(fill, colormap), title=fill, style=style)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-41-bd196dd175cd> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, height=300)
          2 axes = canvas.axes()
          3 bars = axes.bars(heights, fill=(fill, colormap), title=fill, style=style)


    NameError: name 'toyplot' is not defined


Scatterplots
------------

Next on our whirlwind tour of marks is the
:meth:`scatterplot <toyplot.axes.Cartesian.scatterplot>`:

.. code:: python

    x = numpy.linspace(0, 2 * numpy.pi)
    y1 = numpy.sin(x)
    y2 = numpy.cos(x)

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    mark = axes.scatterplot(x, y1)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-43-bd7a3564f101> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=500, height=300)
          2 axes = canvas.axes()
          3 mark = axes.scatterplot(x, y1)


    NameError: name 'toyplot' is not defined


As you might expect, you can omit the X coordinates for a scatterplot,
and they will fall in to the range :math:`[0, M)`:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    mark = axes.scatterplot(y1)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-44-ede8093ebc10> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=500, height=300)
          2 axes = canvas.axes()
          3 mark = axes.scatterplot(y1)


    NameError: name 'toyplot' is not defined


And as we've seen before, you can pass multiple series in a single call:

.. code:: python

    series = numpy.column_stack((y1, y2))
    
    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    mark = axes.scatterplot(series)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-45-ee84b4aa9869> in <module>()
          1 series = numpy.column_stack((y1, y2))
          2 
    ----> 3 canvas = toyplot.Canvas(width=500, height=300)
          4 axes = canvas.axes()
          5 mark = axes.scatterplot(series)


    NameError: name 'toyplot' is not defined


And as expected, you can control attributes like fill, size, and opacity
on a global, per-series, or per-datum basis (note that the size is
treated as an approximation of the *area* of an individual datum):

.. code:: python

    fill = numpy.random.random(series.shape)
    palette = toyplot.color.brewer("Oranges")
    size = [16, 81]
    
    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    mark = axes.scatterplot(series, fill=(fill, palette), size=size)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-46-f8ef65338802> in <module>()
          1 fill = numpy.random.random(series.shape)
    ----> 2 palette = toyplot.color.brewer("Oranges")
          3 size = [16, 81]
          4 
          5 canvas = toyplot.Canvas(width=500, height=300)


    NameError: name 'toyplot' is not defined


Markers
-------

You can choose from a variety of marker shapes for scatterplots and line
plots, also specified either globally, per-series, or per-datum, and
specify styles for the markers:

.. code:: python

    mstyle={"stroke":toyplot.color.near_black}
    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    mark = axes.scatterplot(series, size=50, marker=["^", "o"], mstyle=mstyle)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-47-8c2d30690a87> in <module>()
    ----> 1 mstyle={"stroke":toyplot.color.near_black}
          2 canvas = toyplot.Canvas(width=500, height=300)
          3 axes = canvas.axes()
          4 mark = axes.scatterplot(series, size=50, marker=["^", "o"], mstyle=mstyle)


    NameError: name 'toyplot' is not defined


In addition to the basic marker shapes, you can create your own by
adding text labels, also with their own styles:

.. code:: python

    marker = [{"shape":"o", "label":"1"}, {"shape":"o", "label":"2"}]
    mlstyle = {"fill":"white"}

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes()
    mark = axes.scatterplot(series, size=100, marker=marker, mstyle=mstyle, mlstyle=mlstyle)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-49-00c04f42b750> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=500, height=300)
          2 axes = canvas.axes()
          3 mark = axes.scatterplot(series, size=100, marker=marker, mstyle=mstyle, mlstyle=mlstyle)


    NameError: name 'toyplot' is not defined


See the user guide section on :ref:`markers` for additional detail on
the available marker shapes, styles, and how to create your own custom
markers.

Plots Revisited
---------------

Now that we've seen how bar, fill, and scatter plots can accept multiple
series' worth of data in a single call, let's revisit our earlier line
plots, and see that the same is true:

.. code:: python

    x = numpy.linspace(0, 10, 100)
    y1 = numpy.sin(x)
    y2 = numpy.cos(x)
    y3 = numpy.sin(x) + numpy.cos(x)
    series = numpy.column_stack((y1, y2, y3))

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes()
    mark = axes.plot(x, series)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-51-c2652170c0a0> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=600, height=300)
          2 axes = canvas.axes()
          3 mark = axes.plot(x, series)


    NameError: name 'toyplot' is not defined


Axes
----

So far, we've created a default set of axes in each of the preceeding
examples, and called methods on the axes to add marks to the canvas. The
reason we explicitly create axes in Toyplot (instead of simply adding
marks to the canvas directly) is that it allows us to have multiple axes
on a single canvas:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    axes = canvas.axes(grid=(1, 2, 0))
    mark = axes.plot(x, y1)
    axes = canvas.axes(grid=(1, 2, 1))
    mark = axes.plot(x, y2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-52-f8a1d6ef3957> in <module>()
    ----> 1 canvas = toyplot.Canvas(600, 300)
          2 axes = canvas.axes(grid=(1, 2, 0))
          3 mark = axes.plot(x, y1)
          4 axes = canvas.axes(grid=(1, 2, 1))
          5 mark = axes.plot(x, y2)


    NameError: name 'toyplot' is not defined


In addition to positioning axes on the canvas, there are many properties
that control their behavior. For example, Toyplot axes include builtin
support for *labels*:

.. code:: python

    canvas = toyplot.Canvas(300, 300)
    axes = canvas.axes(label="Toyplot User Growth", xlabel="Days", ylabel="Users")
    mark = axes.plot(x, 40 + x ** 2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-53-0fe0ba96d124> in <module>()
    ----> 1 canvas = toyplot.Canvas(300, 300)
          2 axes = canvas.axes(label="Toyplot User Growth", xlabel="Days", ylabel="Users")
          3 mark = axes.plot(x, 40 + x ** 2)


    NameError: name 'toyplot' is not defined


Similarly, we can specify minimum and maximum values for each axis - for
example, if we wanted the previous figure to include :math:`y = 0`:

.. code:: python

    canvas = toyplot.Canvas(300, 300)
    axes = canvas.axes(label="Toyplot User Growth", xlabel="Days", ylabel="Users", ymin=0)
    mark = axes.plot(x, 40 + x ** 2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-54-ce0767cc8e90> in <module>()
    ----> 1 canvas = toyplot.Canvas(300, 300)
          2 axes = canvas.axes(label="Toyplot User Growth", xlabel="Days", ylabel="Users", ymin=0)
          3 mark = axes.plot(x, 40 + x ** 2)


    NameError: name 'toyplot' is not defined


We can also specify logarithmic scales for axes:

.. code:: python

    x = numpy.linspace(-1000, 1000)

.. code:: python

    toyplot.plot(x, x, marker="o", xscale="linear", yscale="log", width=500);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-56-653fe6b041be> in <module>()
    ----> 1 toyplot.plot(x, x, marker="o", xscale="linear", yscale="log", width=500);
    

    NameError: name 'toyplot' is not defined


There are many more properties that control axes positioning and
behavior - for more details, see :ref:`canvas-layout` and
:ref:`cartesian-axes` in the user guide.

Animation
---------

Toyplot can also create animated figures, by recording changes to a
figure over time. Assume you've setup the following scatterplot:

.. code:: python

    x = numpy.random.normal(size=100)
    y = numpy.random.normal(size=len(x))

.. code:: python

    canvas = toyplot.Canvas(300, 300)
    axes = canvas.axes()
    mark = axes.scatterplot(x, y, size=100)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-58-31e98d4042c9> in <module>()
    ----> 1 canvas = toyplot.Canvas(300, 300)
          2 axes = canvas.axes()
          3 mark = axes.scatterplot(x, y, size=100)


    NameError: name 'toyplot' is not defined


Suppose we want to show the order in which the samples were drawn from
some distribution. We could use the ``fill`` parameter to map each
sample's index to a color, but an animation can be more intuitive. We
can use :meth:`toyplot.canvas.Canvas.animate` to add a sequence of
animation frames to the canvas. We pass the number of frames and a
callback function as arguments, and the callback function will be called
once per frame with a single
:class:`frame <toyplot.canvas.AnimationFrame>` argument. The callback
uses the frame object to retrieve information about the frame and record
any changes that should be made to the canvas at that frame. In the
example below, we set the opacity of each scatterplot datum to 5% in the
first frame, then change them back to 100% over the course of the
animation:

.. code:: python

    canvas = toyplot.Canvas(300, 300)
    axes = canvas.axes()
    mark = axes.scatterplot(x, y, size=100)
    
    def callback(frame):
        if frame.index() == 0:
            for i in range(len(x)):
                frame.set_datum_style(mark, 0, i, style={"opacity":0.1})
        else:
            frame.set_datum_style(mark, 0, frame.index() - 1, style={"opacity":1.0})
    canvas.animate(len(x) + 1, callback)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-59-be28149c89ba> in <module>()
    ----> 1 canvas = toyplot.Canvas(300, 300)
          2 axes = canvas.axes()
          3 mark = axes.scatterplot(x, y, size=100)
          4 
          5 def callback(frame):


    NameError: name 'toyplot' is not defined


Let's try animating something other than a datum style - in the
following example, we add a text mark to the canvas, and use it to
display information about the frame:

.. code:: python

    canvas = toyplot.Canvas(300, 300)
    axes = canvas.axes()
    mark = axes.scatterplot(x, y, size=100)
    text = canvas.text(150, 20, "")
    
    def callback(frame):
        frame.set_datum_text(text, 0, 0, str(frame))
        if frame.index() == 0:
            for i in range(len(x)):
                frame.set_datum_style(mark, 0, i, style={"opacity":0.05})
        else:
            frame.set_datum_style(mark, 0, frame.index() - 1, style={"opacity":1.0})
    canvas.animate(len(x) + 1, callback)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-60-8542e7606918> in <module>()
    ----> 1 canvas = toyplot.Canvas(300, 300)
          2 axes = canvas.axes()
          3 mark = axes.scatterplot(x, y, size=100)
          4 text = canvas.text(150, 20, "")
          5 


    NameError: name 'toyplot' is not defined


Note from this example that each frame has a zero-based frame index,
along with begin and end times, which are measured in seconds. If you
look closely, you'll see that the difference in begin and end times is
0.03 seconds for each frame, which corresponds to a default 30 frames
per second. If we want to control the framerate, we can pass a (frames,
framerate) tuple when we call :meth:`toyplot.canvas.Canvas.animate`
(note that the playback is slower, and the times for the frames are
changed):

.. code:: python

    canvas = toyplot.Canvas(300, 300)
    axes = canvas.axes()
    mark = axes.scatterplot(x, y, size=100)
    text = canvas.text(150, 20, "")
    
    def callback(frame):
        frame.set_datum_text(text, 0, 0, str(frame))
        if frame.index() == 0:
            for i in range(len(x)):
                frame.set_datum_style(mark, 0, i, style={"opacity":0.05})
        else:
            frame.set_datum_style(mark, 0, frame.index() - 1, style={"opacity":1.0})
    canvas.animate((len(x) + 1, 10), callback)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-61-b64cbf430540> in <module>()
    ----> 1 canvas = toyplot.Canvas(300, 300)
          2 axes = canvas.axes()
          3 mark = axes.scatterplot(x, y, size=100)
          4 text = canvas.text(150, 20, "")
          5 


    NameError: name 'toyplot' is not defined


Sometimes the callback approach to animation is awkward, particularly if
you simply have a one-time "event" that needs to happen in the middle of
the animation. In this case, you can use
:meth:`toyplot.canvas.Canvas.time` to record changes for individual
frames:

.. code:: python

    canvas = toyplot.Canvas(300, 300)
    axes = canvas.axes()
    mark = axes.scatterplot(x, y, size=100)
    text = canvas.text(150, 20, "", style={"text-anchor":"middle"})
    text2 = canvas.text(150, 50, "Halfway There!", style={"font-size":"16px", "font-weight":"bold", "fill":"blue", "text-anchor":"middle"})
    
    def callback(frame):
        frame.set_datum_text(text, 0, 0, str(frame))
        if frame.index() == 0:
            for i in range(len(x)):
                frame.set_datum_style(mark, 0, i, style={"opacity":0.05})
        else:
            frame.set_datum_style(mark, 0, frame.index() - 1, style={"opacity":1.0})
    canvas.animate((len(x) + 1), callback)
    canvas.time(0, 0.1).set_datum_style(text2, 0, 0, {"opacity":0.0})
    canvas.time(1.5, 5.1).set_datum_style(text2, 0, 0, {"opacity":1.0})


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-62-f7e579eef94e> in <module>()
    ----> 1 canvas = toyplot.Canvas(300, 300)
          2 axes = canvas.axes()
          3 mark = axes.scatterplot(x, y, size=100)
          4 text = canvas.text(150, 20, "", style={"text-anchor":"middle"})
          5 text2 = canvas.text(150, 50, "Halfway There!", style={"font-size":"16px", "font-weight":"bold", "fill":"blue", "text-anchor":"middle"})


    NameError: name 'toyplot' is not defined


Note that when you combine :meth:`toyplot.canvas.Canvas.animate` and
:meth:`toyplot.canvas.Canvas.time`, you don't have to force the
"frames" to line-up ... you can record events in any order and at any
point in time, whether there are existing frames at those times or not.
In fact, you could call :meth:`toyplot.canvas.Canvas.animate` multiple
times, if you wanted to animate events happening at different rates:

.. code:: python

    canvas = toyplot.Canvas(100, 100, style={"background-color":"ivory"})
    t1 = canvas.text(50, 33, "1 hz", style={"text-anchor":"middle"})
    t2 = canvas.text(50, 66, "2 hz", style={"text-anchor":"middle"})
    def blink(mark):
        def callback(frame):
            frame.set_datum_style(mark, 0, 0, {"opacity":frame.index() % 2.0})
        return callback
    canvas.animate((10, 2), blink(t1))
    canvas.animate((20, 4), blink(t2))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-63-eb95aeaa7d50> in <module>()
    ----> 1 canvas = toyplot.Canvas(100, 100, style={"background-color":"ivory"})
          2 t1 = canvas.text(50, 33, "1 hz", style={"text-anchor":"middle"})
          3 t2 = canvas.text(50, 66, "2 hz", style={"text-anchor":"middle"})
          4 def blink(mark):
          5     def callback(frame):


    NameError: name 'toyplot' is not defined


Using transition properties in your styles can smooth-out the animation
by avoiding instantaneous changes:

.. code:: python

    canvas = toyplot.Canvas(100, 100, style={"background-color":"ivory"})
    t1 = canvas.text(50, 33, "1 hz", style={"text-anchor":"middle", "transition":"opacity 0.5s"})
    t2 = canvas.text(50, 66, "2 hz", style={"text-anchor":"middle", "transition":"opacity 0.25s"})
    def blink(mark):
        def callback(frame):
            frame.set_datum_style(mark, 0, 0, {"opacity":frame.index() % 2.0})
        return callback
    canvas.animate((10, 2), blink(t1))
    canvas.animate((20, 4), blink(t2))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-64-538fe3614308> in <module>()
    ----> 1 canvas = toyplot.Canvas(100, 100, style={"background-color":"ivory"})
          2 t1 = canvas.text(50, 33, "1 hz", style={"text-anchor":"middle", "transition":"opacity 0.5s"})
          3 t2 = canvas.text(50, 66, "2 hz", style={"text-anchor":"middle", "transition":"opacity 0.25s"})
          4 def blink(mark):
          5     def callback(frame):


    NameError: name 'toyplot' is not defined


