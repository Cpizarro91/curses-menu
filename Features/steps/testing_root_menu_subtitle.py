from behave import *
from hamcrest import *
from cursesmenu import *

@given("the name {root_menu_subtitle} for the root menu subtitle and the name {root_menu_name} for the root menu")
def step_impl(context, root_menu_subtitle, root_menu_name):
    context.root_menu_name = root_menu_name
    context.root_menu_subtitle = root_menu_subtitle
    context.menu = CursesMenu(context.root_menu_name, context.root_menu_subtitle)
    pass

@when("the accessor method for the root menu subtitle is called")
def step_impl(context):
    context.accessor = context.menu.get_root_menu_subtitle()
    pass

@then("return the root menu subtitle {root_menu_subtitle}")
def step_impl(context, root_menu_subtitle):
    assert_that(context.accessor, equal_to(root_menu_subtitle))