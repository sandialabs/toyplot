Feature: Administrivia

    Scenario:
        Given all Toyplot sources.
        Then every source must contain a copyright notice.

    Scenario:
        Given pylint
        Then all pylint tests must pass without any messages.
