Feature: Testing command menu item

  Scenario: I want to call a console command from the menu
    Given the command touch hello.txt for the command menu item
    When the accessor method for the command menu item is called
    Then return the command touch hello.txt
