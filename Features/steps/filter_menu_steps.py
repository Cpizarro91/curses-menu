#Cassandra Pizarro
from behave import *
from hamcrest import *
from Features.compare_images import equal

@given("I have a menu with a list of menu items")
def step_impl(context):
    did_menu_items_fail_to_appear = equal("images/Terminal_beforeMenu.png", "images/Terminal_afterMenu.png")
    assert_that(did_menu_items_fail_to_appear is False)

@when("I filter the menu by typing in the name of a menu item")
def step_impl(context):
    did_filter_string_fail_to_appear = equal("images/unfiltered_menu.png", "images/filter_string_entered_on_menu.png")
    assert_that(did_filter_string_fail_to_appear is False)

@then('my menu should now only contain that menu item')
def step_impl(context):
    did_menu_fail_to_filter = equal("images/unfiltered_menu.png", "images/filtered_menu.png")
    assert_that(did_menu_fail_to_filter is False)
