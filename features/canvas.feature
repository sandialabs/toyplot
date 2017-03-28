Feature: Canvas
    Scenario Outline: Canvas layouts
        Given a canvas with a border
        Then axes can be added to the canvas using <layout>.
        And the visualization should match the <reference> reference image

        Examples:
            | layout                | reference |
            | the default layout    | canvas-layout-default |
            | explicit bounds       | canvas-layout-bounds |
            | grid layout           | canvas-layout-grid |
            | corner layout         | canvas-layout-corner |
            | rect layout           | canvas-layout-rect |

    Scenario: Canvas Jupyter HTML
        Given a default canvas
        And a set of cartesian axes
        And a sample plot
        Then the canvas can be rendered in Jupyter as HTML

    Scenario: Canvas Jupyter PNG
        Given a default canvas
        And a set of cartesian axes
        And a sample plot
        Then the canvas can be rendered in Jupyter as a PNG image

    Scenario: Canvas numberline layout
        Given a canvas with a border
        Then numberlines can be added to the canvas using relative coordinates
        And the visualization should match the canvas-layout-numberline-relative reference image
