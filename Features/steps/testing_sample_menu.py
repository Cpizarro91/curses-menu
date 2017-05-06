from PIL import ImageChops
from PIL import Image
from PIL import ImageGrab
from behave import *
from hamcrest import *
from cursesmenu import *
from cursesmenu.items import *
import time

@given("a sample menu with sample menu items")
def step_impl(context):
    context.menu = CursesMenu("Title", "Subtitle")
    menu_item = MenuItem("Red", "Menu Item" )
    function_item = FunctionItem("Blue", "Call a Python function", input, ["Enter an input"])
    command_item = CommandItem("Magenta", "Run a console command", "touch hello.txt")
    selection_menu = SelectionMenu(["item1", "item2", "item3"])
    submenu_item = SubmenuItem("Yellow", "Submenu item", selection_menu, context.menu)
    context.menu.append_item(menu_item)
    context.menu.append_item(function_item)
    context.menu.append_item(command_item)
    context.menu.append_item(submenu_item)
    pass

@when("the sample menu is displayed")
def step_impl(context):
    context.menu.show()
    context.menu.draw()
    time.sleep(1)
    snapshot = ImageGrab.grab([0, 0, 400, 400])
    save_path = "C:\\Users\\Danny\\PyCharmProjects\\DANNY-curses-menu\\images\\MenuScreen.jpg"
    snapshot.save(save_path)
    pass

@then("it looks identical to a stored image of the sample menu")
def step_impl(context):
    im1 = Image.open("images/MenuScreen.jpg")
    im2 = Image.open("images/CompareTo.jpg")
    assert_that(ImageChops.difference(im1, im2).getbbox() is None)