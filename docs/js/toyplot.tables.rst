toyplot/tables module
=====================

.. js:module::toyplot/tables

The `toyplot/tables` module can be used to store tabular data for later retrieval.

.. js:function:: toyplot/tables.set(owner, key, names, columns)

    Store tabular information, identified by owner and key, for later retrieval.  For example::

        context.require(
            dependencies=["toyplot/tables"],
            arguments=[mark_id, column_names, columns],
            code="""function(tables, mark_id, column_names, columns)
            {
                tables.store(mark_id, "vertex_data", column_names, columns);
            }""")

    :param string owner: Unique id for the object that "owns" the table.
    :param string key: Used to disambiguate tables when the owner has more than one.
    :param array names: Names for each column in the table.
    :param array columns: Array of values for eacn column in the table.


.. js:function:: toyplot/tables.get(owner, key)

    Retrieve a table stored previously using :js:func:`toyplot/tables.set`.  For example::

        context.require(
            dependencies=["toyplot/tables"],
            arguments=[graph_id],
            code="""function(tables, graph_id)
            {
                console.log(tables.get(graph_id, "vertex_data"));
            }""")

    :param string owner: Unique id for the object that "owns" the table.
    :param string key: Used to disambiguate tables when the owner has more than one.

    :returns: object containing `names` and `columns` arrays, containing the
    table column names and column values, respectively.
