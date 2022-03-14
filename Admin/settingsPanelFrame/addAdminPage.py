from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from ServerSide.SelectOperation import SelectOperation
from ServerSide.InsertOperations import InsertOperations

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
                              font=(self.font, 19, 'normal'), show="*")
        passwordEntry.place(x=273, y=239)

        passwordLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg=self.textColor, text="Confirm Password",
                              font=(self.font, 25, 'normal'))
        passwordLabel.place(x=225, y=310)

        cPasswordEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                              font=(self.font, 19, 'normal'), show="*")
        cPasswordEntry.place(x=273, y=368)

        def clear_fields():
            usernameEntry.delete(0, END)
            passwordEntry.delete(0, END)
            cPasswordEntry.delete(0, END)

        def create():
            username = usernameEntry.get()
            password = passwordEntry.get()
            confirm_password = cPasswordEntry.get()
            validate = True

            if len(username) < 2 or len(username) > 20:
                validate = False
                messagebox.showerror(title="Wrong Entry", message="Enter Correct Course Name")
            else:
                if SelectOperation().checkExistenceOfAdmin(username):
                    validate = False
                    messagebox.showerror(title="Wrong Entry", message="User Already Exist !")
                else:
                    if len(password) < 8 or len(password) > 18:
                        validate = False
                        messagebox.showerror(title="Wrong Entry", message="Enter Password Length (8-18)")
                    else:
                        if password != confirm_password:
                            validate = False
                            messagebox.showerror(title="Wrong Entry", message="Password Not Match !")

            if validate:
                if InsertOperations().insertAdmin(username, password):
                    messagebox.showinfo(title="Success", message="Admin Added Successfully !")
                    clear_fields()
                else:
                    messagebox.showerror(title="Error Occurred", message="Something Went Wrong !")

        createBut = Button(self.parent, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.createPng, command=create)
        createBut.photo = self.createPng
        createBut.place(x=332, y=445)