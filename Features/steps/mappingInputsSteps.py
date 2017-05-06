#from behave import *
#from cursesmenu import*
#from cursesmenu.items import *

# This should be added to environments.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords.new(nil)

#use_step_matcher('re')
#mainMenu = CursesMenu("Title","Subtitle")


#@given(r'a menu system')
#def impl(context):
#    context.total= []
#    context.menu = SelectionMenu("Title", ["1. ADD Item" , "2. DELETE Item", "3. SEARCH for item", "4. EXIT menu"])
#    context.menu.show()
#    pass

#@when(r'the user selects the numerical option for ADD <integer>')
#def impl(context):
#    context.menu.items[0].choose_selection()
#    pass


#@then(r'the user will be able to ADD their menu option')
#def impl(context):
#    assert context.actionwords.the_user_will_be_able_to_add_their_menu_option()
    #Collect USER INPUT for MENU OPTION
    #mainMenu.append_item(context)


#@given(r'a menu system')
#def impl(context):
#    context.actionwords.a_menu_system()
#    pass


#@when(r'the user selects the numerical option for DELETE <integer>')
#def impl(context):
#    context.menu.items[1].choose_selection()
#    pass


#@then(r'the user will be able to DELETE the menu item')
#def impl(context):
#    assert context.actionwords.the_user_will_be_able_to_delete_the_menu_item()

#@given(r'a menu system')
#def impl(context):
#    context.actionwords.a_menu_system()
#    pass

#@when(r'the user selects the numerical option for SEARCH <integer>')
#def impl(context):
#    context.menu.items[2].choose_selection()
#    pass


#@then(r'the user will be able to SEARCH for their menu item')
#def impl(context):
    #if selection is found
    #selection = mainMenu.get_selection(context)
    #menu = SelectionMenu(selection, "Select an option")
#    assert context.actionwords.the_user_will_be_able_to_search_for_their_menu_item()

#@given(r'a menu system')
#def impl(context):
#    context.actionwords.a_menu_system()
#    pass

#@when(r'the user selects the numerical option for EXIT <integer>')
#def impl(context):
#    context.menu.items[3].choose_selection()
#    pass

#@then(r'the user will be able to EXIT and return to MAIN MENU')
#def impl(context):
#    assert context.actionwords.the_user_will_be_able_to_exit_and_return_to_main_menu()
