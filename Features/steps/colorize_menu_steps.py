#Cassandra Pizarro

import curses
from behave import *
from hamcrest import *
from cursesmenu import *
from cursesmenu.items import *
from Features.compare_images import equal

@given("that colors are enabled on your terminal")
def step_impl(context):
    curses.initscr()
    colors_is_on = True
    if not curses.has_colors():
        assert_that(colors_is_on, False)
    else:
        assert_that(colors_is_on, True)

@when('you create one menu item with a specific color')
def step_impl(context):
    menu_item = MenuItem("RED", "Menu Item")
    assert True

@step("your menu appears in your terminal")
def step_impl(context):
    did_menu_fail_to_appear = equal("images/Terminal_beforeMenu.png", "images/Terminal_afterMenu.png")
    assert_that(did_menu_fail_to_appear is False)

@then("you should see the text in the color that you chose")
def step_impl(context):
    are_these_menus_the_same = equal("images/BW_menuItem.png", "images/Colored_menuItem.png")
    assert_that(are_these_menus_the_same is False)

@given("that colors are enabled on your terminal shell")
def step_impl(context):
    #do not initialize menu again here as it's already initialized above
    colors_is_on = True
    if not curses.has_colors():
        assert_that(colors_is_on, False)
    else:
        assert_that(colors_is_on, True)

@when("you create each individual menu item with specific colors")
def step_impl(context):
    menu = CursesMenu("Title", "Subtitle")
    menu_item = MenuItem("RED", "Menu Item" )
    function_item = FunctionItem("BLUE","Call a Python function", input, ["Enter an input"])
    command_item = CommandItem("MAGENTA","Run a console command", "touch hello.txt")
    selection_menu = SelectionMenu(["item", "item2", "item3"])
    submenu_item = SubmenuItem("YELLOW", "Submenu item", selection_menu, menu)
    assert True

@step("your menu appears in your terminal shell")
def step_impl(context):
    did_menu_fail_to_appear = equal("images/Terminal_beforeMenu.png", "images/Terminal_afterMenu.png")
    assert_that(did_menu_fail_to_appear is False)

@then("you should see each menu item text in the colors that you chose")
def step_impl(context):
    are_these_menus_the_same = equal("images/BW_fullMenu.png", "images/Colored_fullMenu.png")
    assert_that(are_these_menus_the_same is False)