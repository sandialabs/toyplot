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

    :param string mime_type: MIME type of the data to be saved (e.g. "text/csv").
    :param string charset: Character encoding of the data to be saved (e.g. "utf-8").
    :param string data: Data content to be saved.
    :param string filename: Suggested filename to use for saving the data to disk.


