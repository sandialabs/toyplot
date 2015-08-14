Feature: Text alignment
    Scenario Outline: Text alignment
        Given a set of cartesian axes
        Then text can be aligned <phrase>

        Examples: Horizontal Alignment
          | phrase                                                |
          | with default alignment                                |
          | with left alignment                                   |
          | with center alignment                                 |
          | with right alignment                                  |
          | with positive anchor shift                            |
          | with negative anchor shift                            |

        Examples: Vertical Alignment
          | phrase                                                |
          | with hanging alignment                                |
          | with central alignment                                |
          | with middle alignment                                 |
          | with alphabetic alignment                             |
          | with positive baseline shift                          |
          | with negative baseline shift                          |

    Scenario: Unknown text-anchor value
        Given a set of cartesian axes
        When text is aligned with an unknown text-anchor value, an exception is raised.

    Scenario: Unknown alignment-baseline value
        Given a set of cartesian axes
        When text is aligned with an unknown alignment-baseline value, an exception is raised.
