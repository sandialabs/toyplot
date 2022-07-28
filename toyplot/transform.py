# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functions for manipulating transformation matrices."""


import numpy


def rotation(angle):
    """Return a 2D transformation matrix.

    Parameters
    ----------
    angle: number
      Rotation angle in degrees.  Positive values produce counterclockwise rotation.
    """
    theta = numpy.radians(angle)
    cos_theta = numpy.cos(theta)
    sin_theta = numpy.sin(theta)

    return numpy.array([[cos_theta, sin_theta], [-sin_theta, cos_theta]])
