Feature: Text
    Scenario Outline: Text alignment
        Given a set of cartesian axes
        And text with <phrase>
        Then the generated figure will match <reference>

        Examples: Horizontal Alignment
          | phrase                       | reference                          |
          | default alignment            | text-anchor-default                |
          | left alignment               | text-anchor-start                  |
          | center alignment             | text-anchor-middle                 |
          | right alignment              | text-anchor-end                    |
          | positive anchor shift        | text-anchor-shift-positive         |
          | negative anchor shift        | text-anchor-shift-negative         |

        Examples: Vertical Alignment
          | phrase                       | reference                          |
          | hanging alignment            | text-alignment-baseline-hanging    |
          | central alignment            | text-alignment-baseline-central    |
          | middle alignment             | text-alignment-baseline-middle     |
          | alphabetic alignment         | text-alignment-baseline-alphabetic |
          | positive baseline shift      | text-baseline-shift-positive       |
          | negative baseline shift      | text-baseline-shift-negative       |

    Scenario: Unknown text-anchor value
        Given a set of cartesian axes
        When text is aligned with an unknown text-anchor value, an exception is raised.

    Scenario: Unknown alignment-baseline value
        Given a set of cartesian axes
        When text is aligned with an unknown alignment-baseline value, an exception is raised.

    Scenario Outline: Rich Text
        Given a set of cartesian axes
        And rich text <markup>
        Then the generated figure will match <reference>

        Examples:
          | markup                                | reference                          |
          | 10<sup>awesome!</sup>                 | text-rich-text-superscript         |
          | H<sub>2</sub>O                        | text-rich-text-subscript           |
          | Hello<br>World!                       | text-rich-text-line-break          |
          | normal <b>bold</b>                    | text-rich-text-bold                |
          | normal <i>italic</i>                  | text-rich-text-italic              |
          | normal <b><i>bold italic</i></b>      | text-rich-text-bold-italic         |
          | normal <code>code</code>              | text-rich-text-code                |
          | normal <small>small</small>           | text-rich-text-small               |
          | foo <strong>bar<br>baz</strong> blah  | text-rich-text-nested-break        |

