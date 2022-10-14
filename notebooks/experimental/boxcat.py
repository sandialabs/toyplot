# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Proof-of-concept box layout algorithm for a DOM tree."""

import copy

import toyplot.units


def inner_display(item):
    return item.get("display", "flow")


def outer_display(item):
    return item.get("display", "block")


def shortcut(item, name, parent_width):
    top = right = bottom = left = 0

    if name in item.attrib:
        value = str(item.get(name)).split()
        if len(value) == 1:
            top = right = bottom = left = value[0]
        elif len(value) == 2:
            top = bottom = value[0]
            left = right = value[1]
        elif len(value) == 3:
            top = value[0]
            left = right = value[1]
            bottom = value[2]
        elif len(value) == 4:
            top, right, bottom, left = value
        else:
            raise ValueError(f"Unsupported {name} value: {value}")

    top = item.get(f"{name}-top", top)
    right = item.get(f"{name}-right", right)
    bottom = item.get(f"{name}-bottom", bottom)
    left = item.get(f"{name}-left", left)

    top = toyplot.units.convert(top, target="px", default="px", reference=parent_width)
    right = toyplot.units.convert(right, target="px", default="px", reference=parent_width)
    bottom = toyplot.units.convert(bottom, target="px", default="px", reference=parent_width)
    left = toyplot.units.convert(left, target="px", default="px", reference=parent_width)

    return top, right, bottom, left


def layout_children(parent, parent_top, parent_right, parent_bottom, parent_left):
    """Apply the box layout algorithm to a DOM element's children."""
    parent_width = parent_right - parent_left
    parent_height = parent_bottom - parent_top

    # Identify which layout to apply to the parent's children.
    display = inner_display(parent)
    if display == "flow":
        for child in parent:
            display = outer_display(child)
            if display != "block":
                raise ValueError(f"Unsupported outer display type: {display}")
            position = child.get("position", "fixed")
            if position != "fixed":
                raise ValueError(f"Unsupported position type: {position}")

            top = toyplot.units.convert(child.get("top", 0), target="px", default="px", reference=parent_height)
            right = toyplot.units.convert(child.get("right", 0), target="px", default="px", reference=parent_width)
            bottom = toyplot.units.convert(child.get("bottom", 0), target="px", default="px", reference=parent_height)
            left = toyplot.units.convert(child.get("left", 0), target="px", default="px", reference=parent_width)

            margin_top, margin_right, margin_bottom, margin_left = shortcut(child, "margin", parent_width)
            padding_top, padding_right, padding_bottom, padding_left = shortcut(child, "padding", parent_width)

#            child_padding_top = parent_top + margin_top + top)
#            child_padding_right = parent_right - margin_right - right)
#            child_padding_bottom = parent_bottom - margin_bottom - bottom)
#            child_padding_left = parent_left + margin_left + left)
#            child.set("boxcat:padding", (child_padding_top, child_padding_right, child_padding_bottom, child_padding_left))

            child_content_top = parent_top + margin_top + padding_top + top
            child_content_right = parent_right - margin_right - padding_right - right
            child_content_bottom = parent_bottom - margin_bottom - padding_bottom - bottom
            child_content_left = parent_left + margin_left + padding_left + left
            child.set("boxcat:content", (child_content_top, child_content_right, child_content_bottom, child_content_left))

            layout_children(child, child_content_top, child_content_right, child_content_bottom, child_content_left)
    else:
        raise ValueError(f"Unsupported inner display type: {display}")


def layout(item):
    """Apply the box layout algorithm to the root of a DOM tree."""

    # The top level item *must* have width and height attributes.
    left = 0
    top = 0
    right = toyplot.units.convert(item.get("width"), target="px", default="px")
    bottom = toyplot.units.convert(item.get("height"), target="px", default="px")
    item.set("boxcat:content", (top, right, bottom, left))

    # Layout the item's children
    layout_children(item, top, right, bottom, left)


def graphcat_layout(graph, name, inputs):
    """Graphcat task function that applies the box layout algorithm to a DOM tree."""
    original = inputs.getone(None)
    modified = copy.deepcopy(original)
    layout(modified)
    return modified
