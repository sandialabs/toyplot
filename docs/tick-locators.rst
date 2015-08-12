
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _tick-locators:

Tick Locators
=============

When you create a figure in Toyplot, you begin by creating a
:class:`canvas<toyplot.canvas.Canvas>`, add
:mod:`axes<toyplot.axes>`, and add data to the axes in the form of
marks. The axes map data from its *domain* to a *range* on the canvas,
generating *ticks* in domain-space with *tick labels* as an integral
part of the process.

To generate tick locations and tick labels, the axes delegate to the
*tick locator* classes in the :mod:`toyplot.locator` module. Each tick
locator class is responsible for generating a collection of tick
locations from the range of values in an axis domain, and there are
several different classes available that implement different strategies
for generating "good" tick locations. If you don't specify any tick
locators when creating axes, sensible defaults will be chosen for you.
For example:

.. code:: python

    import numpy
    x = numpy.arange(20)
    y = numpy.linspace(0, 1, len(x)) ** 2

.. code:: python

    import toyplot
    canvas, axes, mark = toyplot.plot(x, y, width=300)


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-2-f05dc1f2cd12> in <module>()
    ----> 1 import toyplot
          2 canvas, axes, mark = toyplot.plot(x, y, width=300)


    ImportError: No module named toyplot


Note that the Y axis in this plot has sensible ticks that cover the full
data domain :math:`[0, 1]`, while the X axis also has sensible ticks
that include "round" numbers like 20 even though the X values only cover
:math:`[0, 19]`. The algorithm for identifying "good" "round" tick
values is provided by Toyplot's :class:`toyplot.locator.Extended`
locator.

However, let's say that we prefer to always have ticks that include the
exact minimum and maximum data domain values, and evenly divide the rest
of the domain. In this case, we can override the default choice of
locator with the :class:`toyplot.locator.Basic` tick locator:

.. code:: python

    canvas, axes, mark = toyplot.plot(x, y, width=300)
    axes.x.ticks.locator = toyplot.locator.Basic(count=5)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-2d0d745823a7> in <module>()
    ----> 1 canvas, axes, mark = toyplot.plot(x, y, width=300)
          2 axes.x.ticks.locator = toyplot.locator.Basic(count=5)


    NameError: name 'toyplot' is not defined


We can also override the default formatting string used to generate the
locator labels:

.. code:: python

    canvas, axes, mark = toyplot.plot(x, y, width=300)
    axes.x.ticks.locator = toyplot.locator.Basic(count=5, format="{:.2f}")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-7d8e5f5290f4> in <module>()
    ----> 1 canvas, axes, mark = toyplot.plot(x, y, width=300)
          2 axes.x.ticks.locator = toyplot.locator.Basic(count=5, format="{:.2f}")


    NameError: name 'toyplot' is not defined


Anytime you use log scale axes in a plot, Toyplot automatically uses the
:class:`toyplot.locator.Log` locator to provide ticks that are
evenly-spaced :

.. code:: python

    canvas, axes, mark = toyplot.plot(x, y, xscale="log10", width=300)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-a2cac1ec39d1> in <module>()
    ----> 1 canvas, axes, mark = toyplot.plot(x, y, xscale="log10", width=300)
    

    NameError: name 'toyplot' is not defined


If you don't like the "superscript" notation that the Log locator
produces, you could replace it with your own locator and custom format:

.. code:: python

    canvas, axes, mark = toyplot.plot(x, y, xscale="log10", width=300)
    axes.x.ticks.locator = toyplot.locator.Log(base=10, format="{base}^{exponent}")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-005f4d91b71e> in <module>()
    ----> 1 canvas, axes, mark = toyplot.plot(x, y, xscale="log10", width=300)
          2 axes.x.ticks.locator = toyplot.locator.Log(base=10, format="{base}^{exponent}")


    NameError: name 'toyplot' is not defined


Or even display raw tick values:

.. code:: python

    canvas, axes, mark = toyplot.plot(x, y, xscale="log2", width=300)
    axes.x.ticks.locator = toyplot.locator.Log(base=2, format="{:.0f}")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-1a1b97f8494a> in <module>()
    ----> 1 canvas, axes, mark = toyplot.plot(x, y, xscale="log2", width=300)
          2 axes.x.ticks.locator = toyplot.locator.Log(base=2, format="{:.0f}")


    NameError: name 'toyplot' is not defined


Although you might not think of :ref:`table-axes` as needing tick
locators, when you use :func:`toyplot.matrix` or
:meth:`toyplot.canvas.Canvas.matrix` to visualize a matrix of values,
it generates a table visualization and uses
:class:`toyplot.locator.Integer` locators to generate row and column
labels:

.. code:: python

    numpy.random.seed(1234)
    canvas, table = toyplot.matrix(numpy.random.random((5, 5)), width=300)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-cc02fb2b7c9c> in <module>()
          1 numpy.random.seed(1234)
    ----> 2 canvas, table = toyplot.matrix(numpy.random.random((5, 5)), width=300)
    

    NameError: name 'toyplot' is not defined


By default the Integer locator generates a tick/label for every integer
in the range :math:`[0, N)` ... as you visualize larger matrices, you'll
find that a label for every row and column becomes crowded, in which
case you can override the default ``step`` parameter to space-out the
labels:

.. code:: python

    canvas, table = toyplot.matrix(numpy.random.random((50, 50)), width=400, step=5)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-c47d1d2117fb> in <module>()
    ----> 1 canvas, table = toyplot.matrix(numpy.random.random((50, 50)), width=400, step=5)
    

    NameError: name 'toyplot' is not defined


For the ultimate flexibility in positioning tick locations and labels,
you can use the :class:`toyplot.locator.Explicit` locator. With it,
you can specify an explicit set of labels, and a set of :math:`[0, N)`
integer locations will be created to match. This is particularly useful
if you are working with categorical data:

.. code:: python

    fruits = ["Apples", "Oranges", "Kiwi", "Miracle Fruit", "Durian"]
    counts = [452, 347, 67, 21, 5]
    
    canvas, axes, mark = toyplot.bars(counts, width=400, height=300)
    axes.x.ticks.locator = toyplot.locator.Explicit(labels=fruits)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-774492910dc2> in <module>()
          2 counts = [452, 347, 67, 21, 5]
          3 
    ----> 4 canvas, axes, mark = toyplot.bars(counts, width=400, height=300)
          5 axes.x.ticks.locator = toyplot.locator.Explicit(labels=fruits)


    NameError: name 'toyplot' is not defined


Note that in the above example the implicit :math:`[0, N)` tick
locations match the implicit :math:`[0, N)` X coordinates that are
generated for each bar when you don't supply any X coordinates of your
own. This is by design!

You can also use Explicit locators with a list of tick locations, and a
set of tick labels will be generated using a format string. For example:

.. code:: python

    x = numpy.linspace(0, 2 * numpy.pi)
    y = numpy.sin(x)
    locations=[0, numpy.pi/2, numpy.pi, 3*numpy.pi/2, 2*numpy.pi]
    
    canvas, axes, mark = toyplot.plot(x, y, width=500, height=300)
    axes.x.ticks.locator = toyplot.locator.Explicit(locations=locations, format="{:.2f}")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-356a8355bbbf> in <module>()
          3 locations=[0, numpy.pi/2, numpy.pi, 3*numpy.pi/2, 2*numpy.pi]
          4 
    ----> 5 canvas, axes, mark = toyplot.plot(x, y, width=500, height=300)
          6 axes.x.ticks.locator = toyplot.locator.Explicit(locations=locations, format="{:.2f}")


    NameError: name 'toyplot' is not defined


Finally, you can supply both locations and labels to an Explicit
locator:

.. code:: python

    labels = ["0", u"\u03c0 / 2", u"\u03c0", u"3\u03c0 / 2", u"2\u03c0"]
    
    canvas, axes, mark = toyplot.plot(x, y, width=500, height=300)
    axes.x.ticks.locator = toyplot.locator.Explicit(locations=locations, labels=labels)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-1d50c25707eb> in <module>()
          1 labels = ["0", u"\u03c0 / 2", u"\u03c0", u"3\u03c0 / 2", u"2\u03c0"]
          2 
    ----> 3 canvas, axes, mark = toyplot.plot(x, y, width=500, height=300)
          4 axes.x.ticks.locator = toyplot.locator.Explicit(locations=locations, labels=labels)


    NameError: name 'toyplot' is not defined


Explicit locators are also a good way to handle timeseries using
timestamps or Python datetime objects. For this example, we will create
a series "x" that contains datetime objects, and a series "y" containing
values:

.. code:: python

    import datetime
    import toyplot.data
    
    data = toyplot.data.read_csv("commute-obd.csv")
    observations = numpy.logical_and(data["name"] == "Vehicle Speed", data["value"] != "NODATA")
    timestamps = data["timestamp"][observations]
    
    x = [datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f") for timestamp in timestamps]
    y = data["value"][observations]


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-13-71d177fc7ca7> in <module>()
          1 import datetime
    ----> 2 import toyplot.data
          3 
          4 data = toyplot.data.read_csv("commute-obd.csv")
          5 observations = numpy.logical_and(data["name"] == "Vehicle Speed", data["value"] != "NODATA")


    ImportError: No module named toyplot.data


Now, we can extract a set of locations and labels, formatting the
datetime objects to suit:

.. code:: python

    locations = []
    labels = []
    for index, timestamp in enumerate(x):
        if timestamp.minute % 5 == 0 and 0 < timestamp.second < 5:
            locations.append(index)
            labels.append(timestamp.strftime("%H:%M"))
    
    canvas, axes, mark = toyplot.plot(y, label="Vehicle Speed", xlabel="Time", ylabel="km/h", width=600, height=300)
    axes.x.ticks.locator = toyplot.locator.Explicit(locations=locations, labels=labels)
    axes.x.ticks.show = True


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-14-f88cfb062f96> in <module>()
          2 labels = []
          3 for index, timestamp in enumerate(x):
    ----> 4     if timestamp.minute % 5 == 0 and 0 < timestamp.second < 5:
          5         locations.append(index)
          6         labels.append(timestamp.strftime("%H:%M"))


    AttributeError: 'numpy.float64' object has no attribute 'minute'


Because timestamp labels tend to be fairly long, this is often a case
where you'll want to adjust the orientation of the labels so they don't
overlap (note in the following example that we had to make the canvas
larger and position the axes manually on the canvas to make room for the
vertical labels - and we manually placed the x axis label to avoid
overlap):

.. code:: python

    locations = []
    labels = []
    for index, timestamp in enumerate(x):
        if timestamp.minute % 5 == 0 and 0 < timestamp.second < 5:
            locations.append(index)
            labels.append(timestamp.strftime("%Y-%m-%d %H:%M"))
    
    canvas = toyplot.Canvas(width=600, height=400)
    canvas.text(300, 360, "Time", style={"font-weight":"bold"})
    axes = canvas.axes(label="Vehicle Speed", ylabel="km/h", bounds=(50, -50, 50, -150))
    axes.x.ticks.locator = toyplot.locator.Explicit(locations=locations, labels=labels)
    axes.x.ticks.show = True
    axes.x.ticks.labels.angle = 90
    axes.x.ticks.labels.style = {"baseline-shift":0, "text-anchor":"end", "-toyplot-anchor-shift":"-6px"}
    mark = axes.plot(y)



::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-15-9ac85444d8ba> in <module>()
          2 labels = []
          3 for index, timestamp in enumerate(x):
    ----> 4     if timestamp.minute % 5 == 0 and 0 < timestamp.second < 5:
          5         locations.append(index)
          6         labels.append(timestamp.strftime("%Y-%m-%d %H:%M"))


    AttributeError: 'numpy.float64' object has no attribute 'minute'

