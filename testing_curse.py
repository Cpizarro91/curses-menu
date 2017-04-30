# Import the necessary packages
from cursesmenu import *
from cursesmenu.items import *

names2 = []
# Create the menu
menu = CursesMenu("Title", "Subtitle")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("RED", "Menu Item" )

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("BLUE","Call a Python function", input, ["Enter an input"])

# A CommandItem runs a console command
command_item = CommandItem("MAGENTA","Run a console command", "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("YELLOW" ,"Submenu item", selection_menu, menu)

# A MultiMenu constructs a menu from a list of strings
multi_menu = MultiMenu(["Item 1", "Item 2", "Item 3"])

# A SubmenuItem used to create a menu within a menu using MultiMenu
submenu_item2 = SubmenuItem("GREEN","Submenu Item 2", multi_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)
menu.append_item(submenu_item2)


# Finally, we call show to show the menu and allow the user to interact
menu.show()