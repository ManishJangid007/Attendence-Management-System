from tkinter import *
from PIL import ImageTk, Image

class AccountPage():
    def __init__(self, parent):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.textColor = "#0F4189"
        self.font = "Bahnschrift"
        self.cardPng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/cards.png"))
        self.cPassPng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/buttons/changePassword.png"))
        self.cUserPng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/buttons/changeUsername.png"))

    def draw(self):
        card = Label(self.parent, bd=0, bg=self.ligBluePrimColor, image=self.cardPng)
        card.photo = self.cardPng
        card.place(x=18, y=14)

        h1 = Label(self.parent, bd=0, bg=self.bluePrimColor, fg="white", text="Update Password", font=(self.font, 15, 'normal'))
        h1.place(x=97, y=25)

        h2 = Label(self.parent, bd=0, bg=self.bluePrimColor, fg="white", text="Change Username",
                   font=(self.font, 15, 'normal'))
        h2.place(x=465, y=25)

        oldPassLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg=self.textColor, text="Old Password",
                   font=(self.font, 25, 'normal'))
        oldPassLabel.place(x=71.5, y=62)

        oldPassEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                              font=(self.font, 19, 'normal'))
        oldPassEntry.place(x=84, y=118)

        newPassLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg=self.textColor, text="New Password",
                   font=(self.font, 25, 'normal'))
        newPassLabel.place(x=64, y=192)

        newPassEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                             font=(self.font, 19, 'normal'))
        newPassEntry.place(x=84, y=250)

        confirmPassLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg=self.textColor, text="Confirm Password",
                             font=(self.font, 25, 'normal'))
        confirmPassLabel.place(x=40, y=328)

        confirmPassEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                             font=(self.font, 19, 'normal'))
        confirmPassEntry.place(x=84, y=386)

        newUsernameLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg=self.textColor, text="New Username",
                             font=(self.font, 25, 'normal'))
        newUsernameLabel.place(x=434, y=62)

        newUsernameEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                             font=(self.font, 19, 'normal'))
        newUsernameEntry.place(x=457, y=118)

        passwordLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg=self.textColor, text="Password",
                                 font=(self.font, 25, 'normal'))
        passwordLabel.place(x=473, y=192)

        passwordEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                                 font=(self.font, 19, 'normal'))
        passwordEntry.place(x=457, y=250)

        changePassButt = Button(self.parent, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.cPassPng)
        changePassButt.photo = self.cPassPng
        changePassButt.place(x=108, y=455)

        changeUserButt = Button(self.parent, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor,
                                image=self.cUserPng)
        changeUserButt.photo = self.cUserPng
        changeUserButt.place(x=480, y=318)