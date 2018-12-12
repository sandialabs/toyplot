Feature: Legacy Tests
    Scenario Outline: Legacy tests
        Given <scenario>
        Then the visualization should match the <reference> reference image

        Examples:
            | scenario              | reference |
            | axes-bars-boundaries-masked-nan | axes-bars-boundaries-masked-nan |
            | axes-bars-histogram | axes-bars-histogram |
            | axes-bars-magnitudes-masked-nan | axes-bars-magnitudes-masked-nan |
            | axes-bars-n-boundaries-along-y | axes-bars-n-boundaries-along-y |
            | axes-bars-n-boundaries-centers | axes-bars-n-boundaries-centers |
            | axes-bars-n-boundaries-edges | axes-bars-n-boundaries-edges |
            | axes-bars-n-boundaries-titles | axes-bars-n-boundaries-titles |
            | axes-bars-n-boundaries | axes-bars-n-boundaries |
            | axes-bars-n-magnitudes-along-y | axes-bars-n-magnitudes-along-y |
            | axes-bars-n-magnitudes-centers | axes-bars-n-magnitudes-centers |
            | axes-bars-n-magnitudes-edges | axes-bars-n-magnitudes-edges |
            | axes-bars-n-magnitudes-symmetric | axes-bars-n-magnitudes-symmetric |
            | axes-bars-n-magnitudes-titles | axes-bars-n-magnitudes-titles |
            | axes-bars-n-magnitudes-wiggle | axes-bars-n-magnitudes-wiggle |
            | axes-bars-n-magnitudes | axes-bars-n-magnitudes |
            | axes-bars-one-boundary-centers | axes-bars-one-boundary-centers |
            | axes-bars-one-boundary-edges | axes-bars-one-boundary-edges |
            | axes-bars-one-boundary | axes-bars-one-boundary |
            | axes-bars-one-magnitude-centers | axes-bars-one-magnitude-centers |
            | axes-bars-one-magnitude-edges | axes-bars-one-magnitude-edges |
            | axes-bars-one-magnitude | axes-bars-one-magnitude |
            | axes-fill-boundaries-masked-nan | axes-fill-boundaries-masked-nan |
            | axes-fill-magnitudes-masked-nan | axes-fill-magnitudes-masked-nan |
            | axes-palette | axes-palette |
            | axes-palettes | axes-palettes |
            | axes-plot-masked-nan | axes-plot-masked-nan |
            | axes-plot-n-variables-along-y | axes-plot-n-variables-along-y |
            | axes-plot-n-variables-x | axes-plot-n-variables-x |
            | axes-plot-n-variables | axes-plot-n-variables |
            | axes-plot-one-variable-x | axes-plot-one-variable-x |
            | axes-plot-one-variable | axes-plot-one-variable |
            | axes-rect-singular-along-y | axes-rect-singular-along-y |
            | axes-rect-singular | axes-rect-singular |
            | axes-rect | axes-rect |
            | axes-scatterplot-markers | axes-scatterplot-markers |
            | axes-scatterplot-n-variables-along-y | axes-scatterplot-n-variables-along-y |
            | axes-scatterplot-n-variables-x | axes-scatterplot-n-variables-x |
            | axes-scatterplot-n-variables | axes-scatterplot-n-variables |
            | axes-scatterplot-one-variable-fill | axes-scatterplot-one-variable-fill |
            | axes-scatterplot-one-variable-x | axes-scatterplot-one-variable-x |
            | axes-scatterplot-one-variable | axes-scatterplot-one-variable |
            | axes-scatterplot-singular | axes-scatterplot-singular |
            | axes-tick-titles | axes-tick-titles |
            | bars-one-magnitude | bars-one-magnitude |
            | scatterplot-one-variable | scatterplot-one-variable |


    Scenario: Animation frame
        When an animation frame is created, its fields are populated.

    Scenario: Canvas frame
        When a canvas is used to create an animation frame, its fields are populated.
