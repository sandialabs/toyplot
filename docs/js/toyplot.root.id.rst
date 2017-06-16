toyplot/root/id module
======================

.. js:module::toyplot/root/id

The `toyplot/root/id` module is a string containing the globally-unique HTML DOM
id for a Toyplot figure.  You can use this id to reference the outer DOM
element that contains the figure.  For example::

    context.require(dependencies=["toyplot/root/id"], code="""function(root_id)
    {
        var root = document.querySelector("#" + root_id);
        /* Make global changes to the figure using root. */
    }""")

