Feature: Testing standard menu item

  Scenario: I want to create a standard menu item
    Given the name MenuItem for the standard menu item
    When the accessor method for the standard menu item name is called
    Then return the standard menu item name MenuItem