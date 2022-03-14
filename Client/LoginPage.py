from ErrorPage import *
from tkinter import *
from PIL import ImageTk, Image
from ServerSide.Connection import *
from HomePage import HomePage

class LoginPage():
    def __init__(self, root):
        self.root = root
        #assets
        self.bgImage = ImageTk.PhotoImage(Image.open("assets/Login_Page_Assets/Background.png"))
        self.loginButtonPng = ImageTk.PhotoImage(Image.open("assets//Login_Page_Assets/button/login.png"))
        self.backgroundColor = "#f2f8ff"
        self.font = "Bahnschrift"
        self.fontColor = "#0f4189"
        self.primaryColor = "#ff793f"
        self.errorColor = "#c63038"
        self.textBoxColor = "#87a0c4"

    def draw(self):
        self.login_page_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.login_page_frame.place(x=0, y=0)

        self.background = Label(self.login_page_frame, bg="white", bd=0, image=self.bgImage)
        self.background.photo = self.bgImage
        self.background.place(x=12, y=5)

        self.attLabel = Label(self.login_page_frame, fg=self.primaryColor, text="Attendence", bd=0, bg=self.backgroundColor, font=(self.font, 35, "normal"))
        self.attLabel.place(x=150, y=50)

        self.msLabel = Label(self.login_page_frame, fg=self.fontColor, text="Management System", bd=0, bg=self.backgroundColor, font=(self.font, 35, "normal"))
        self.msLabel.place(x=150, y=100)

        self.loginLabel = Label(self.login_page_frame, fg=self.fontColor, text="Login", bd=0, bg=self.backgroundColor, font=(self.font, 30, "normal"))
        self.loginLabel.place(x=820, y=83)

        self.unLabel = Label(self.login_page_frame, fg=self.fontColor, text="Username", bg=self.backgroundColor, font=(self.font, 15, "normal"),bd=0)
        self.unLabel.place(x=775, y=195)

        self.unEntry = Entry(self.login_page_frame, fg="black", bg=self.textBoxColor, width=17, bd=0, font=(self.font, 15, "normal"), justify="center")
        self.unEntry.place(x=786, y=248)

        self.passLabel = Label(self.login_page_frame, fg=self.fontColor, text="Password", bg=self.backgroundColor, font=(self.font, 15, "normal"), bd=0)
        self.passLabel.place(x=892, y=352)

        self.passEntry = Entry(self.login_page_frame, fg="black", bg=self.textBoxColor, width=17, bd=0, font=(self.font, 15, "normal"), justify="center", show="*")
        self.passEntry.place(x=786, y=402)

        def logfun():
            if Connection().check():
                if Connection().check_database():
                    try:
                        self.errorLabel.destroy()
                    except:
                        pass
                    userName = self.unEntry.get()
                    password = self.passEntry.get()
                    if len(userName) > 0 and len(password) > 0:
                        HomePage(self.root, userName)
                    else:
                        self.errorLabel = Label(self.login_page_frame, fg=self.errorColor, text="*Invalid username & password", bd=0, bg=self.backgroundColor, font=(self.font, 10, "normal"))
                        self.errorLabel.place(x=794, y=452)
                else:
                    ErrorPage(self.root, message="Database Not Found").draw()
            else:
                ErrorPage(self.root, message="You're Disconnected from Server").draw()

        self.loginButton = Button(self.login_page_frame, bg=self.backgroundColor, activebackground=self.backgroundColor, bd=0, image=self.loginButtonPng, command=logfun)
        self.loginButton.photo = self.loginButtonPng
        self.loginButton.place(x=840, y=530)

    def destroy(self):
        self.login_page_frame.destroy()
