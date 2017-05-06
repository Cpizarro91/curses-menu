from behave import *
from hamcrest import *
from cursesmenu import *
from cursesmenu.items import *
from time import *

@given("the input function for the function menu item")
def step_impl(context):
    context.menu = CursesMenu("RootMenu", "RootMenuSubtitle")
    context.function_item = FunctionItem("Blue", "Call a Python function", input, ["Enter an input"])
    context.menu.append_item(context.function_item)
    pass

@when("the accessor method for the function menu item is called")
def step_impl(context):
    context.accessor = context.menu.get_items()[0].get_function()
    pass

@then("return the input function")
def step_impl(context):
    assert_that(context.accessor, equal_to(input))
