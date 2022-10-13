# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Provides the top-level :ref:`convenience-api`, which allows you to create
many plots using a single compact statement.
"""

import logging
import sys

if sys.version_info.major < 3:
    raise RuntimeError("As of version 0.19, Toyplot requires Python 3.  For Python 2 support, use Toyplot version 0.18")

from toyplot.canvas import Canvas

__version__ = "1.0.3"

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)
log.addHandler(logging.NullHandler())


class DeprecationWarning(Warning):
    """Used with :func:`warnings.warn` to mark deprecated API."""
    pass


def bars(
        a,
        b=None,
        c=None,
        along="x",
        baseline="stacked",
        color=None,
        filename=None,
        height=None,
        hyperlink=None,
        label=None,
        margin=50,
        opacity=1.0,
        padding=10,
        show=True,
        style=None,
        title=None,
        width=None,
        xlabel=None,
        xmax=None,
        xmin=None,
        xscale="linear",
        xshow=True,
        ylabel=None,
        ymax=None,
        ymin=None,
        yscale="linear",
        yshow=True,
    ):
    """Convenience function for creating a bar plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.bars`,
    :meth:`toyplot.canvas.Canvas.cartesian`, and :class:`toyplot.canvas.Canvas` for
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
        label=label,
        margin=margin,
        padding=padding,
        show=show,
        xlabel=xlabel,
        xmax=xmax,
        xmin=xmin,
        xscale=xscale,
        xshow=xshow,
        ylabel=ylabel,
        ymax=ymax,
        ymin=ymin,
        yscale=yscale,
        yshow=yshow,
        )

    mark = axes.bars(
        a=a,
        b=b,
        c=c,
        along=along,
        baseline=baseline,
        color=color,
        filename=filename,
        hyperlink=hyperlink,
        opacity=opacity,
        style=style,
        title=title,
        )
    return canvas, axes, mark


def fill(
        a,
        b=None,
        c=None,
        along="x",
        baseline=None,
        color=None,
        filename=None,
        height=None,
        label=None,
        margin=50,
        opacity=1.0,
        padding=10,
        show=True,
        style=None,
        title=None,
        width=None,
        xlabel=None,
        xmax=None,
        xmin=None,
        xscale="linear",
        xshow=True,
        ylabel=None,
        ymax=None,
        ymin=None,
        yscale="linear",
        yshow=True,
    ):
    """Convenience function for creating a fill plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.fill`,
    :meth:`toyplot.canvas.Canvas.cartesian`, and :class:`toyplot.canvas.Canvas` for
    parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
      A new canvas object.
    axes: :class:`toyplot.coordinates.Cartesian`
      A new set of 2D axes that fill the canvas.
    mark: :class:`toyplot.mark.FillBoundaries` or :class:`toyplot.mark.FillMagnitudes`
      The new fill mark.
    """
    canvas = Canvas(
        height=height,
        width=width,
        )
    axes = canvas.cartesian(
        label=label,
        margin=margin,
        padding=padding,
        show=show,
        xlabel=xlabel,
        xmax=xmax,
        xmin=xmin,
        xscale=xscale,
        xshow=xshow,
        ylabel=ylabel,
        ymax=ymax,
        ymin=ymin,
        yscale=yscale,
        yshow=yshow,
        )
    mark = axes.fill(
        a=a,
        b=b,
        c=c,
        along=along,
        baseline=baseline,
        color=color,
        filename=filename,
        opacity=opacity,
        style=style,
        title=title,
        )
    return canvas, axes, mark


def graph(
        a,
        b=None,
        c=None,
        along="x",
        ecolor=None,
        eopacity=1.0,
        estyle=None,
        ewidth=1.0,
        height=None,
        hmarker=None,
        layout=None,
        margin=50,
        mmarker=None,
        mposition=0.5,
        olayout=None,
        padding=20,
        tmarker=None,
        varea=None,
        vcolor=None,
        vcoordinates=None,
        vlabel=None,
        vlshow=True,
        vlstyle=None,
        vmarker="o",
        vopacity=1.0,
        vsize=None,
        vstyle=None,
        vtitle=None,
        width=None,
    ): # pragma: no cover
    """Convenience function for creating a graph plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.graph`,
    :meth:`toyplot.canvas.Canvas.cartesian`, and :class:`toyplot.canvas.Canvas` for
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
    canvas = Canvas(
        height=height,
        width=width,
        )
    axes = canvas.cartesian(
        aspect="fit-range",
        margin=margin,
        padding=padding,
        show=False,
        )
    mark = axes.graph(
        a=a,
        b=b,
        c=c,
        along=along,
        ecolor=ecolor,
        eopacity=eopacity,
        estyle=estyle,
        ewidth=ewidth,
        hmarker=hmarker,
        layout=layout,
        mmarker=mmarker,
        mposition=mposition,
        olayout=olayout,
        tmarker=tmarker,
        varea=varea,
        vcolor=vcolor,
        vcoordinates=vcoordinates,
        vlabel=vlabel,
        vlshow=vlshow,
        vlstyle=vlstyle,
        vmarker=vmarker,
        vopacity=vopacity,
        vsize=vsize,
        vstyle=vstyle,
        vtitle=vtitle,
        )
    return canvas, axes, mark


def image(
        data,
        height=None,
        margin=0,
        width=None,
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
    canvas = Canvas(
        height=height,
        width=width,
        )
    mark = canvas.image(
        data=data,
        margin=margin,
        )
    return canvas, mark


def matrix(
        data,
        blabel=None,
        blocator=None,
        bshow=None,
        colorshow=False,
        filename=None,
        height=None,
        label=None,
        llabel=None,
        llocator=None,
        lshow=None,
        margin=50,
        rlabel=None,
        rlocator=None,
        rshow=None,
        step=1,
        tlabel=None,
        tlocator=None,
        tshow=None,
        width=None,
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
    canvas = Canvas(
        height=height,
        width=width,
        )
    axes = canvas.matrix(
        blabel=blabel,
        blocator=blocator,
        bshow=bshow,
        colorshow=colorshow,
        data=data,
        filename=filename,
        label=label,
        llabel=llabel,
        llocator=llocator,
        lshow=lshow,
        margin=margin,
        rlabel=rlabel,
        rlocator=rlocator,
        rshow=rshow,
        step=step,
        tlabel=tlabel,
        tlocator=tlocator,
        tshow=tshow,
        )
    return canvas, axes


def plot(
        a,
        b=None,
        along="x",
        area=None,
        aspect=None,
        color=None,
        filename=None,
        height=None,
        label=None,
        margin=50,
        marker=None,
        mfill=None,
        mlstyle=None,
        mopacity=1.0,
        mstyle=None,
        mtitle=None,
        opacity=1.0,
        padding=10,
        show=True,
        size=None,
        stroke_width=2.0,
        style=None,
        title=None,
        width=None,
        xlabel=None,
        xmax=None,
        xmin=None,
        xscale="linear",
        xshow=True,
        ylabel=None,
        ymax=None,
        ymin=None,
        yscale="linear",
        yshow=True,
    ):
    """Convenience function for creating a line plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.plot`,
    :meth:`toyplot.canvas.Canvas.cartesian`, and :class:`toyplot.canvas.Canvas` for
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
    canvas = Canvas(
        height=height,
        width=width,
        )
    axes = canvas.cartesian(
        aspect=aspect,
        label=label,
        margin=margin,
        padding=padding,
        show=show,
        xlabel=xlabel,
        xmax=xmax,
        xmin=xmin,
        xscale=xscale,
        xshow=xshow,
        ylabel=ylabel,
        ymax=ymax,
        ymin=ymin,
        yscale=yscale,
        yshow=yshow,
        )
    mark = axes.plot(
        a=a,
        b=b,
        along=along,
        area=area,
        color=color,
        filename=filename,
        marker=marker,
        mfill=mfill,
        mlstyle=mlstyle,
        mopacity=mopacity,
        mstyle=mstyle,
        mtitle=mtitle,
        opacity=opacity,
        size=size,
        stroke_width=stroke_width,
        style=style,
        title=title,
        )
    return canvas, axes, mark


def scatterplot(
        a,
        b=None,
        along="x",
        area=None,
        aspect=None,
        color=None,
        filename=None,
        height=None,
        hyperlink=None,
        label=None,
        margin=50,
        marker="o",
        mlstyle=None,
        mstyle=None,
        opacity=1.0,
        padding=10,
        show=True,
        size=None,
        title=None,
        width=None,
        xlabel=None,
        xmax=None,
        xmin=None,
        xscale="linear",
        xshow=True,
        ylabel=None,
        ymax=None,
        ymin=None,
        yscale="linear",
        yshow=True,
    ):
    """Convenience function for creating a scatter plot in a single call.

    See :meth:`toyplot.coordinates.Cartesian.scatterplot`,
    :meth:`toyplot.canvas.Canvas.cartesian`, and :class:`toyplot.canvas.Canvas` for
    parameter descriptions.

    Returns
    -------
    canvas: :class:`toyplot.canvas.Canvas`
      A new canvas object.
    axes: :class:`toyplot.coordinates.Cartesian`
      A new set of 2D axes that fill the canvas.
    mark: :class:`toyplot.mark.Point`
      The new scatterplot mark.
    """
    canvas = Canvas(
        height=height,
        width=width,
        )
    axes = canvas.cartesian(
        aspect=aspect,
        label=label,
        margin=margin,
        padding=padding,
        show=show,
        xlabel=xlabel,
        xmax=xmax,
        xmin=xmin,
        xscale=xscale,
        xshow=xshow,
        ylabel=ylabel,
        ymax=ymax,
        ymin=ymin,
        yscale=yscale,
        yshow=yshow,
        )
    mark = axes.scatterplot(
        a=a,
        b=b,
        along=along,
        area=area,
        color=color,
        filename=filename,
        hyperlink=hyperlink,
        marker=marker,
        mlstyle=mlstyle,
        mstyle=mstyle,
        opacity=opacity,
        size=size,
        title=title,
        )
    return canvas, axes, mark


def table(
        data=None,
        brows=None,
        columns=None,
        filename=None,
        height=None,
        label=None,
        lcolumns=None,
        margin=50,
        rcolumns=None,
        rows=None,
        trows=None,
        width=None,
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
    canvas = Canvas(
        height=height,
        width=width,
        )
    axes = canvas.table(
        brows=brows,
        columns=columns,
        data=data,
        filename=filename,
        label=label,
        lcolumns=lcolumns,
        margin=margin,
        rcolumns=rcolumns,
        rows=rows,
        trows=trows,
        )
    return canvas, axes
