#Cassandra Pizarro

Feature: Filter menu items
In order to find menu items easier
As a user
I want to be able to type in a key word
And have the menu show only that specific item

    Scenario:
      Given I have a menu with a list of menu items
      When I filter the menu by typing in the name of a menu item
      Then my menu should now only contain that menu item

