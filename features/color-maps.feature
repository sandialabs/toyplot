Feature: Color maps

  Scenario: Linear color maps
    Given a linear color map
    Then the linear color map can be rendered as ipython html
    And the linear color map can map scalar values to toyplot colors
    And the linear color map can map scalar values to css colors

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

  Scenario: Categorical color maps
    Given a categorical color map, the map can be rendered as ipython html

  Scenario: Categorial color map colors
    Given a categorical color map, multiple colors can be returned by index

  Scenario: Categorical color map color
    Given a categorical color map, individual colors can be returned by index

  Scenario: Categorical color map css
    Given a categorical color map, individual css colors can be returned by index
