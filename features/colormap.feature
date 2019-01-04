Feature: Colormap

  Scenario: Linear color map
    Given a linear color map
    Then the linear color map can be rendered as ipython html
    And the linear color map can map scalar values to toyplot colors
    And the linear color map can map scalar values to css colors
    And the color map domain can be changed

  Scenario: Diverging color map
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

  Scenario: Categorical color map
    Given a categorical color map, the map can be rendered as ipython html

  Scenario: Categorial color map colors
    Given a categorical color map, multiple colors can be returned by index

  Scenario: Categorical color map color
    Given a categorical color map, individual colors can be returned by index

  Scenario: Categorical color map css
    Given a categorical color map, individual css colors can be returned by index

    Scenario Outline: Empty domain
        Given a linear color map without a domain
        And colormap values <values>
        When mapping colors without a domain
        Then the color swatches should match the <reference> reference html

        Examples:
            | values              | reference                   |
            | [0, 0, 0]           | colormap-empty-domain-zeros |
            | [1, 1, 1]           | colormap-empty-domain-ones  |


