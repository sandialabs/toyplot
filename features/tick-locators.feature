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

    Scenario Outline: Tick locators
        Given <period> of timestamp data
        And a visualization using the timestamp locator
        Then the generated figure will match <reference>

        Examples:
            | period                                       | reference                        |
            | five years                                   | tick-locator-timestamp-year      |
            | one year                                     | tick-locator-timestamp-quarter   |
            | six months                                   | tick-locator-timestamp-month     |
            | one month                                    | tick-locator-timestamp-week      |
            | one week                                     | tick-locator-timestamp-day       |
            | one day                                      | tick-locator-timestamp-4-hour    |
            | six hours                                    | tick-locator-timestamp-hour      |
            | two hours                                    | tick-locator-timestamp-15-minute |
            | one hour                                     | tick-locator-timestamp-10-minute |
            | thirty minutes                               | tick-locator-timestamp-5-minute  |
            | five minutes                                 | tick-locator-timestamp-minute    |
            | two minutes                                  | tick-locator-timestamp-15-second |
            | one minute                                   | tick-locator-timestamp-10-second |
            | thirty seconds                               | tick-locator-timestamp-5-second  |
            | five seconds                                 | tick-locator-timestamp-second    |

