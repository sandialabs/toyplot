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
