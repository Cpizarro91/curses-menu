Feature: Testing root menu subtitle

  Scenario: I want to create a root menu subtitle
    Given the name RootMenuSubtitle for the root menu subtitle and the name RootMenu for the root menu
    When the accessor method for the root menu subtitle is called
    Then return the root menu subtitle RootMenuSubtitle