Feature: Documentation

    Scenario: Module documentation
        Given all public Toyplot modules
        And the Toyplot reference documentation
        Then every module must have a section in the reference documentation
        And every section in the reference documentation must match a module

    Scenario: Notebook documentation
        Given the Toyplot documentation notebooks
        Then every notebook can be converted to a script
        And every notebook script can be run without error
