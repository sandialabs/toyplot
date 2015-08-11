Feature: Color palettes

  Scenario: Default color palette
    Given a default color palette
    Then the palette should contain 8 colors
    And the default palette can be rendered as ipython html

  Scenario: Reversed color palette
    Given a reversed default color palette
    Then the reversed palette can be rendered as ipython html

  Scenario: Color Brewer palettes
    Given a collection of Color Brewer palettes
    Then each palette can be rendered as ipython html

  Scenario: Unsized Color Brewer palette
    When the user creates a Color Brewer palette
    Then the Color Brewer palette should have the maximum number of colors

  Scenario: Sized Color Brewer palette
    When the user creates a sized Color Brewer palette
    Then the Color Brewer palette should have the requested number of colors

  Scenario: Reversed Color Brewer palette
    When the user creates a reversed Color Brewer palette
    Then the Color Brewer palette should have its colors reversed

  Scenario: Lighten color palettes
    Given a starting color
    Then the color can be used to generate a palette of lighter shades

  Scenario: Concatenate color palettes
    Given two color palettes
    Then the color palettes can be concatenated into a single palette

  Scenario: Incrementally grow color palettes
    Given a color palette
    Then another palette can be appended

  Scenario: Color palette CSS names
    Given a collection of CSS color names, a color palette can be created

  Scenario: Color palette getitem
    Given a color palette, colors can be retrieved using item notation

  Scenario: Color palette iteration
    Given a color palette, callers can iterate over the colors

  Scenario: Color palette color retrieval
    Given a color palette, callers can retrieve colors by index

  Scenario: Color palette css color retrieval
    Given a color palette, colors can retrieve css colors by index

