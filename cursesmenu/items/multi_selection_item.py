from cursesmenu.items import MenuItem

class MultiSelectionItem(MenuItem):
    def __init__(self, item_selected, menu = None):
        super(MultiSelectionItem, self).__init__(item_selected=item_selected, menu=menu, should_exit=True)
        self.add_selection = False
        self.item_selected = "[ ]" + self.item_selected


    def show_selected_items(self):
        if self.add_selection:
            self.add_selection = False
            self.item_selected = self.item_selected.replace("[X]", "[ ]")
        else:
            self.add_selection = True
            self.item_selected = self.item_selected.replace("[ ]", "[X]")
