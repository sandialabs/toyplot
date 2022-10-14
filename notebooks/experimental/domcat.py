# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Proof-of-concept DOM manipulation using Graphcat."""

import copy
import io
import xml.etree.ElementTree as xml

def append_element(graph, name, inputs):
    """Graphcat task function that appends one element as a child of another."""
    parent = copy.copy(inputs.getone("parent"))
    child = inputs.getone("child")
    parent.append(child)
    return parent


def create_element(tag, attrib={}, **extra):
    """Graphcat task function that creates an element."""
    def implementation(graph, name, inputs):
        return xml.Element(tag, attrib=attrib, **extra)
    return implementation


def dump(element, level=0):
    """Recursively pretty-print an element and its children."""
    indent = "  " * level
    attributes = "".join(f" {key}=\"{str(value)}\"" for key, value in element.items())
    if len(element) or element.text:
        print(f"{indent}<{element.tag}{attributes}>")
        if element.text:
            print(f"{indent}  {element.text}")
        for child in element:
            dump(child, level+1)
        print(f"{indent}</{element.tag}>")
    else:
        print(f"{indent}<{element.tag}{attributes}/>")


def set_attribute(key, value):
    """Graphcat task function that sets an element attribute."""
    def implementation(graph, name, inputs):
        original = inputs.getone(None)
        modified = xml.Element(original.tag, attrib=original.attrib)
        for child in original:
            modified.append(child)
        modified.set(key, value)
        return modified
    return implementation


def tostring(element):
    """Convert an element to a compact string representation."""
    attributes = "".join(f" {key}=\"{str(value)}\"" for key, value in element.items())
    if len(element) or element.text:
        result = f"<{element.tag}{attributes}>"
        if element.text:
            result += element.text
        for child in element:
            result += tostring(child)
        return result + f"</{element.tag}>"
    return f"<{element.tag}{attributes}/>"

