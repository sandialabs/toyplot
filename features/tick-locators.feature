Feature: Tick locators
  Scenario Outline: Tick locators
    Given sample sin wave data
    Then the data can be rendered <phrase>

    Examples:
      | phrase                                       |
      | with default ticks                           |
      | with ticks evenly spread across the domain   |
      | with explicit locations                      |
      | with explicit locations and explicit labels  |
      | with explicit labels                         |
      | with ticks identified by heckbert            |
      | with ticks identified by optimization        |
      | without ticks                                |

