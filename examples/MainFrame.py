import wx

from cursesmenu import *
from cursesmenu.items import *

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.CreateMenuBar()
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel = wx.Panel(self)
        panel.SetSizer(sizer)
        sizer.Layout()

    def OnClose(self, evt):
        self.Destroy()
        evt.Skip()

    def CreateMenuBar(self):
        file_menu = wx.Menu()
        AS_EXIT = wx.NewId()
        file_menu.Append(AS_EXIT, "&Exit")
        self.Bind(wx.EVT_MENU, self.OnClose, id=AS_EXIT)


def start_hci():
    app = wx.PySimpleApp()
    f = MainFrame(parent=None, id=-1)
    f.Show()
    app.MainLoop()

if __name__ == "__main__":

    use_wx_with_curses = True  # combine wxpython and curses or not

    if use_wx_with_curses:
        menu = CursesMenu("Version 0.1", "Debug HCI")
        menu.append_item(FunctionItem("Start HCI", start_hci, ""))
        menu.show()
    else:
        start_hci()
