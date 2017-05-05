Feature: Mapping User Inputs Using a Dictionary
    When I access the selection menu 
    I want to be able to add, delete, and search for items or return to main menu

  Scenario: Adding a menu item
    Given a menu system
    When the user selects the numerical option for ADD <integer>
    Then the user will be able to ADD their menu option

  Scenario: Deleting a menu item
    Given a menu system
    When the user selects the numerical option for DELETE <integer>
    Then the user will be able to DELETE the menu item

  Scenario: Search for menu item
    Given a menu system
    When the user selects the numerical option for SEARCH <integer>
    Then the user will be able to SEARCH for their menu item

  Scenario: Exiting menu
    Given a menu system
    When the user selects the numerical option for EXIT <integer>
    Then the user will be able to EXIT and return to MAIN MENU
