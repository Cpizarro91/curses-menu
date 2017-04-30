from cursesmenu.items import MenuItem


class MultiItem(MenuItem):
    def __init__(self, text_color, text, menu=None):
        super(MultiItem, self).__init__(text_color=text_color, text=text, menu=menu, should_exit=True)
        self.selected = False
        self.text = "[ ]" + self.text

    def choose_selection(self):
        if self.selected:
            self.selected = False
            self.text = self.text.replace("[X]", "[ ]")
        else:
            self.selected = True
            self.text = self.text.replace("[ ]", "[X]")


