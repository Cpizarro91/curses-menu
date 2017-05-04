from behave import given, when, then
from cursesmenu import *
from cursesmenu.items import MultiItem


@given("a multi-selection menu with three items")
def step_impl(context):
    context.menu = MultiMenu(["Item", "Thing", "Other thing"])
    context.menu.show()
    pass


@when("the first item is chosen")
def step_impl(context):
    context.menu.items[0].choose_selection()
    pass


@then("the first item is selected")
def step_impl(context):
    assert context.menu.items[0].choice_selected()

@given("a multi-selection menu with two items")
def step_impl(context):
    context.menu = MultiMenu(["Item", "Thing"])
    context.menu.show()
    pass

@when("the first and second items are chosen")
def step_impl(context):
    context.menu.items[0].choose_selection()
    context.menu.items[1].choose_selection()
    pass


@then("the first and second items are selected")
def step_impl(context):
    assert context.menu.items[0].choice_selected()
    assert context.menu.items[1].choice_selected()
    pass


@given("a multi-selection menu with two out of three items selected")
def step_impl(context):
    context.menu = MultiMenu(["Item", "Thing"])
    context.menu.show()
    context.menu.items[0].choose_selection()
    context.menu.items[1].choose_selection()
    pass


@when("one of the items are chosen again")
def step_impl(context):
    context.menu.items[1].choose_selection()
    pass


@then("the chosen item is no longer selected")
def step_impl(context):
    assert not context.menu.items[1].choice_selected()


