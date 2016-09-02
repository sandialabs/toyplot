Feature: Documentation

    Scenario: Module documentation
        Given all public Toyplot modules
        And the Toyplot reference documentation
        Then every module must have a section in the reference documentation
        And every section in the reference documentation must match a module

    Scenario: Colormap luma plots
        Given a collection of linear color maps
        Then the color maps can be rendered as luma plots
        And the visualization should match the linear-luma-plots reference image
