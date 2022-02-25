from tkinter import *
from PIL import ImageTk, Image

class AddStudentPage():
    def __init__(self, parent):
        self.parent = parent
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/background.png"))
        self.addPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/buttons/add.png"))
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"

    def draw(self):
        background = Label(self.parent, bd=0, bg=self.ligBluePrimColor, image=self.backgroundPng)
        background.photo = self.backgroundPng
        background.place(x=90, y=25)

        addButton = Button(self.parent, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor, image=self.addPng)
        addButton.photo = self.addPng
        addButton.place(x=655, y=485)