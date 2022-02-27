from tkinter import *
from PIL import ImageTk, Image

class SearchResultPage():
    def __init__(self, parent, course, year):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"
        self.course = course
        self.year = year
        self.backButPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/buttons/back.png"))

    def draw(self):
        self.searchResultFrame = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.searchResultFrame.place(x=0, y=0)

        def back():
            self.destroy()

        backButt = Button(self.searchResultFrame, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                          image=self.backButPng, command=back)
        backButt.photo = self.backButPng
        backButt.place(x=10, y=10)

    def destroy(self):
        self.searchResultFrame.destroy()