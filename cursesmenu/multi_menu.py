# using the github picker and pick for examples
# structure based off selection menu
from cursesmenu import CursesMenu
from cursesmenu.items import MultiItem


class MultiMenu(CursesMenu):
    """
    A menu that allows the user to select multiple options from the Curses Menu
    """

    def __init__(self,
                 choices,
                 title=None,
                 subtitle="Use the space bar to select/unselect items and the enter key to finish",
                 show_exit_option=False):
        super(MultiMenu, self).__init__(title, subtitle, show_exit_option)
        for choice in choices:
            self.append_item(MultiItem("Main Menu", choice, self))

    def gather_selections(self):
        list_of_selections = []
        for choice in self.items:
            if choice.selected:
                list_of_selections.append(choice.text.replace("[X]", ""))
        return list_of_selections

    @staticmethod
    def use_multi():
        """
        
        :return: True if using the multimenu
        """
        return True
