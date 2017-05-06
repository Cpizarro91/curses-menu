Feature: Testing root menu

  Scenario: I want to create a root menu
    Given the name RootMenu for the root menu and the name RootMenuSubtitle for the root menu subtitle
    When the accessor method for the root menu name is called
    Then return the root menu name RootMenu