Feature: ReportLab renderer
  Scenario: SVG cubic path commands are translated to ReportLab path calls
    Given an SVG path with move, line, cubic, and close commands
    When the SVG path is rendered with the ReportLab backend
    Then the ReportLab path should receive the expected drawing commands
