toyplot/io module
=================

.. js:module::toyplot/io

The `toyplot/io` module contains functionality for exporting data from the viewer's browser.

.. js:function:: toyplot/io.save_file(mime_type, charset, data, filename)

    Save data from the viewer's browser to a file.  For example::

        context.require(
            dependencies=["toyplot/tables", "toyplot/io"],
            code="""function(tables, io)
            {
                var data = tables.get_csv("my-graph", "vertices");
                io.save_file("text/csv", "utf-8", data, "my-graph-vertices.csv");
            }""")

    Note that the behavior of individual browsers when saving files will vary -
    they may-or-may not prompt the user to choose an alternate filename, or
    offer to open the file in some other application instead.

    :param mime_type: String MIME type of the data to be saved (e.g. "text/csv").
    :param charset: String character encoding of the data to be saved (e.g. "utf-8").
    :param data: String data to be saved.
    :param filename: Suggested filename string to use for saving the data to disk.


