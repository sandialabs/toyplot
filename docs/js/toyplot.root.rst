toyplot/root module
===================

.. js:module::toyplot/root

The `toyplot/root` module is a reference to the outer DOM element that contains
the figure.  For example::

    context.require(dependencies=["toyplot/root"], code="""function(root)
    {
        /* Make global changes to the figure using root. */
    }""")

