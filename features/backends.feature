Feature: Backends
  Scenario Outline: Render a canvas with a backend
    Given that the <backend> backend is available
    And a sample canvas to be rendered
    Then the canvas can be rendered to <output>

    Examples:
      | backend                  | output                          |
      | toyplot.html             | an html file                    |
      | toyplot.html             | an html buffer                  |
      | toyplot.html             | a returned html dom             |
      | toyplot.pdf              | a pdf file                      |
      | toyplot.pdf              | a pdf buffer                    |
      | toyplot.pdf              | a returned pdf document         |
      | toyplot.png              | a png file                      |
      | toyplot.png              | a png buffer                    |
      | toyplot.png              | a returned png document         |
      | toyplot.reportlab.pdf    | a pdf file                      |
      | toyplot.reportlab.pdf    | a pdf buffer                    |
      | toyplot.reportlab.pdf    | a returned pdf document         |
      | toyplot.reportlab.png    | a png file                      |
      | toyplot.reportlab.png    | a png buffer                    |
      | toyplot.reportlab.png    | a returned png document         |
      | toyplot.svg              | an svg file                     |
      | toyplot.svg              | an svg buffer                   |
      | toyplot.svg              | a returned svg dom              |

