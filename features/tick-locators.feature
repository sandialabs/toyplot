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

    Scenario Outline: Timestamp tick locators
        Given <period> of timestamp data
        And a default interval
        And a visualization using the timestamp locator
        Then the figure should match the <reference> reference image

        Examples:
            | period              | reference                        |
            | five years          | tick-locator-timestamp-year      |
            | one year            | tick-locator-timestamp-quarter   |
            | six months          | tick-locator-timestamp-month     |
            | one month           | tick-locator-timestamp-week      |
            | one week            | tick-locator-timestamp-day       |
            | one day             | tick-locator-timestamp-4-hour    |
            | six hours           | tick-locator-timestamp-hour      |
            | two hours           | tick-locator-timestamp-15-minute |
            | one hour            | tick-locator-timestamp-10-minute |
            | thirty minutes      | tick-locator-timestamp-5-minute  |
            | five minutes        | tick-locator-timestamp-minute    |
            | two minutes         | tick-locator-timestamp-15-second |
            | one minute          | tick-locator-timestamp-10-second |
            | thirty seconds      | tick-locator-timestamp-5-second  |
            | five seconds        | tick-locator-timestamp-second    |

    Scenario Outline: Timestamp tick locators with explicit interval
        Given <period> of timestamp data
        And a <count> <units> interval
        And a visualization using the timestamp locator
        Then the figure should match the <reference> reference image

        Examples:
            | period              | count    | units        | reference                                     |
            | seven thousand years| 2        | millenia     | tick-locator-timestamp-two-millenium-interval |
            | one thousand years  | 2        | centuries    | tick-locator-timestamp-two-century-interval   |
            | one hundred years   | 2        | decades      | tick-locator-timestamp-two-decade-interval    |
            | five years          | 2        | years        | tick-locator-timestamp-two-year-interval      |
            | one year            | 2        | quarters     | tick-locator-timestamp-two-quarter-interval   |
            | six months          | 2        | months       | tick-locator-timestamp-two-month-interval     |
            | one month           | 2        | weeks        | tick-locator-timestamp-two-week-interval      |
            | one week            | 2        | days         | tick-locator-timestamp-two-day-interval       |
            | one day             | 3        | hours        | tick-locator-timestamp-three-hour-interval    |
            | one hour            | 12       | minutes      | tick-locator-timestamp-twelve-minute-interval |
            | one minute          | 12       | seconds      | tick-locator-timestamp-twelve-second-interval |

    Scenario Outline: Timestamp tick locators with string interval
        Given <period> of timestamp data
        And an interval of <interval>
        And a visualization using the timestamp locator
        Then the figure should match the <reference> reference image

        Examples:
            | period              | interval     | reference                                  |
            | one week            | days         | tick-locator-timestamp-days-interval       |

