# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for managing scene graphs.

Note that the scenegraph is an internal implementation detail for developers
adding new functionality to Toyplot, casual Toyplot users will never need to
work with it.
"""

import collections


##########################################################################
# AdjacencyList

class AdjacencyList(object):
    """Adjaceny list representation for a directed graph."""
    def __init__(self):
        self._targets = collections.defaultdict(list)

    def add_edge(self, source, target):
        """Add a directed edge from `source` to `target`."""
        self._targets[source].append(target)

    def remove_edge(self, source, target):
        """Remove the directed edge from `source` to `target`, if it exists."""
        self._targets[source].remove(target)

    def sources(self, target):
        """Return nodes that are connected to `target` via incoming edges."""
        return [source for source, targets in self._targets.items() if target in targets]

    def targets(self, source):
        """Return nodes are connected to `source` via outgoing edges."""
        return self._targets.get(source, [])

##########################################################################
# SceneGraph

class SceneGraph(object):
    """Collection of graphs representing semantic relationships among a (small number) of canvas objects.
    """
    def __init__(self):
        self._relationships = {}

    def __repr__(self):
        result = "<toyplot.scenegraph.SceneGraph at 0x{:x}>".format(id(self))
        for relationship, graph in self._relationships.items():
            result += "\n  Relationship: {}".format(relationship)
            for source, targets in graph._targets.items():
                result += "\n    {!r} ->".format(source)
                for target in targets:
                    result += "\n      {!r}".format(target)
        return result

    def add_edge(self, source, relationship, target):
        """Add an edge of type `relationship` from `source` to `target`.
        """
        if not isinstance(relationship, str):
            raise ValueError("Relationship must be a string.")
        if relationship not in self._relationships:
            self._relationships[relationship] = AdjacencyList()
        self._relationships[relationship].add_edge(source, target)

    def remove_edge(self, source, relationship, target):
        """Remove an edge of type `relationship` from `source` to `target`, if one exists.
        """
        if not isinstance(relationship, str):
            raise ValueError("Relationship must be a string.")
        if relationship not in self._relationships:
            return
        self._relationships[relationship].remove_edge(source, target)

    def sources(self, relationship, target):
        """Return nodes that are connected to `target` via incoming edges of type `relationship`, if any."""
        if not isinstance(relationship, str):
            raise ValueError("Relationship must be a string.")
        if relationship not in self._relationships:
            return []
        return self._relationships[relationship].sources(target)

    def source(self, relationship, target):
        """Return a single node that is connected to `target` via an incoming edge of type `relationship`.

        Raises an exception if there isn't exactly one incoming edge of type `relationship`.
        """
        if not isinstance(relationship, str):
            raise ValueError("Relationship must be a string.")
        result = self.sources(relationship, target)
        if len(result) != 1:
            raise RuntimeError("Expected one source, found {}.".format(len(result)))
        return result[0]

    def targets(self, source, relationship):
        """Return nodes are connected to `source` via outgoing edges of type `relationship`."""
        if not isinstance(relationship, str):
            raise ValueError("Relationship must be a string.")
        if relationship not in self._relationships:
            return []
        return self._relationships[relationship].targets(source)

