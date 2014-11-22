Feature: Color palettes

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
