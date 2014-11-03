Feature: Color broadcasting

  Scenario: Broadcast one color
    When broadcasting one color to a 2d array
    Then toyplot.color.broadcast should broadcast the value to the 2d array

  Scenario: Broadcast a list of colors
    When broadcasting a list of colors to a 1d array
    Then toyplot.color.broadcast should broadcast the list to the 1d array

  Scenario: Broadcast a list of colors
    When broadcasting a list of colors to a 2d array
    Then toyplot.color.broadcast should broadcast the list to the 2d array

  Scenario: Broadcast a 1d array of css colors
    When broadcasting a 1d array of css colors to a 1d array
    Then toyplot.color.broadcast should broadcast the 1d array of colors to the 1d array

  Scenario: Broadcast a 1d array of css colors
    When broadcasting a 1d array of css colors to a 2d array
    Then toyplot.color.broadcast should broadcast the 1d array of colors to the 2d array
