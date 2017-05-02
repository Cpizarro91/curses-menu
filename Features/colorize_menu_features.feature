#Cassandra Pizarro

Feature: Coloring of text on menu
In order to make text more visible
As a user
I want to be able to colorize text on my menus

    Scenario: Visually seeing colors of text on menu for one item
      Given that colors are enabled on your terminal
      When you create one menu item with a specific color
      And your menu appears in your terminal
      Then you should see the text in the color that you chose

    Scenario: Visually seeing colors of text on menu for entire menu
      Given that colors are enabled on your terminal shell
      When you create each individual menu item with specific colors
      And your menu appears in your terminal shell
      Then you should see each menu item text in the colors that you chose
