from tkinter import *

class AddSubjectPage():
    def __init__(self, parent):
        self.parent = parent

    def draw(self):
        Label(self.parent, text="Add Subject").place(x=10, y=10)