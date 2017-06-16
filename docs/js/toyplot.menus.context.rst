toyplot/menus/context module
============================

.. js:module::toyplot/menus/context

The `toyplot/menus/context` module provides functionality to display custom
context menu entries when the user right-clicks over a figure.

.. js:function:: toyplot/menus/context.add_item(label, show, activate)

    Adds a new menu item to the context menu.  Each menu item has a label, a
    callback to determine when item should be visible, and a callback to
    performe some action when the item is activated by the user.  Typically,
    menu items are added by individual marks, and the visibility callback
    will show the item if the mouse pointer was over the mark when the
    context menu was opened.  For example::

        context.require(
            dependencies["toyplot/menus/context"],
            code="""function(menus)
            {
                // This item will always be visible.
                function show() { return true; }
                function activate() { console.log("Hello, World!"); }
                menus.add_item("Hello World!", show, activate);
            }""")

    Note that the Toyplot context menu will not be shown if there are no visible items.  When this happens
    the system context menu will be shown instead.

    :param string label: Human readable label for the menu item to be added.
    :param function show: Callback function that will be called before the context menu is opened.
        The function must take one argument - the DOM event that is causing the
        context menu to be shown (such as a `contextmenu` or `mousedown`
        event).  The callback should return `true` if the menu item should be
        visible, or `false` otherwise.
    :param function activate: Callback function that will be called if the user selects this item.
