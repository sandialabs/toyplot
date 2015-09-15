# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy
import toyplot.require

def prufer_tree(sequence):
        """Use a Prufer sequence to generate a tree.
        """
        sequence = toyplot.require.integer_vector(sequence)
        n = len(sequence)
        if numpy.any(sequence < 0) or numpy.any(sequence >= n+2):
            raise ValueError("Sequence values must be in the range [0, %s)" % n+2)

        sources = []
        targets = []

        degree = numpy.ones(n+2, dtype="int64")
        for i in sequence:
                degree[i] += 1

        for i in sequence:
            for j in numpy.arange(n+2):
                if degree[j] == 1:
                    sources.append(i)
                    targets.append(j)
                    degree[i] -= 1
                    degree[j] -= 1
                    break

        u, v = numpy.flatnonzero(degree == 1)
        sources.append(u)
        targets.append(v)

        return numpy.column_stack((sources, targets))

