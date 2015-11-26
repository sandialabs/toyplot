Feature: Graph visualization
  Scenario Outline: Render a graph with a layout
    Given a <graph>
    And a <layout> graph layout
    When the graph and layout are combined
    Then the visualization should match the <reference> reference image

    Examples:
      | graph                   | layout                          | reference                        |
      | prufer tree             | default                         | graph-prufer-tree-default-layout |
      | prufer tree             | random                          | graph-prufer-tree-random-layout |
      | prufer tree             | eades                           | graph-prufer-tree-eades-layout |
      | prufer tree             | fruchterman-reingold            | graph-prufer-tree-fruchterman-reingold-layout |
      | prufer tree             | buchheim                        | graph-prufer-tree-buchheim-layout |
#      | prufer tree             | graphviz                        | graph-prufer-tree-graphviz-layout |
      | ba graph                | default                         | graph-ba-graph-default-layout |
      | ba graph                | random                          | graph-ba-graph-random-layout |
      | ba graph                | eades                           | graph-ba-graph-eades-layout |
      | ba graph                | fruchterman-reingold            | graph-ba-graph-fruchterman-reingold-layout |
#      | ba graph                | graphviz                        | graph-ba-graph-graphviz-layout |
      | ba graph                | fruchterman-reingold-curved-edge | graph-ba-graph-fruchterman-reingold-curved-edges-layout |

  Scenario: Explicit graph edges
    When a graph visualization is constructed from explicit source and target edge arrays
    Then the visualization should match the graph-source-target-array reference image
