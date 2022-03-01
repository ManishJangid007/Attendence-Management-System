from tkinter import *

class AddCoursePage():
    def __init__(self, parent):
        self.parent = parent

    def draw(self):
        Label(self.parent, text="Add Course").place(x=10, y=10)