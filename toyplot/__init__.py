# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Provides the top-level :ref:`convenience-api`, which allows you to create
many plots using a single compact statement.
"""

from __future__ import division

__version__ = "0.13.0"

from toyplot.canvas import Canvas
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)

def bars(
        a,
        b=None,
        c=None,
        along="x",
        baseline="stacked",
        color=None,
        opacity=1.0,
        title=None,
        style=None,
        filename=None,
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        show=True,
        xshow=True,
        yshow=True,
        label=None,
        xlabel=None,
        ylabel=None,
        xscale="linear",
        yscale="linear",
        padding=10,
        width=None,
        height=None,
        ):
    """Convenience function for creating a bar plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.bars`,
    :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for
    parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
      A new canvas object.
    axes: :class:`toyplot.coordinates.Cartesian`
      A new set of 2D axes that fill the canvas.
    mark: :class:`toyplot.mark.BarMagnitudes` or :class:`toyplot.mark.BarBoundaries`
      The new bar mark.
    """
    canvas = Canvas(width=width, height=height)
    axes = canvas.cartesian(
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        show=show,
        xshow=xshow,
        yshow=yshow,
        label=label,
        xlabel=xlabel,
        ylabel=ylabel,
        xscale=xscale,
        yscale=yscale,
        padding=padding)
    mark = axes.bars(
        a=a,
        b=b,
        c=c,
        along=along,
        baseline=baseline,
        color=color,
        opacity=opacity,
        title=title,
        style=style,
        filename=filename)
    return canvas, axes, mark


def fill(
        a,
        b=None,
        c=None,
        along="x",
        baseline=None,
        color=None,
        opacity=1.0,
        title=None,
        style=None,
        filename=None,
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        show=True,
        xshow=True,
        yshow=True,
        label=None,
        xlabel=None,
        ylabel=None,
        xscale="linear",
        yscale="linear",
        padding=10,
        width=None,
        height=None,
        ):
    """Convenience function for creating a fill plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.fill`,
    :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for
    parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
      A new canvas object.
    axes: :class:`toyplot.coordinates.Cartesian`
      A new set of 2D axes that fill the canvas.
    mark: :class:`toyplot.mark.FillBoundaries` or :class:`toyplot.mark.FillMagnitudes`
      The new bar mark.
    """
    canvas = Canvas(width=width, height=height)
    axes = canvas.cartesian(
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        show=show,
        xshow=xshow,
        yshow=yshow,
        label=label,
        xlabel=xlabel,
        ylabel=ylabel,
        xscale=xscale,
        yscale=yscale,
        padding=padding)
    mark = axes.fill(
        a=a,
        b=b,
        c=c,
        along=along,
        baseline=baseline,
        color=color,
        opacity=opacity,
        title=title,
        style=style,
        filename=filename)
    return canvas, axes, mark


def graph(
        a,
        b=None,
        c=None,
        olayout=None,
        layout=None,
        along="x",
        vlabel=None,
        vcoordinates=None,
        vcolor=None,
        vmarker="o",
        varea=None,
        vsize=None,
        vopacity=1.0,
        vtitle=None,
        vstyle=None,
        vlstyle=None,
        vlshow=True,
        ecolor=None,
        ewidth=1.0,
        eopacity=1.0,
        estyle=None,
        padding=20,
        width=None,
        height=None,
        ): # pragma: no cover
    """Convenience function for creating a graph plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.graph`,
    :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for
    parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
        A new canvas object.
    axes: :class:`toyplot.coordinates.Cartesian`
        A new set of 2D axes that fill the canvas.
    mark: :class:`toyplot.mark.Graph`
        The new graph mark.
    """
    canvas = Canvas(width=width, height=height)
    axes = canvas.cartesian(aspect="fit-range", show=False, padding=padding)
    mark = axes.graph(
        a=a,
        b=b,
        c=c,
        olayout=olayout,
        layout=layout,
        along=along,
        vlabel=vlabel,
        vcoordinates=vcoordinates,
        vcolor=vcolor,
        vmarker=vmarker,
        varea=varea,
        vsize=vsize,
        vopacity=vopacity,
        vtitle=vtitle,
        vstyle=vstyle,
        vlstyle=vlstyle,
        vlshow=vlshow,
        ecolor=ecolor,
        ewidth=ewidth,
        eopacity=eopacity,
        estyle=estyle,
        )
    return canvas, axes, mark


def image(
        data,
        width=None,
        height=None,
        ): # pragma: no cover
    """Convenience function for displaying an image in a single call.

    See :meth:`toyplot.canvas.Canvas.image`, and :class:`toyplot.canvas.Canvas`
    for parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
        A new canvas object.
    mark: :class:`toyplot.mark.Image`
        The new image mark.
    """
    canvas = Canvas(width=width, height=height)
    mark = canvas.image(
        data=data,
        )
    return canvas, mark


def matrix(
        data,
        label=None,
        tlabel=None,
        llabel=None,
        rlabel=None,
        blabel=None,
        step=1,
        tshow=None,
        lshow=None,
        rshow=None,
        bshow=None,
        tlocator=None,
        llocator=None,
        rlocator=None,
        blocator=None,
        colorshow=False,
        width=None,
        height=None,
        filename=None,
        ):
    """Convenience function to create a matrix visualization in a single call.

    See :meth:`toyplot.canvas.Canvas.matrix`, and
    :class:`toyplot.canvas.Canvas` for parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
      A new canvas object.
    table: :class:`toyplot.coordinates.Table`
      A new set of table axes that fill the canvas.
    """
    canvas = Canvas(width=width, height=height)
    axes = canvas.matrix(
        data=data,
        label=label,
        tlabel=tlabel,
        llabel=llabel,
        rlabel=rlabel,
        blabel=blabel,
        step=step,
        tshow=tshow,
        lshow=lshow,
        rshow=rshow,
        bshow=bshow,
        tlocator=tlocator,
        llocator=llocator,
        rlocator=rlocator,
        blocator=blocator,
        colorshow=colorshow,
        filename=filename,
        )
    return canvas, axes


def plot(
        a,
        b=None,
        along="x",
        color=None,
        stroke_width=2.0,
        opacity=1.0,
        title=None,
        marker=None,
        area=None,
        size=None,
        mfill=None,
        mopacity=1.0,
        mtitle=None,
        style=None,
        mstyle=None,
        mlstyle=None,
        filename=None,
        aspect=None,
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        show=True,
        xshow=True,
        yshow=True,
        label=None,
        xlabel=None,
        ylabel=None,
        xscale="linear",
        yscale="linear",
        padding=10,
        width=None,
        height=None,
        ):
    """Convenience function for creating a line plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.plot`,
    :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for
    parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
      A new canvas object.
    axes: :class:`toyplot.coordinates.Cartesian`
      A new set of 2D axes that fill the canvas.
    mark: :class:`toyplot.mark.Plot`
      The new plot mark.
    """
    canvas = Canvas(width=width, height=height)
    axes = canvas.cartesian(
        aspect=aspect,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        show=show,
        xshow=xshow,
        yshow=yshow,
        label=label,
        xlabel=xlabel,
        ylabel=ylabel,
        xscale=xscale,
        yscale=yscale,
        padding=padding)
    mark = axes.plot(
        a=a,
        b=b,
        along=along,
        color=color,
        stroke_width=stroke_width,
        opacity=opacity,
        title=title,
        marker=marker,
        area=area,
        size=size,
        mfill=mfill,
        mopacity=mopacity,
        mtitle=mtitle,
        style=style,
        mstyle=mstyle,
        mlstyle=mlstyle,
        filename=filename)
    return canvas, axes, mark


def scatterplot(
        a,
        b=None,
        along="x",
        color=None,
        marker="o",
        area=None,
        size=None,
        opacity=1.0,
        title=None,
        style=None,
        mstyle=None,
        mlstyle=None,
        filename=None,
        aspect=None,
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        show=True,
        xshow=True,
        yshow=True,
        label=None,
        xlabel=None,
        ylabel=None,
        xscale="linear",
        yscale="linear",
        padding=10,
        width=None,
        height=None,
        ):
    """Convenience function for creating a scatter plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.scatterplot`,
    :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for
    parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
      A new canvas object.
    axes: :class:`toyplot.coordinates.Cartesian`
      A new set of 2D axes that fill the canvas.
    mark: :class:`toyplot.mark.Plot`
      The new scatter plot mark.
    """
    canvas = Canvas(width=width, height=height)
    axes = canvas.cartesian(
        aspect=aspect,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        show=show,
        xshow=xshow,
        yshow=yshow,
        label=label,
        xlabel=xlabel,
        ylabel=ylabel,
        xscale=xscale,
        yscale=yscale,
        padding=padding)
    mark = axes.scatterplot(
        a=a,
        b=b,
        along=along,
        color=color,
        marker=marker,
        area=area,
        size=size,
        opacity=opacity,
        title=title,
        style=style,
        mstyle=mstyle,
        mlstyle=mlstyle,
        filename=filename)
    return canvas, axes, mark


def table(
        data=None,
        rows=None,
        columns=None,
        trows=None,
        brows=None,
        lcolumns=None,
        rcolumns=None,
        label=None,
        width=None,
        height=None,
        filename=None,
        ):
    """Convenience function to create a table visualization in a single call.

    See :meth:`toyplot.canvas.Canvas.table`, and :class:`toyplot.canvas.Canvas`
    for parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
      A new canvas object.
    table: :class:`toyplot.coordinates.Table`
      A new set of table axes that fill the canvas.
    """
    canvas = Canvas(width=width, height=height)
    axes = canvas.table(
        data=data,
        rows=rows,
        columns=columns,
        trows=trows,
        brows=brows,
        lcolumns=lcolumns,
        rcolumns=rcolumns,
        label=label,
        filename=filename,
        )
    return canvas, axes
