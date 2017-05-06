Feature: Testing sample menu

  Scenario: I want to make sure a sample menu is properly displayed and is identical every time
    Given a sample menu with sample menu items
    When the sample menu is displayed
    Then it looks identical to a stored image of the sample menu

