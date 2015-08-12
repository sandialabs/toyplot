
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _interaction:

Interaction
-----------

A key goal for the Toyplot team is to explore interactive features for
plots, making them truly useful and embeddable, so that they become a
ubiquitous part of every data graphic user's experience. The following
examples of interaction are just scratching the surface of what we have
planned for Toyplot:

Titles
~~~~~~

Most of the visualization types in Toyplot accept a ``title`` parameter,
allowing you to specify per-series or per-datum titles for a figure.
With Toyplot's preferred embeddable HTML output, those titles are
displayed via a popup when hovering over the data. For example, the
following figure has a global title "Employee Schedule", which you
should see as a popup when you hover the mouse over any of the bars:

.. code:: python

    import numpy
    numpy.random.seed(1234)
    start = numpy.random.normal(loc=8, scale=1, size=20)
    end = numpy.random.normal(loc=16, scale=1, size=20)
    boundaries = numpy.column_stack((start, end))
    title = "Employee Schedule"

.. code:: python

    import toyplot
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-2-6ab374508c69> in <module>()
    ----> 1 import toyplot
          2 toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);


    ImportError: No module named toyplot


If your plot includes multiple series, you can assign a per-series title
instead. Hover the mouse over both series in the following plot to see
"Morning Schedule" and "Afternoon Schedule":

.. code:: python

    lunch = numpy.random.normal(loc=12, scale=0.5, size=20)
    boundaries = numpy.column_stack((start, lunch, end))
    title = ["Morning Schedule", "Afternoon Schedule"]
    
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-d4b72413aae7> in <module>()
          3 title = ["Morning Schedule", "Afternoon Schedule"]
          4 
    ----> 5 toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);
    

    NameError: name 'toyplot' is not defined


Finally, you can assign a title for every datum:

.. code:: python

    title = numpy.column_stack((
            ["Employee %s Morning" % i for i in range(20)],
            ["Employee %s Afternoon" % i for i in range(20)]
            ))
    
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-fdeedf8d73d6> in <module>()
          4         ))
          5 
    ----> 6 toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);
    

    NameError: name 'toyplot' is not defined


Of course, the title attribute works with all types of visualizations.

Coordinates
~~~~~~~~~~~

As you mouse over the above figures, you should also see the interactive
mouse coordinates in the upper-right-hand corner of the axes. These
coordinates show the domain values where the crosshair mouse cursor is
located.

If you wish to disable the mouse coordinates altogether, you can do so
using the axes:

.. code:: python

    canvas, axes, mark = toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300)
    axes.coordinates.show = False


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-4c989fe0ce9e> in <module>()
    ----> 1 canvas, axes, mark = toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300)
          2 axes.coordinates.show = False


    NameError: name 'toyplot' is not defined


Now when you mouse over the axes, the coordinates are no longer there.

Data Export
~~~~~~~~~~~

If you right-click the mouse over any of the above plots, a small popup
menu will appear, giving you the option to "Save as .csv". If you choose
that option, the raw data from the plot will be extracted in CSV format
and you can save it.

Note that different browsers, browser versions, and platforms will
behave differently when extracting the file:

-  Safari on OSX will open the file in a separate tab, which you can
   save to disk using ``File > Save As``.
-  Chrome on OSX will immediately open a file dialog, prompting you to
   save the file.
-  Firefox on OSX will prompt you to open the file with Microsoft Excel
   (if installed), or save it to disk.

Note that, on the browsers that support it, the default filename for the
saved data is ``toyplot.csv``. You can override this default on a
per-data-table basis by specifying the filename when you create your
figure. For example, when exporting data from the following figure
(again, for browsers that support setting a default filename), the
filename will default to ``employee-schedules.csv``:

.. code:: python

    canvas, axes, mark = toyplot.bars(boundaries, baseline=None, filename="employee-schedules", title=title, width=500, height=300)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-edfcf7e4eb3b> in <module>()
    ----> 1 canvas, axes, mark = toyplot.bars(boundaries, baseline=None, filename="employee-schedules", title=title, width=500, height=300)
    

    NameError: name 'toyplot' is not defined


Note that the filename you specify should not include a file extension,
as the file extension is added for you (and other file formats may
become available in the future).
