from cursesmenu import CursesMenu
from cursesmenu.items import MultiSelectionItem


def multiSelection():
    return True


class MultiSelectionMenu(CursesMenu):
    """
    A menu that simplifies item creation, just give it a list of strings and it builds the menu for you
    """

    def __init__(self, options, title=None, subtitle="Use 'x' to choose your items.", show_exit_option=True):
        """
        :ivar list[str] strings: The list of strings this menu should be built from
        """
        super(MultiSelectionMenu, self).__init__(title, subtitle, show_exit_option)
        for option in options:
            self.append_item(MultiSelectionItem({
                "label": option,
                "selected": self
            }))

    @classmethod
    def get_selection(cls, options, title, subtitle, exit_option=True, _menu=None):
        """
        Single-method way of getting a selection out of a list of strings

        :param list[str] strings: the list of string used to build the menu
        :param list _menu: should probably only be used for testing, pass in a list and the created menu used \
        internally by the method will be appended to it
        """
        menu = cls(options, title, subtitle, exit_option)
        if _menu is not None:
            _menu.append(menu)
        menu.show()
        menu.join()
        return menu.selected_option

    def define_items_selected(self):
        all_options = []
        for option in self.items:
            if options.add_selection:
                all_options.append(option.item_selected is False)
        return all_options

    multiSelection()
