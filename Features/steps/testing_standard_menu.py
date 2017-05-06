from behave import *
from hamcrest import *
from cursesmenu import *
from cursesmenu.items import *

@given("the name {menu_item} for the standard menu item")
def step_impl(context, menu_item):
    context.menu = CursesMenu("RootMenu", "RootMenuSubtitle")
    context.menu_item = MenuItem("Red", menu_item, context.menu)
    context.menu.append_item(context.menu_item)
    pass

@when("the accessor method for the standard menu item name is called")
def step_impl(context):
    context.accessor = context.menu.get_items()[0].get_text()
    pass

@then("return the standard menu item name {menu_item}")
def step_impl(context, menu_item):
    assert_that(context.accessor, equal_to(menu_item))