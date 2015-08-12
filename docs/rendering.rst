
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _rendering:

Rendering
---------

Of course, any plotting library needs a way to render figures for
display, and Toyplot is no exception. To integrate Toyplot into your
workflow as easily as possible, we provide three different rendering
mechanisms:

Backends
~~~~~~~~

At the lowest level, Toyplot provides a large collection of rendering
``backends``. Each backend knows how to render a Toyplot canvas to a
specific file format, and can typically render the canvas directly to
disk, to a buffer you provide, or return the raw representation of the
canvas for further processing. You choose a backend that provides the
file format you want to generate, and use it to explicitly render your
canvas. For example, you could use the :mod:`toyplot.pdf` backend to
save a figure as a vector PDF image on disk:

.. code:: python

    import toyplot.pdf
    toyplot.pdf.render(canvas, "figure1.pdf")

Similarly, you could substitute the :mod:`toyplot.png` backend to save
a PNG bitmap image:

.. code:: python

    import toyplot.png
    toyplot.png.render(canvas, "figure1.png")

You could do the same with the :mod:`toyplot.svg` backend, but suppose
you wanted to add a custom CSS class to the SVG markup for inclusion in
a publishing workflow. To accomodate this, the SVG backend can return a
DOM for further editing, instead of saving it directly to disk:

.. code:: python

    import toyplot.svg
    svg = toyplot.svg.render(canvas)
    svg.attrib["class"] = "MyCustomClass"
    import xml.etree.ElementTree as xml
    with open("figure1.svg", "wb") as file:
        file.write(xml.tostring(svg))

Finally, there is Toyplot's most important backend,
:mod:`toyplot.html` which produces the preferred interactive HTML
representation of a canvas. Like the other backends, you can use it to
write directly to disk, or return a DOM object for editing as-needed:

.. code:: python

    import toyplot.html
    toyplot.html.render(canvas, "figure1.html")

Note that the file produced by this backend is a completely
self-contained HTML fragment that could be emailed directly to a
colleague, inserted into a larger HTML document, etc.

Displays
~~~~~~~~

While backends are useful when you wish to save a canvas to disk for
incorporation into a paper or some larger workflow, in many cases you
may find yourself simply wanting to display the results of some
computation. Writing files to disk and opening them in a separate
application can be time-consuming and frustrating, particularly when
running a script repeatedly during development. For this case, Toyplot
provides ``display`` modules, which provide convenient ways to display
figures interactively. The most portable of these modules is
:mod:`toyplot.browser`:

.. code:: python

    import toyplot.browser
    toyplot.browser.show(canvas)

This will open a new browser window containing your figure, with all of
Toyplot's interaction and features intact.

If you prefer, an experimental new Qt display is available. It also
displays figures in a popup window with full interaction; in the future
it may grow to include additional Toyplot-specific functionality:

.. code:: python

    import toyplot.qt
    toyplot.qt.show(canvas)

Autorendering
~~~~~~~~~~~~~

For interactive environments such as
`Jupyter <http://www.ipython.org>`__, Toyplot's *autorender* feature
automatically renders a canvas into a notebook cell using Toyplot's
preferred interactive HTML representation. We use autorendering with few
exceptions throughout this documentation ... for example, executing the
following automatically inserts a figure into a Jupyter notebook:

.. code:: python

    import numpy
    x = numpy.linspace(0, 1)
    y = x ** 2

.. code:: python

    import toyplot
    canvas = toyplot.Canvas(width=300)
    canvas.axes().plot(x, y);


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-2-055b10ffce5d> in <module>()
    ----> 1 import toyplot
          2 canvas = toyplot.Canvas(width=300)
          3 canvas.axes().plot(x, y);


    ImportError: No module named toyplot


Note that no special import statements, magics, backends, or
configuration is required - Toyplot Just Works. In this case,
autorendering is enabled by default when you create a new canvas.
Toyplot knows that it's being run in the Jupyter notebook environment,
and when you execute a notebook cell that contains a canvas with
autorendering enabled, it inserts the rendered canvas in the cell
output. Note that this is not the same as Jupyter's rich output system -
a Toyplot canvas doesn't have to be the result of an expression to be
rendered, and you can create multiple Toyplot canvases in a single
notebook cell (handy when producing multiple figures in a loop), and
they will all be rendered.

Autorendering for a canvas is automatically disabled if you pass it to a
rendering backend or a display. So while the above example automatically
rendered the canvas into a notebook cell, the following will not:

.. code:: python

    canvas = toyplot.Canvas(width=300)
    canvas.axes().plot(x, y)
    toyplot.pdf.render(canvas, "figure2.pdf")

In some circumstances you may want to disable autorendering yourself,
which you can do when the canvas is created:

.. code:: python

    canvas = toyplot.Canvas(width=300, autorender=False)
    canvas.axes().plot(x, y);


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-c62d7b01a26d> in <module>()
    ----> 1 canvas = toyplot.Canvas(width=300, autorender=False)
          2 canvas.axes().plot(x, y);


    NameError: name 'toyplot' is not defined

