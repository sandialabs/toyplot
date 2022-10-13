# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

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


def layout_children(item, item_top, item_right, item_bottom, item_left):
    item_width = item_right - item_left
    item_height = item_bottom - item_top

    # Identify which layout to apply to the item's children.
    display = inner_display(item)
    if display == "flow":
        for child in item:
            display = outer_display(child)
            if display != "block":
                raise ValueError(f"Unsupported outer display type: {display}")
            position = child.get("position", "fixed")
            if position != "fixed":
                raise ValueError(f"Unsupported position type: {position}")

            top = toyplot.units.convert(child.get("top", 0), target="px", default="px", reference=item_height)
            right = toyplot.units.convert(child.get("right", 0), target="px", default="px", reference=item_width)
            bottom = toyplot.units.convert(child.get("bottom", 0), target="px", default="px", reference=item_height)
            left = toyplot.units.convert(child.get("left", 0), target="px", default="px", reference=item_width)

            margin_top, margin_right, margin_bottom, margin_left = shortcut(child, "margin", item_width)
            padding_top, padding_right, padding_bottom, padding_left = shortcut(child, "padding", item_width)

            child.set("boxcat:padding-edge", (
                item_top + margin_top + top,
                item_right - margin_right - right,
                item_bottom - margin_bottom - bottom,
                item_left + margin_left + left,
                ))
            child.set("boxcat:content-edge", (
                item_top + margin_top + padding_top + top,
                item_right - margin_right - padding_right - right,
                item_bottom - margin_bottom - padding_bottom - bottom,
                item_left + margin_left + padding_left + left,
                ))

#            child_top = item_top + margin_top + padding_top + top
#            child_right = item_right - margin_right - padding_right - right
#            child_bottom = item_bottom - margin_bottom - padding_bottom - bottom
#            child_left = item_left + margin_left + padding_left + left
#
#            child.set("boxcat:top", child_top)
#            child.set("boxcat:right", child_right)
#            child.set("boxcat:bottom", child_bottom)
#            child.set("boxcat:left", child_left)

            layout_children(child, child_top, child_right, child_bottom, child_left)
    else:
        raise ValueError(f"Unsupported inner display type: {display}")


def layout(item):
    # Convert item size to pixels.
    left = 0
    top = 0
    right = toyplot.units.convert(item.get("width"), target="px", default="px")
    bottom = toyplot.units.convert(item.get("height"), target="px", default="px")

    item.set("boxcat:left", left)
    item.set("boxcat:right", right)
    item.set("boxcat:top", top)
    item.set("boxcat:bottom", bottom)

    # Layout the item's children
    layout_children(item, top, right, bottom, left)


def graphcat_layout(graph, name, inputs):
    original = inputs.getone(None)
    modified = copy.deepcopy(original)
    layout(modified)
    return modified
