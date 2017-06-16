toyplot/canvas/id module
========================

.. js:module::toyplot/canvas/id

The `toyplot/canvas/id` module is a string containing the globally-unique HTML
DOM id for the SVG element containing a Toyplot figure.  You can use this id to
reference the SVG element and make changes.  For example::

    context.require(dependencies=["toyplot/canvas/id"], code="""function(canvas_id)
    {
        var canvas = document.querySelector("#" + canvas_id);
        /* Make changes to the figure using canvas. */
    }""")

