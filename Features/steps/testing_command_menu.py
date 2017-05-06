from behave import *
from hamcrest import *
from cursesmenu import *
from cursesmenu.items import *

@given("the command {command} for the command menu item")
def step_impl(context, command):
    context.menu = CursesMenu("RootMenu", "RootMenuSubtitle")
    context.command_item = CommandItem("Magenta", "Run a console command", "touch hello.txt")
    context.menu.append_item(context.command_item)
    pass

@when("the accessor method for the command menu item is called")
def step_impl(context):
    context.accessor = context.menu.get_items()[0].get_command()
    pass

@then("return the command {command}")
def step_impl(context, command):
    assert_that(context.accessor, equal_to(command))