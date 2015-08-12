
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _convenience-api:

Convenience API
===============

With Toyplot, a figure always consists of three parts:

-  A :py:class:`canvas <toyplot.canvas.Canvas>`
-  One or more sets of :py:mod:`axes <toyplot.axes>` added to the
   canvas.
-  One or more :py:mod:`marks <toyplot.mark>` added to the axes.

Creating these entities separately gives you the maximum flexibility,
allowing you to add multiple axes (even overlapping axes) to one canvas,
splitting the marks among the different axes, etc. However for simple
figures containing a single set of axes and a single mark, this way of
working can be tedious. Toyplot's convenience API combines the three
calls to create canvas, axes, and mark into a single function that can
handle many of your plotting needs with a minimum of code.

Consider the following verbose example:

.. code:: python

    import numpy
    y = numpy.linspace(0, 1, 20) ** 2

.. code:: python

    import toyplot
    canvas = toyplot.Canvas(width=300)
    axes = canvas.axes()
    axes.plot(y);


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-2-55c72fab190b> in <module>()
    ----> 1 import toyplot
          2 canvas = toyplot.Canvas(width=300)
          3 axes = canvas.axes()
          4 axes.plot(y);


    ImportError: No module named toyplot


Using the convenience API, it can be reduced to a single call to
:py:func:`toyplot.plot`:

.. code:: python

    canvas, axes, mark = toyplot.plot(y, width=300)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-6cf4d18f83b8> in <module>()
    ----> 1 canvas, axes, mark = toyplot.plot(y, width=300)
    

    NameError: name 'toyplot' is not defined


Of course, if you're using the convenience API there's a good chance you
don't need the function's return value (a (canvas, axes, mark) tuple) at
all, making it even more compact:

.. code:: python

    toyplot.plot(y, width=300);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-b2cee9a10477> in <module>()
    ----> 1 toyplot.plot(y, width=300);
    

    NameError: name 'toyplot' is not defined


If you check the reference documentation for :py:func:`toyplot.plot`,
you will see that its parameters include the union of the parameters for
:py:class:`toyplot.canvas.Canvas`,
:py:meth:`toyplot.canvas.Canvas.axes`, and
:py:meth:`toyplot.axes.Cartesian.plot`, except where parameter names
might conflict.

Similar convenience API functions are provided for
:py:func:`bar <toyplot.bars>`, :py:func:`fill <toyplot.fill>`, and
:py:func:`scatter <toyplot.scatterplot>` plots:

.. code:: python

    toyplot.bars(y, width=300);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-0d3747b2d340> in <module>()
    ----> 1 toyplot.bars(y, width=300);
    

    NameError: name 'toyplot' is not defined


.. code:: python

    toyplot.fill(numpy.column_stack((y, y*2)), width=300);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-e17e575320c2> in <module>()
    ----> 1 toyplot.fill(numpy.column_stack((y, y*2)), width=300);
    

    NameError: name 'toyplot' is not defined


.. code:: python

    numpy.random.seed(1234)
    toyplot.scatterplot(numpy.random.normal(size=50), width=300);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-c0470dfc787b> in <module>()
          1 numpy.random.seed(1234)
    ----> 2 toyplot.scatterplot(numpy.random.normal(size=50), width=300);
    

    NameError: name 'toyplot' is not defined


.. code:: python

    toyplot.matrix(numpy.random.normal(size=(10, 10)), width=300);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-9d84bb7573ad> in <module>()
    ----> 1 toyplot.matrix(numpy.random.normal(size=(10, 10)), width=300);
    

    NameError: name 'toyplot' is not defined


.. code:: python

    columns = ["Year", "MPG", "Model"]
    canvas, table = toyplot.table(toyplot.data.read_csv("cars.csv").columns(columns)[:10], width=300)
    table.column(2).width = 130


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-b2af3942da92> in <module>()
          1 columns = ["Year", "MPG", "Model"]
    ----> 2 canvas, table = toyplot.table(toyplot.data.read_csv("cars.csv").columns(columns)[:10], width=300)
          3 table.column(2).width = 130


    NameError: name 'toyplot' is not defined


If you need greater control over the positioning of the axes within the
canvas, need to add multiple axes to one canvas, or need to add multiple
marks to one set of axes, you'll have to create the canvas and axes
explicitly.
