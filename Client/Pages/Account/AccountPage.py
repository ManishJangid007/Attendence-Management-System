from tkinter import *

class AccountPage():
    def __init__(self, parent):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"

    def draw(self):
        self.frame = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.frame.place(x=0, y=0)

        Label(self.frame, bg=self.ligBluePrimColor, text="Account Page").place(x=20, y=20)

    def destroy(self):
        self.frame.destroy()