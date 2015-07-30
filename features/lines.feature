Feature: Lines
  Scenario: Annotation Lines
    When adding default line marks to axes
    Then the line marks should be treated as annotations.

  Scenario: Data Lines
    When adding data line marks to axes
    Then the line marks should be treated as data.
