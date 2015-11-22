Feature: Backends
  Scenario Outline: Render a canvas with a backend
    Given that the <backend> backend is available
    And a sample canvas to be rendered
    Then the canvas can be rendered to <output>

    Examples:
      | backend                  | output                          |
      | toyplot.cairo.eps        | an eps file                     |
      | toyplot.cairo.eps        | an eps buffer                   |
      | toyplot.cairo.eps        | a returned eps document         |
      | toyplot.cairo.pdf        | a pdf file                      |
      | toyplot.cairo.pdf        | a pdf buffer                    |
      | toyplot.cairo.pdf        | a returned pdf document         |
      | toyplot.cairo.png        | a png file                      |
      | toyplot.cairo.png        | a png buffer                    |
      | toyplot.cairo.png        | a returned png document         |
      | toyplot.html             | an html file                    |
      | toyplot.html             | an html buffer                  |
      | toyplot.html             | a returned html dom             |
      | toyplot.pdf              | a pdf file                      |
      | toyplot.pdf              | a pdf buffer                    |
      | toyplot.pdf              | a returned pdf document         |
      | toyplot.png              | a png file                      |
      | toyplot.png              | a png buffer                    |
      | toyplot.png              | a returned png document         |
      | toyplot.qt.pdf           | a pdf file                      |
      | toyplot.qt.pdf           | a pdf buffer                    |
      | toyplot.qt.pdf           | a returned pdf document         |
      | toyplot.qt.png           | a png file                      |
      | toyplot.qt.png           | a png buffer                    |
      | toyplot.qt.png           | a returned png document         |
      | toyplot.reportlab.pdf    | a pdf file                      |
      | toyplot.reportlab.pdf    | a pdf buffer                    |
      | toyplot.reportlab.pdf    | a returned pdf document         |
      | toyplot.svg              | an svg file                     |
      | toyplot.svg              | an svg buffer                   |
      | toyplot.svg              | a returned svg dom              |

