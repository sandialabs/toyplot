Feature: Rectangle visualization
    Scenario Outline: Rectangle visualization
        Given a default canvas
        And a set of cartesian axes
        And <scenario>
        Then the figure should match the <reference> reference image

        Examples:
            | scenario              | reference |
            | axes-rect-singular-along-y | axes-rect-singular-along-y |
            | axes-rect-singular | axes-rect-singular |
            | axes-rect | axes-rect |


