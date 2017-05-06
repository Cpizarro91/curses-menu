from behave import *
from hamcrest import *
from cursesmenu import *

@given("the name {root_menu_name} for the root menu and the name {root_menu_subtitle} for the root menu subtitle")
def step_impl(context, root_menu_name, root_menu_subtitle):
    context.root_menu = root_menu_name
    context.root_menu_subtitle = root_menu_subtitle
    context.menu = CursesMenu(context.root_menu, context.root_menu_subtitle)
    pass

@when("the accessor method for the root menu name is called")
def step_impl(context):
    context.accessor = context.menu.get_root_menu_name()
    pass

@then("return the root menu name {root_menu_name}")
def step_impl(context, root_menu_name):
    assert_that(context.accessor, equal_to(root_menu_name))