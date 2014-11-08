Feature: Diverging color maps

  Scenario: Diverging color maps
    Given a collection of diverging color maps
    Then each diverging color map can be rendered as ipython html

  Scenario: Default diverging color map
    When the user creates a default diverging color map
    Then the default diverging color map can be rendered as ipython html

  Scenario: Custom diverging color map
    When the user creates a custom diverging color map
    Then the custom diverging color map can be rendered as ipython html

  Scenario: Diverging color map colors
    When the user creates a default diverging color map with domain
    Then individual values can be mapped to colors by the diverging color map

  Scenario: Diverging color map css
    When the user creates a default diverging color map with domain
    Then individual values can be mapped to css colors by the diverging color map
