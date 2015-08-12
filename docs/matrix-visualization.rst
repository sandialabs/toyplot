
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
    toyplot.matrix(matrix, label="A matrix");


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-2-717fa7e3e33c> in <module>()
    ----> 1 import toyplot
          2 toyplot.matrix(matrix, label="A matrix");


    ImportError: No module named toyplot


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
    toyplot.matrix(matrix, label="A matrix", colormap=colormap);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-140bda1f5ce6> in <module>()
    ----> 1 colormap = toyplot.color.LinearMap(toyplot.color.brewer("BlueRed"), domain_min=-4, domain_max=4)
          2 toyplot.matrix(matrix, label="A matrix", colormap=colormap);


    NameError: name 'toyplot' is not defined


As your matrix sizes grow, you may need to thin-out the row and column
indices to avoid overlap:

.. code:: python

    big_matrix = numpy.random.normal(loc=1, size=(50, 50))
    toyplot.matrix(big_matrix, step=5, label="A matrix", colormap=colormap);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-676ba0b5e06c> in <module>()
          1 big_matrix = numpy.random.normal(loc=1, size=(50, 50))
    ----> 2 toyplot.matrix(big_matrix, step=5, label="A matrix", colormap=colormap);
    

    NameError: name 'toyplot' is not defined


Or, you may wish to leave off the indices altogether:

.. code:: python

    toyplot.matrix(big_matrix, xshow=False, yshow=False, label="A matrix", colormap=colormap);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-e6397b87018a> in <module>()
    ----> 1 toyplot.matrix(big_matrix, xshow=False, yshow=False, label="A matrix", colormap=colormap);
    

    NameError: name 'toyplot' is not defined


Note that the matrix visualization in Toyplot is actually just a factory
function that creates and populates a set of :ref:`table-axes`, so you
can use the full :class:`toyplot.axes.Table` API to configure it
however you like. For example, you could highlight the maximum value in
the matrix using a contrasting color:

.. code:: python

    i, j = numpy.unravel_index(numpy.argmax(matrix), matrix.shape)
    
    canvas, table = toyplot.matrix(matrix, label="A matrix", colormap=colormap)
    table.body.cell(i, j).bstyle = {"fill":"yellow"}


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-1f37da8484f7> in <module>()
          1 i, j = numpy.unravel_index(numpy.argmax(matrix), matrix.shape)
          2 
    ----> 3 canvas, table = toyplot.matrix(matrix, label="A matrix", colormap=colormap)
          4 table.body.cell(i, j).bstyle = {"fill":"yellow"}


    NameError: name 'toyplot' is not defined


Or you could use the table API to overwrite or replace the default
labels:

.. code:: python

    x = numpy.arange(-5, 5, 0.2)
    y = numpy.arange(-5, 5, 0.2)
    xx, yy = numpy.meshgrid(x, y, sparse=True)
    z = xx ** 2 - yy ** 2
    
    canvas, table = toyplot.matrix(z, step=5, width=400)
    table.left.cell(25, 0).style = {"fill":"red"}
    table.top.cell(0, 25).style = {"fill":"red"}
    table.right.cell(25, 0).data = "Saddle"
    table.bottom.cell(0, 25).data = "Saddle"


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-4540187a7586> in <module>()
          4 z = xx ** 2 - yy ** 2
          5 
    ----> 6 canvas, table = toyplot.matrix(z, step=5, width=400)
          7 table.left.cell(25, 0).style = {"fill":"red"}
          8 table.top.cell(0, 25).style = {"fill":"red"}


    NameError: name 'toyplot' is not defined


If you want to combine a matrix with additional plots on a canvas, you
use the same :ref:`canvas-layout` mechanisms as usual:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=400)
    table = canvas.matrix(matrix, label="Matrix", bounds=(50, -250, 50, -50), step=5)
    axes = canvas.axes(bounds=(-200, -50, 50, -50), label="Distribution", xlabel="Count", ylabel="Value")
    axes.bars(numpy.histogram(matrix, 20), along="y")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-8c147550b6e1> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=600, height=400)
          2 table = canvas.matrix(matrix, label="Matrix", bounds=(50, -250, 50, -50), step=5)
          3 axes = canvas.axes(bounds=(-200, -50, 50, -50), label="Distribution", xlabel="Count", ylabel="Value")
          4 axes.bars(numpy.histogram(matrix, 20), along="y")


    NameError: name 'toyplot' is not defined

