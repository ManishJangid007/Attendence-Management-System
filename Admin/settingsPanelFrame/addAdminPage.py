from tkinter import *
from PIL import ImageTk, Image

class AddAdminPage():
    def __init__(self, parent):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.textColor = "#0F4189"
        self.font = "Bahnschrift"
        self.cardPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/settingspanel/card.png"))
        self.createPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/settingspanel/buttons/create.png"))

    def draw(self):
        card = Label(self.parent, bd=0, bg=self.ligBluePrimColor, image=self.cardPng)
        card.photo = self.cardPng
        card.place(x=190, y=28)

        usernameLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg=self.textColor, text="Username", font=(self.font, 25, 'normal'))
        usernameLabel.place(x=288, y=57)

        usernameEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                        font=(self.font, 19, 'normal'))
        usernameEntry.place(x=273, y=114)

        passwordLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg=self.textColor, text="Password",
                              font=(self.font, 25, 'normal'))
        passwordLabel.place(x=290, y=182)

        passwordEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                              font=(self.font, 19, 'normal'))
        passwordEntry.place(x=273, y=239)

        passwordLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg=self.textColor, text="Confirm Password",
                              font=(self.font, 25, 'normal'))
        passwordLabel.place(x=225, y=310)

        cPasswordEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                              font=(self.font, 19, 'normal'))
        cPasswordEntry.place(x=273, y=368)

        createBut = Button(self.parent, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.createPng)
        createBut.photo = self.createPng
        createBut.place(x=332, y=445)