from tkinter import *
from PIL import ImageTk, Image

class AddTeacherPage():
    def __init__(self, parent):
        self.parent = parent
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/teacherpanel/background.png"))
        self.addPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/teacherpanel/buttons/add.png"))
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"

    def draw(self):
        background = Label(self.parent, bg=self.ligBluePrimColor, bd=0, image=self.backgroundPng)
        background.photo = self.backgroundPng
        background.place(x=100, y=60)

        nameLabel = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="black", text="Full Name",
                          font=(self.font, 15, "normal"))
        nameLabel.place(x=100, y=30)

        nameEntry = Entry(self.parent, bg="white", bd=0, width=14, justify="center",
                          font=(self.font, 21, 'normal'))
        nameEntry.place(x=109.5, y=64)

        usernameLabel = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="black", text="Username",
                              font=(self.font, 15, "normal"))
        usernameLabel.place(x=400, y=30)

        usernameEntry = Entry(self.parent, bg="white", bd=0, width=14, justify="center",
                              font=(self.font, 21, 'normal'))
        usernameEntry.place(x=411, y=64)

        emailLabel = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="black", text="E-mail",
                           font=(self.font, 15, "normal"))
        emailLabel.place(x=100, y=143)

        emailEntry = Entry(self.parent, bg="white", bd=0, width=14, justify="center",
                           font=(self.font, 21, 'normal'))
        emailEntry.place(x=109.5, y=176)

        passwordLabel = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="black", text="Password",
                              font=(self.font, 15, "normal"))
        passwordLabel.place(x=400, y=143)

        passwordEntry = Entry(self.parent, bg="white", bd=0, width=14, justify="center",
                              font=(self.font, 21, 'normal'), show="*")
        passwordEntry.place(x=411, y=176)

        phoneLabel = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="black", text="Phone No.",
                           font=(self.font, 15, "normal"))
        phoneLabel.place(x=100, y=261)

        phoneEntry = Entry(self.parent, bg="white", bd=0, width=14, justify="center",
                           font=(self.font, 21, 'normal'))
        phoneEntry.place(x=109.5, y=293)

        confirmPassLabel = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="black",
                                 text="Confirm Password",
                                 font=(self.font, 15, "normal"))
        confirmPassLabel.place(x=400, y=261)

        confirmPassEntry = Entry(self.parent, bg="white", bd=0, width=14, justify="center",
                                 font=(self.font, 21, 'normal'), show="*")
        confirmPassEntry.place(x=411, y=293)

        error1 = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error1.place(x=110, y=108)

        error2 = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error2.place(x=412, y=108)

        error3 = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error3.place(x=110, y=220)

        error4 = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error4.place(x=412, y=220)

        error5 = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error5.place(x=110, y=336)

        error6 = Label(self.parent, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error6.place(x=412, y=336)

        def clear_error():
            error1.config(text="")  # name
            error2.config(text="")  # username
            error3.config(text="")  # email
            error4.config(text="")  # password
            error5.config(text="")  # phone no.
            error6.config(text="")  # confirmpass

        def add_fun():
            clear_error()
            validate = True
            name = nameEntry.get()
            username = usernameEntry.get()
            email = emailEntry.get()
            password = passwordEntry.get()
            phone = phoneEntry.get()
            confirmPass = confirmPassEntry.get()

            if len(name) < 4 or len(name) > 25:
                validate = False
                error1.config(text="*name character's should be(4-25)")

            if len(username) < 4 or len(username) > 12:
                validate = False
                error2.config(text="*username character's should be(4-12)")
            # verify duplicate username

            if len(email) < 5:
                validate = False
                error3.config(text="*enter valid email")

            if len(password) < 8 or len(password) > 18:
                validate = False
                error4.config(text="*password character's should be(8-18)")

            if len(phone) == 10:
                num = list(phone)
                for d in num:
                    asa = ord(d)
                    for i in range(47, 59):
                        if asa == i:
                            break
                        elif i > 57:
                            validate = False
                            error5.config(text="*enter valid number")
            else:
                validate = False
                error5.config(text="*enter valid number")

            if len(confirmPass) > 0:
                if confirmPass != password:
                    validate = False
                    error6.config(text="*password not match")
            else:
                validate = False
                error6.config(text="*don't leave this field blank")

            if validate:
                # fire your query here!
                clear_error()
                print("Done!")

        addButton = Button(self.parent, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                           bd=0, image=self.addPng, command=add_fun)
        addButton.photo = self.addPng
        addButton.place(x=328, y=420)