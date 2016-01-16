Feature: Graph visualization
    Scenario Outline: Render a graph
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
            | ba graph                | default                         | graph-ba-graph-default-layout |
            | ba graph                | explicit coordinates            | graph-ba-graph-explicit-coordinates |
            | ba graph                | random                          | graph-ba-graph-random-layout |
            | ba graph                | eades                           | graph-ba-graph-eades-layout |
            | ba graph                | fruchterman-reingold            | graph-ba-graph-fruchterman-reingold-layout |
            | ba graph                | fruchterman-reingold-curved-edge | graph-ba-graph-fruchterman-reingold-curved-edges-layout |

    Scenario Outline: Render a graph from source and target arrays
        Given <graph>
        And a <layout> graph layout
        When the source and target arrays and layout are combined
        Then the visualization should match the <reference> reference image

        Examples:
            | graph                                        | layout                            | reference                        |
            | explicit source and target arrays            | default                           | graph-source-target-array |
            | explicit source and target arrays with loops | fruchterman-reingold              | graph-source-target-array-loop |
            | explicit source and target arrays with loops | fruchterman-reingold-curved-edge  | graph-source-target-array-loop-curved |

    Scenario: Render a graph with disconnected vertices
        Given a ba graph
        And disconnected vertices
        And a fruchterman-reingold graph layout
        When the graph and layout are combined
        Then the visualization should match the graph-ba-graph-disconnected-vertices-fruchterman-reingold-layout reference image

