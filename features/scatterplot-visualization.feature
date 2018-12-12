Feature: Scatterplot visualization
    Scenario Outline: Scatterplot visualization
        Given a default canvas
        And a set of cartesian axes
        And <scenario>
        Then the figure should match the <reference> reference image

        Examples:
            | scenario              | reference |
            | axes-scatterplot-markers | axes-scatterplot-markers |
            | axes-scatterplot-n-variables-along-y | axes-scatterplot-n-variables-along-y |
            | axes-scatterplot-n-variables-x | axes-scatterplot-n-variables-x |
            | axes-scatterplot-n-variables | axes-scatterplot-n-variables |
            | axes-scatterplot-one-variable-fill | axes-scatterplot-one-variable-fill |
            | axes-scatterplot-one-variable-x | axes-scatterplot-one-variable-x |
            | axes-scatterplot-one-variable | axes-scatterplot-one-variable |
            | axes-scatterplot-singular | axes-scatterplot-singular |
            | scatterplot-one-variable | scatterplot-one-variable |


