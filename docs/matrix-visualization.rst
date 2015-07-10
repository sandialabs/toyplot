
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
    

    /Users/tshead/src/toyplot/toyplot/__init__.pyc in matrix(matrix, title, step, colormap, palette, width, height, canvas_style)
         98   """
         99   canvas = Canvas(width=width, height=height, style=canvas_style)
    --> 100   table = canvas.matrix(matrix=matrix, title=title, step=step, colormap=colormap, palette=palette)
        101   return canvas, table
        102 


    TypeError: matrix() got an unexpected keyword argument 'title'



.. raw:: html

    <div align="center" class="toyplot" id="t76bb0f90258f4208911602616b271b80"><svg height="600px" id="tea49e31b5d3344c486a956b4c405cbfa" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>


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
    

    /Users/tshead/src/toyplot/toyplot/__init__.pyc in matrix(matrix, title, step, colormap, palette, width, height, canvas_style)
         98   """
         99   canvas = Canvas(width=width, height=height, style=canvas_style)
    --> 100   table = canvas.matrix(matrix=matrix, title=title, step=step, colormap=colormap, palette=palette)
        101   return canvas, table
        102 


    TypeError: matrix() got an unexpected keyword argument 'title'



.. raw:: html

    <div align="center" class="toyplot" id="t47e35e010abb4c448d406a24e5a6247c"><svg height="600px" id="t8c75d38b4d8a477bbbe3877e9487cd31" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>


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


    /Users/tshead/src/toyplot/toyplot/__init__.pyc in matrix(matrix, title, step, colormap, palette, width, height, canvas_style)
         98   """
         99   canvas = Canvas(width=width, height=height, style=canvas_style)
    --> 100   table = canvas.matrix(matrix=matrix, title=title, step=step, colormap=colormap, palette=palette)
        101   return canvas, table
        102 


    TypeError: matrix() got an unexpected keyword argument 'title'



.. raw:: html

    <div align="center" class="toyplot" id="ta49fdbccc8c8472e936251c8f896483e"><svg height="600px" id="tfd37658bf3114a6b97ff90ae38e9e71f" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>


