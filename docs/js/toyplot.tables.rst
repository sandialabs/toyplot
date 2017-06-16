toyplot/tables module
=====================

.. js:module::toyplot/tables

The `toyplot/tables` module can be used to store tabular data for later retrieval.

.. js:function:: toyplot/tables.store(owner, key, names, columns)

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


.. js:function:: toyplot/tables.get_csv(owner, key)

    Retrieve the CSV representation of a table stored previously using :js:func:`toyplot/tables.store`.  For example::

        context.require(
            dependencies=["toyplot/tables"],
            arguments=[mark_id],
            code="""function(tables, mark_id)
            {
                console.log(tables.get_csv(mark_id, "vertex_data"));
            }""")

    :param string owner: Unique id for the object that "owns" the table.
    :param string key: Used to disambiguate tables when the owner has more than one.

    :returns: String containing the CSV representation of the table.
