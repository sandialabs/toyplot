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

    Examples: Vertical Alignment
      | phrase                                                |
      | with hanging alignment                                |
      | with central alignment                                |
      | with middle alignment                                 |
      | with alphabetic alignment                             |
      | with positive baseline shift                          |
      | with negative baseline shift                          |

