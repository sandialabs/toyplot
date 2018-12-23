Feature: Ellipse visualization
    Scenario Outline: Ellipse visualization
        Given a default canvas
        And a set of cartesian axes
        And <scenario>
        Then the figure should match the <reference> reference image

        Examples:
            | scenario      | reference |
            | a basic ellipse | ellipse-basic |
            | a rotated ellipse | ellipse-rotated |
            | an ellipse with log y axis | ellipse-log-y-axis |
            | an ellipse with a title | ellipse-title |
            | an ellipse with a custom color | ellipse-custom-color |
            | an ellipse with a custom opacity | ellipse-custom-opacity |
            | an ellipse with a custom style | ellipse-custom-style |
            | multiple ellipses | ellipse-multiple |


