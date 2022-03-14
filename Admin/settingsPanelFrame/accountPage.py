from tkinter import *
from PIL import ImageTk, Image
from ServerSide.SelectOperation import SelectOperation

class AccountPage():
    def __init__(self, parent, username):
        self.parent = parent
        self.username = username
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

        error01 = Label(self.parent, bg=self.bluePrimColor, fg="red", text="", font=(self.font, 14, 'normal'))
        error01.place(x=84, y=160)
        error02 = Label(self.parent, bg=self.bluePrimColor, fg="red", text="", font=(self.font, 14, 'normal'))
        error02.place(x=84, y=290)
        error03 = Label(self.parent, bg=self.bluePrimColor, fg="red", text="", font=(self.font, 14, 'normal'))
        error03.place(x=84, y=423)

        error11 = Label(self.parent, bg=self.bluePrimColor, fg="red", text="", font=(self.font, 14, 'normal'))
        error11.place(x=457, y=160)
        error12 = Label(self.parent, bg=self.bluePrimColor, fg="red", text="", font=(self.font, 14, 'normal'))
        error12.place(x=457, y=288)

        def clear_errors():
            error01.config(text="")
            error02.config(text="")
            error03.config(text="")
            error11.config(text="")
            error12.config(text="")

        def clear_errors0():
            error01.config(text="")
            error02.config(text="")
            error03.config(text="")

        def clear_errors1():
            error11.config(text="")
            error12.config(text="")

        def clear_fields0():
            oldPassEntry.delete(0, END)
            newPassEntry.delete(0, END)
            confirmPassEntry.delete(0, END)

        def clear_fields1():
            newUsernameEntry.delete(0, END)
            passwordEntry.delete(0, END)

        def change_password():
            clear_errors0()
            old_password = oldPassEntry.get()
            new_password = newPassEntry.get()
            confirm_password = confirmPassEntry.get()

            validate = True

            if len(old_password) < 1:
                validate = False
                error01.config(text="Field Blank")

            if SelectOperation().verifyAdmin(self.username, old_password) == False:
                validate = False
                error01.config(text="Incorrect Password")

            if len(new_password) < 8 or len(new_password) > 18:
                validate = False
                error02.config(text="Enter Password Length (8-18)")
            else:
                if new_password == old_password:
                    validate = False
                    error02.config(text="New Password Cannot Be Same")

            if confirm_password != new_password:
                validate = False
                error03.config(text="Password Not Match !")

            if validate:
                clear_errors0()

        changePassButt = Button(self.parent, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.cPassPng, command=change_password)
        changePassButt.photo = self.cPassPng
        changePassButt.place(x=108, y=455)

        def change_username():
            clear_errors1()
            new_username = newUsernameEntry.get()
            password = passwordEntry.get()
            validate = True

            if len(new_username) < 2 or len(new_username) > 20:
                validate = False
                error11.config(text="Field Blank Length (2-20)")

            if new_username == self.username:
                validate = False
                error11.config(text="Username Cannot Be Same")

            if len(password) < 1:
                validate = False
                error12.config(text="Field Blank")
            else:
                if SelectOperation().verifyAdmin(self.username, password):
                    validate = False
                    error12.config(text="Incorrect Password !")

            if validate:
                clear_errors1()


        changeUserButt = Button(self.parent, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor,
                                image=self.cUserPng, command=change_username)
        changeUserButt.photo = self.cUserPng
        changeUserButt.place(x=480, y=318)