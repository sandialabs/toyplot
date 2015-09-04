Feature: Matrix visualization
    Scenario: Default matrix visualization
        Given a matrix
        Then a default matrix visualization can be created with the convenience API
        And a default matrix visualization can be created with the standard API
