
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _color:

Color
=====

Color choices are critical in visualization because good color choices
can reveal or emphasize patterns in your data while poor choices will
obscure them.

Palettes
--------

Much of the color management in Toyplot centers around
:class:`palette <toyplot.color.Palette>` objects, which store ordered
collections of RGBA colors. For example, consider Toyplot's default
palette:

.. code:: python

    import toyplot.color
    toyplot.color.Palette()


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-594bc2e88ee5> in <module>()
    ----> 1 import toyplot.color
          2 toyplot.color.Palette()


    ImportError: No module named toyplot.color


Note: Like other Toyplot objects, palettes are automatically rendered in
Jupyter notebooks, in this case as a collection of color swatches.

You will likely recognize the colors in the default palette, since they
are used to provide default colors for series when adding marks to a
plot. Although you can create your own custom palettes by passing a
sequence of colors to the :class:`toyplot.color.Palette` constructor,
we strongly recommend that you choose from the collection of
high-quality palettes that are builtin to Toyplot, and outlined in the
next section.

Color Brewer Palettes
---------------------

Toyplot includes a complete collection of high-quality palettes from
`Color Brewer <http://colorbrewer2.org>`__ which are ideal for
visualization (we will provide empirical evidence for this in the
section on linear color maps) and accessed by name:

.. code:: python

    print toyplot.color.brewer.names()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-1ba03da0f90d> in <module>()
    ----> 1 print toyplot.color.brewer.names()
    

    NameError: name 'toyplot' is not defined


.. code:: python

    toyplot.color.brewer("BlueYellowRed")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-9b699f0fb4c0> in <module>()
    ----> 1 toyplot.color.brewer("BlueYellowRed")
    

    NameError: name 'toyplot' is not defined


You can also reverse the order of any palette (though this should almost
never be necessary, as we will see shortly):

.. code:: python

    toyplot.color.brewer("BlueYellowRed", reverse=True)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-f2a4f99744ef> in <module>()
    ----> 1 toyplot.color.brewer("BlueYellowRed", reverse=True)
    

    NameError: name 'toyplot' is not defined


Each of the Color Brewer palettes comes in multiple variants with
different numbers of colors. By default, when you create a Color Brewer
palette, the one with the maximum number of colors is returned. However,
you can query for all of the available variants, and request one with
fewer colors if necessary:

.. code:: python

    toyplot.color.brewer.counts("BlueYellowRed")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-6dc8c67c9fd4> in <module>()
    ----> 1 toyplot.color.brewer.counts("BlueYellowRed")
    

    NameError: name 'toyplot' is not defined


.. code:: python

    toyplot.color.brewer("BlueYellowRed", 5)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-15b84e0d2be0> in <module>()
    ----> 1 toyplot.color.brewer("BlueYellowRed", 5)
    

    NameError: name 'toyplot' is not defined


Finally, each of the Color Brewer palettes are categorized as
"sequential", "diverging", or "qualitative", which you can query by
name:

.. code:: python

    toyplot.color.brewer.category("BlueYellowRed")


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-62876355fa05> in <module>()
    ----> 1 toyplot.color.brewer.category("BlueYellowRed")
    

    NameError: name 'toyplot' is not defined


Color Brewer Sequential Palettes
--------------------------------

Sequential color palettes are designed to visualize magnitudes for some
quantity of interest. Colors at one end of the palette are mapped to low
values and colors at the opposite end map to high values. Toyplot
includes the complete set of Color Brewer sequential palettes, reordered
where necessary so that the colors always progress from low luminance to
high luminance. This ensures that colormaps based on these palettes
always map low values to low luminance and high values to high luminance
(this is why you should never need to reverse a palette). The names of
the palettes have been modified from the originals to eliminate
abbreviations:

.. code:: python

    import IPython.display
    for name in toyplot.color.brewer.names():
        if toyplot.color.brewer.category(name) == "sequential":
            IPython.display.display_html(IPython.display.HTML("<b>%s</b>" % name))
            IPython.display.display(toyplot.color.brewer(name))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-be29b29a850f> in <module>()
          1 import IPython.display
    ----> 2 for name in toyplot.color.brewer.names():
          3     if toyplot.color.brewer.category(name) == "sequential":
          4         IPython.display.display_html(IPython.display.HTML("<b>%s</b>" % name))
          5         IPython.display.display(toyplot.color.brewer(name))


    NameError: name 'toyplot' is not defined


Color Brewer Diverging Palettes
-------------------------------

Diverging palettes are especially useful when visualizing signed
magnitudes, or magnitudes relative to some well-defined reference point,
such as a mean, median, or domain-specific critical value. Once again,
Toyplot includes the complete set of Color Brewer diverging palettes,
reordered so the colors consistently progress from cooler colors to
warmer colors, so low/negative values map to cool colors and
high/positive values map to warm colors, and renamed for consistency:

.. code:: python

    for name in toyplot.color.brewer.names():
        if toyplot.color.brewer.category(name) == "diverging":
            IPython.display.display_html(IPython.display.HTML("<b>%s</b>" % name))
            IPython.display.display(toyplot.color.brewer(name))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-24f76a7217c0> in <module>()
    ----> 1 for name in toyplot.color.brewer.names():
          2     if toyplot.color.brewer.category(name) == "diverging":
          3         IPython.display.display_html(IPython.display.HTML("<b>%s</b>" % name))
          4         IPython.display.display(toyplot.color.brewer(name))


    NameError: name 'toyplot' is not defined


Color Brewer Qualitative (Categorical) Palettes
-----------------------------------------------

Qualitative or categorical palettes are designed for visualizing
unordered information. Adjacent colors typically have high contrast in
hue or luminance, to emphasize boundaries between values. Toyplot
includes the full set of qualitative palettes from Color Brewer, without
modification:

.. code:: python

    for name in toyplot.color.brewer.names():
        if toyplot.color.brewer.category(name) == "qualitative":
            IPython.display.display_html(IPython.display.HTML("<b>%s</b>" % name))
            IPython.display.display(toyplot.color.brewer(name))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-d572533b5483> in <module>()
    ----> 1 for name in toyplot.color.brewer.names():
          2     if toyplot.color.brewer.category(name) == "qualitative":
          3         IPython.display.display_html(IPython.display.HTML("<b>%s</b>" % name))
          4         IPython.display.display(toyplot.color.brewer(name))


    NameError: name 'toyplot' is not defined


You may recognize "Set2" as Toyplot's default color palette.

Linear Color Maps
-----------------

While palettes group together related collections of colors, Toyplot
uses *color maps* to perform the work of mapping data values to colors.
The most important type of map in Toyplot is a
:class:`toyplot.color.LinearMap`, which uses linear interpolation to
map a continuous range of data values to a continuous range of colors,
provided by a palette:

.. code:: python

    toyplot.color.LinearMap(toyplot.color.brewer("BlueYellowRed"))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-8128487c9e92> in <module>()
    ----> 1 toyplot.color.LinearMap(toyplot.color.brewer("BlueYellowRed"))
    

    NameError: name 'toyplot' is not defined


Note that not all linear interpolations of colors are equal! Because the
human visual system is much more sensitive to changes in luminance than
changes in hue, we typically want to use color maps that generate a
linear range of luminance values. For example, the following figure
relates the relationship between data values and luminance values for
each of the Color Brewer sequential palettes:

.. code:: python

    import numpy
    def luma_plot(colormaps):
        grid_n = 4.0
        grid_m = numpy.ceil(len(colormaps) / grid_n)
        canvas = toyplot.Canvas(grid_n * 150, grid_m * 150)
        for index, (name, colormap) in enumerate(colormaps):
            x = numpy.linspace(0, 1, 200)
            y = [toyplot.color.to_lab(color)[0] for color in colormap.colors(x)]
    
            axes = canvas.axes(grid=(grid_m, grid_n, index), ymin=0, ymax=100, gutter=20, xshow=True, yshow=True, label=name)
            axes.scatterplot(x, y, size=10**2, fill=(x, colormap))

.. code:: python

    luma_plot([(name, toyplot.color.LinearMap(toyplot.color.brewer(name), 0, 1)) for name in toyplot.color.brewer.names() if toyplot.color.brewer.category(name) == "sequential"])


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-abd2c8a569b3> in <module>()
    ----> 1 luma_plot([(name, toyplot.color.LinearMap(toyplot.color.brewer(name), 0, 1)) for name in toyplot.color.brewer.names() if toyplot.color.brewer.category(name) == "sequential"])
    

    NameError: name 'toyplot' is not defined


And here are the diverging palettes, viewed in the same fashion:

.. code:: python

    luma_plot([(name, toyplot.color.LinearMap(toyplot.color.brewer(name), 0, 1)) for name in toyplot.color.brewer.names() if toyplot.color.brewer.category(name) == "diverging"])


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-14-3bbad180d6bc> in <module>()
    ----> 1 luma_plot([(name, toyplot.color.LinearMap(toyplot.color.brewer(name), 0, 1)) for name in toyplot.color.brewer.names() if toyplot.color.brewer.category(name) == "diverging"])
    

    NameError: name 'toyplot' is not defined


Note that for each of the palettes, the relationship between data and
luminance is very close to linear, minimizing distortion, and that the
diverging palettes provide a crisp transition between negative and
positive values. When we say that Color Brewer is a "high quality" set
of palettes, this is what we mean - the color choices in the Color
Brewer palettes generate close-to-optimal relationships between data and
luminance.

As a counterexample, here is the same analysis, applied to a low-quality
colormap (mis)used by many mainstream visualization libraries:

.. code:: python

    luma_plot([("jet", toyplot.color.LinearMap(toyplot.color.Palette(numpy.load("jet.npy")), 0, 1))])


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-0dde4d4d6a20> in <module>()
    ----> 1 luma_plot([("jet", toyplot.color.LinearMap(toyplot.color.Palette(numpy.load("jet.npy")), 0, 1))])
    

    NameError: name 'toyplot' is not defined


Note that this palette provides a complex luminance profile that makes
it a poor choice for sequential or diverging data.

Moreland Diverging Maps
-----------------------

As an alternative to the linear maps based on the Color Brewer diverging
palettes, Toyplot also provides a set of nonlinear diverging color maps
based on “Diverging Color Maps for Scientific Visualization” by Ken
Moreland at http://www.sandia.gov/~kmorel/documents/ColorMaps. You will
note in the following plots that the Moreland diverging color maps use a
much narrower range of available luminance - this is because they have
been carefully crafted to provide a perceptually uniform mapping that
takes both color and luminance into account to eliminate Mach banding
effects:

.. code:: python

    luma_plot([(name, toyplot.color.diverging(name, 0, 1)) for name in toyplot.color.diverging.names()])


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-675f60f27cdb> in <module>()
    ----> 1 luma_plot([(name, toyplot.color.diverging(name, 0, 1)) for name in toyplot.color.diverging.names()])
    

    NameError: name 'toyplot' is not defined


