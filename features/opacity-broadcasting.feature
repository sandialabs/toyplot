Feature: Opacity Broadcasting
    Scenario Outline: Opacity broadcasting use-cases
        Given a default canvas
        And a set of cartesian axes
        And a set of diverging series
        And a set of per-series opacity values
        And a set of per-datum opacity values
        Then <mark> can be rendered with <opacity>
        And the figure should match the <reference> reference image

        Examples:
            | mark           | opacity               | reference                                           |
            | bars           | one explicit opacity  | opacity-broadcast-bars-one-opacity                  |
            | bars           | per-series opacities  | opacity-broadcast-bars-per-series-opacities         |
            | bars           | per-datum opacities   | opacity-broadcast-bars-per-datum-opacities          |
            | fills          | one explicit opacity  | opacity-broadcast-fills-one-opacity                 |
            | fills          | per-series opacities  | opacity-broadcast-fills-per-series-opacities        |
            | hlines         | one explicit opacity  | opacity-broadcast-hlines-one-opacity                |
            | hlines         | per-datum opacities   | opacity-broadcast-hlines-per-datum-opacities        |
            | plots          | one explicit opacity  | opacity-broadcast-plots-one-opacity                 |
            | plots          | per-series opacities  | opacity-broadcast-plots-per-series-opacities        |
            | rects          | one explicit opacity  | opacity-broadcast-rects-one-opacity                 |
            | rects          | per-datum opacities   | opacity-broadcast-rects-per-datum-opacities         |
            | scatterplots   | one explicit opacity  | opacity-broadcast-scatterplots-one-opacity          |
            | scatterplots   | per-series opacities  | opacity-broadcast-scatterplots-per-series-opacities |
            | scatterplots   | per-datum opacities   | opacity-broadcast-scatterplots-per-datum-opacities  |
            | text           | one explicit opacity  | opacity-broadcast-text-one-opacity                  |
            | text           | per-datum opacities   | opacity-broadcast-text-per-datum-opacities          |
            | vlines         | one explicit opacity  | opacity-broadcast-vlines-one-opacity                |
            | vlines         | per-datum opacities   | opacity-broadcast-vlines-per-datum-opacities        |

    Scenario: Per-datum opacity broadcasting with one series
        Given a default canvas
        And a set of cartesian axes
        Then bars can be rendered with a single series and per-datum opacities
        And the figure should match the opacity-broadcast-bars-single-series-per-datum-opacities reference image

