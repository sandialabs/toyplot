Feature: Graph visualization
  Scenario Outline: Render a graph with a layout
    Given a <graph>.
    And a <layout> layout.
    Then the rendered graph should match the <reference> reference.

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
      | ba graph                | fruchterman-reingold-curved-edges | graph-ba-graph-fruchterman-reingold-curved-edges-layout |

