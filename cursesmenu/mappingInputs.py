from cursesmenu import *
from cursesmenu.items import *


def dictionaryMenu(menu_data):
    menu_title = menu_data['title']
    mainMenu = CursesMenu(menu_title)

    menu = {}
    menu['1']="ADD a Menu Item."
    menu['2']="DELETE a Menu Item."
    menu['3']="SEARCH for Menu Item"
    menu['4']="EXIT to Main Menu."
    while True:
      options=menu.keys()
      options.sort()
      for entry in options:
          print(entry, menu[entry])

          selection=raw_input("Please Select Option: ")
          if selection == '1':
              newItem = raw_input("Enter Menu Item to ADD: ")
              print("Adding new Menu Item")
              mainMenu.append_item(newItem)
          elif selection == '2':
              delItem = raw_input("Enter Menu Item to DELETE: ")
              print("Deleting Menu Item")
              del mainMenu[delItem]
          elif selection == '3':
              searchItem = raw_input("Enter Menu Item to SEARCH: ")
          elif selection == '4':
              ExitItem()
          else:
              print("Unknown Option Selected.")