Feature: Color scale
  Scenario Outline: Canvas color scales
    Given a default canvas
    And a <colormap>
    Then a <scale> can be added to the canvas
    And the visualization should match the <reference> reference image

    Examples:
      | colormap            | scale                | reference |
      | linear colormap     | vertical color scale | color-scale-canvas-vertical |
      | linear colormap     | diagonal color scale | color-scale-canvas-diagonal |

  Scenario Outline: Canvas color scales
    Given a default canvas
    And a set of default axes
    And a <colormap>
    Then a <scale> can be added to the axes
    And the visualization should match the <reference> reference image

    Examples:
      | colormap                 | scale          | reference |
      | linear colormap          | color scale    | color-scale-axes-linear-colormap      |
      | categorical colormap     | color scale    | color-scale-axes-categorical-colormap |

  Scenario Outline: Matrix visualization color scales
    Given a default canvas
    Then a <scale> can be added to a matrix visualization
    And the visualization should match the <reference> reference image

    Examples:
      | scale                               | reference |
      | color scale with default colormap   | color-scale-matrix-default-colormap |
      | color scale with linear colormap    | color-scale-matrix-linear-colormap  |

