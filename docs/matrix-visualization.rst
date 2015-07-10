
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _matrix-visualization:

Matrix Visualization
====================

It is often useful to render a two-dimensional matrix as a regular grid,
colored by the matrix values, as a way to look for patterns in the data.
To facilitate this, Toyplot provides
:meth:`toyplot.canvas.Canvas.matrix` and :func:`toyplot.matrix`
functions. To demonstrate, let's begin with a visualization of a matrix
containing values from a normal distribution centered at 1.0:

.. code:: python

    import numpy
    numpy.random.seed(1234)
    matrix = numpy.random.normal(loc=1.0, size=(20, 20))

.. code:: python

    import toyplot
    toyplot.matrix(matrix, title="A matrix");


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-c2218b3dd736> in <module>()
          1 import toyplot
    ----> 2 toyplot.matrix(matrix, title="A matrix");
    

    TypeError: matrix() got an unexpected keyword argument 'title'


By default, the matrix is rendered using the Color Brewer diverging
"BlueRed" :ref:`palette<color>`, mapped to the minimum and maximum
values in the matrix. Thus, dark blue represents the minimum value and
dark red is the maximum value. If you hover the mouse over the cells in
the matrix you can see their values as a popup and compare them to the
minimum and maximum values in the data:

.. code:: python

    print matrix.min(), matrix.max()


.. parsed-literal::

    -2.56351666062 3.76384407985


However, let's say that we want our colormap to be symmetric around zero
so all blue colors are negative and all red colors are positive. To do
so, we simply create a custom :class:`toyplot.color.LinearMap`,
specifying explicit minimum and maximum domain values and using it in
the call to create the matrix visualization:

.. code:: python

    colormap = toyplot.color.LinearMap(toyplot.color.brewer("BlueRed"), domain_min=-4, domain_max=4)
    toyplot.matrix(matrix, title="A matrix", colormap=colormap);


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-f41f02325afd> in <module>()
          1 colormap = toyplot.color.LinearMap(toyplot.color.brewer("BlueRed"), domain_min=-4, domain_max=4)
    ----> 2 toyplot.matrix(matrix, title="A matrix", colormap=colormap);
    

    TypeError: matrix() got an unexpected keyword argument 'title'


Note that the matrix visualization in Toyplot is actually a special-case
initialization of a :ref:`table<table-axes>`, so you can use the full
:class:`toyplot.axes.Table` API to configured it however you like. For
example, you could highlight the maximum value in the matrix using a
contrasting color:

.. code:: python

    i, j = numpy.unravel_index(numpy.argmax(matrix), matrix.shape)
    
    canvas, table = toyplot.matrix(matrix, title="A matrix", colormap=colormap)
    table.body.cell(i, j).bstyle = {"fill":"yellow"}


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-1be4ed147bcd> in <module>()
          1 i, j = numpy.unravel_index(numpy.argmax(matrix), matrix.shape)
          2 
    ----> 3 canvas, table = toyplot.matrix(matrix, title="A matrix", colormap=colormap)
          4 table.body.cell(i, j).bstyle = {"fill":"yellow"}


    TypeError: matrix() got an unexpected keyword argument 'title'


