Feature: Plot visualization
    Scenario Outline: Plot visualization
        Given a default canvas
        And a set of cartesian axes
        And <scenario>
        Then the figure should match the <reference> reference image

        Examples:
            | scenario              | reference |
            | axes-plot-masked-nan | axes-plot-masked-nan |
            | axes-plot-n-variables-along-y | axes-plot-n-variables-along-y |
            | axes-plot-n-variables-x | axes-plot-n-variables-x |
            | axes-plot-n-variables | axes-plot-n-variables |
            | axes-plot-one-variable-x | axes-plot-one-variable-x |
            | axes-plot-one-variable | axes-plot-one-variable |


