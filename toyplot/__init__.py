# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

__version__ = "0.4.0"

from toyplot.canvas import Canvas

def bars(a, b=None, c=None, along="x", baseline="stacked", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style=None):
  """Convenience function for creating a bar plot in a single call.

  See :meth:`toyplot.axes.Cartesian.bars`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.axes.Cartesian`
    A new set of 2D axes that fill the canvas.
  mark: :class:`toyplot.mark.BarMagnitudes` or :class:`toyplot.mark.BarBoundaries`
    The new bar mark.
  """
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.bars(a=a, b=b, c=c, along=along, baseline=baseline, fill=fill, colormap=colormap, palette=palette, opacity=opacity, title=title, style=style)
  return canvas, axes, mark

def fill(a, b=None, c=None, along="x", baseline=None, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style=None):
  """Convenience function for creating a fill plot in a single call.

  See :meth:`toyplot.axes.Cartesian.fill`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.axes.Cartesian`
    A new set of 2D axes that fill the canvas.
  mark: :class:`toyplot.mark.FillBoundaries` or :class:`toyplot.mark.FillMagnitudes`
    The new bar mark.
  """
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.fill(a=a, b=b, c=c, along=along, baseline=baseline, fill=fill, colormap=colormap, palette=palette, opacity=opacity, title=title, style=style)
  return canvas, axes, mark

def plot(a, b=None, along="x", color=None, colormap=None, palette=None, stroke_width=2.0, stroke_opacity=1.0, marker=None, size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style=None, mstyle=None, mlstyle=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style=None):
  """Convenience function for creating a line plot in a single call.

  See :meth:`toyplot.axes.Cartesian.plot`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.axes.Cartesian`
    A new set of 2D axes that fill the canvas.
  mark: :class:`toyplot.mark.Plot`
    The new plot mark.
  """
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.plot(a=a, b=b, along=along, color=color, colormap=colormap, palette=palette, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, fill_colormap=fill_colormap, fill_palette=fill_palette, opacity=opacity, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle)
  return canvas, axes, mark

def scatterplot(a, b=None, along="x", color=None, colormap=None, palette=None, marker="o", size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style=None, mstyle=None, mlstyle=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style=None):
  """Convenience function for creating a scatter plot in a single call.

  See :meth:`toyplot.axes.Cartesian.scatterplot`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.axes.Cartesian`
    A new set of 2D axes that fill the canvas.
  mark: :class:`toyplot.mark.Plot`
    The new scatter plot mark.
  """
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.scatterplot(a=a, b=b, along=along, color=color, colormap=colormap, palette=palette, marker=marker, size=size, fill=fill, fill_colormap=fill_colormap, fill_palette=fill_palette, opacity=opacity, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle)
  return canvas, axes, mark

