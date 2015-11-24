Feature: Color scale
  Scenario Outline: Canvas color scales
    Given a default canvas
    And a <colormap>
    Then a <scale> can be added to the canvas

    Examples:
      | colormap                      | scale                                                 |
      | explicit linear color map     | vertical color scale                                  |
      | explicit linear color map     | diagonal color scale                                  |

  Scenario Outline: Canvas color scales
    Given a default canvas
    And a set of default axes
    And a <colormap>
    Then a <scale> can be added to the axes

    Examples:
      | colormap                      | scale                                                 |
      | explicit linear color map     | color scale                                           |

  Scenario Outline: Matrix visualization color scales
    Given a default canvas
    Then a <scale> can be added to a matrix visualization

    Examples:
      | scale                                          |
      | color scale with default colormap              |
      | color scale with explicit colormap             |

