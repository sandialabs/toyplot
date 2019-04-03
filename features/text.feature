Feature: Text
    Scenario Outline: Text alignment
        Given a default canvas
        And a set of cartesian axes
        And text with <phrase>
        Then the figure should match the <reference> reference image

        Examples: Horizontal Alignment
          | phrase                       | reference                          |
          | default alignment            | text-anchor-default                |
          | left alignment               | text-anchor-start                  |
          | center alignment             | text-anchor-middle                 |
          | right alignment              | text-anchor-end                    |
          | positive anchor shift        | text-anchor-shift-positive         |
          | negative anchor shift        | text-anchor-shift-negative         |
          | angled anchor shift          | text-anchor-shift-angled           |

        Examples: Vertical Alignment
          | phrase                            | reference                              |
          | vertical alignment top            | text-vertical-alignment-top            |
          | vertical alignment first baseline | text-vertical-alignment-first-baseline |
          | vertical alignment middle         | text-vertical-alignment-middle         |
          | vertical alignment last baseline  | text-vertical-alignment-last-baseline  |
          | vertical alignment bottom         | text-vertical-alignment-bottom         |
          | positive baseline shift           | text-baseline-shift-positive           |
          | negative baseline shift           | text-baseline-shift-negative           |
          | angled baseline shift             | text-baseline-shift-angled             |

        Examples: Alignment Baseline
          | phrase                       | reference                          |
          | alignment baselines          | text-alignment-baselines           |

    Scenario: Unknown text-anchor value
        Given a default canvas
        And a set of cartesian axes
        When text is aligned with an unknown text-anchor value, an exception is raised.

    Scenario: Unknown alignment-baseline value
        Given a default canvas
        And a set of cartesian axes
        When text is aligned with an unknown alignment-baseline value, an exception is raised.

    Scenario Outline: Custom font family
        Given a default canvas
        And a set of cartesian axes
        And text using font-family <family>
        Then the figure should match the <reference> reference image

        Examples: Fonts
          | family            | reference                          |
          | courier           | text-font-family-courier           |
          | helvetica         | text-font-family-helvetica         |
          | times             | text-font-family-times             |
          | monospace         | text-font-family-monospace         |
          | serif             | text-font-family-serif             |
          | sans-serif        | text-font-family-sans-serif        |

    Scenario: Unknown font family
        Given a default canvas
        And a set of cartesian axes
        When text is drawn with an unknown font family, an exception is raised.

    Scenario Outline: Rich Text
        Given a default canvas
        And a set of cartesian axes
        And rich text <markup>
        Then the figure should match the <reference> reference image

        Examples:
          | markup                                | reference                          |
          | 10<sup>awesome!</sup>                 | text-rich-text-superscript         |
          | H<sub>2</sub>O                        | text-rich-text-subscript           |
          | Hello<br/>World!                      | text-rich-text-line-break          |
          | normal <b>bold</b>                    | text-rich-text-bold                |
          | normal <i>italic</i>                  | text-rich-text-italic              |
          | normal <b><i>bold italic</i></b>      | text-rich-text-bold-italic         |
          | normal <code>code</code>              | text-rich-text-code                |
          | normal <small>small</small>           | text-rich-text-small               |
          | foo <strong>bar<br/>baz</strong> blah | text-rich-text-nested-break        |
          | foo &lt; bar &gt; baz                 | text-rich-text-brackets            |
          | foo &amp; baz                         | text-rich-text-ampersand           |
          | Visit <a href="http://toyplot.readthedocs.io" style="fill:blue">Toyplot</a> for more info! | text-rich-text-hyperlink |
          | Visit <a href="http://toyplot.readthedocs.io" target="_blank" style="fill:blue">Toyplot</a> for more info! | text-rich-text-hyperlink-target |

