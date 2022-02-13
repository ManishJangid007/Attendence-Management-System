from tkinter import *
from PIL import ImageTk, Image
from Connection import *
from ErrorPage import *

class LoginPage():
    def __init__(self, root):
        self.root = root
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Login_Page_Assets/background.png"))
        self.loginButtonPng = ImageTk.PhotoImage(Image.open("Assets/Login_Page_Assets/Button/login.png"))
        self.font = "Bahnschrift"
        self.primaryColor = "#ff793f"
        self.textBoxColor = "#87a0c4"
        self.fontColor = "#0f4189"
        self.errorColor = "#c63038"

    def draw(self):
        self.login_page_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.login_page_frame.place(x=0, y=0)

        self.background = Label(self.login_page_frame, bg="white", bd=0, image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=12, y=5)

        self.attLabel = Label(self.login_page_frame, fg=self.primaryColor, text="Attendence", bd=0,
                              bg="white", font=(self.font, 32, "normal"))
        self.attLabel.place(x=510, y=50)

        self.manageLabel = Label(self.login_page_frame, fg=self.fontColor, text="Management", bd=0,
                             bg="white", font=(self.font, 32, "normal"))
        self.manageLabel.place(x=740, y=50)

        self.systemLabel = Label(self.login_page_frame, fg=self.fontColor, text="System", bd=0,
                                 bg="white", font=(self.font, 32, "normal"))
        self.systemLabel.place(x=540, y=110)

        self.adminLabel = Label(self.login_page_frame, fg=self.primaryColor, text="Admin", bd=0,
                              bg="white", font=(self.font, 32, "normal"))
        self.adminLabel.place(x=695, y=110)

        self.portalLabel = Label(self.login_page_frame, fg=self.fontColor, text="Portal", bd=0,
                                 bg="white", font=(self.font, 32, "normal"))
        self.portalLabel.place(x=830, y=110)

        self.loginLabel = Label(self.login_page_frame, fg=self.fontColor, text="Login", bd=0, bg="white",
                                font=(self.font, 30, "normal"))
        self.loginLabel.place(x=150, y=84)

        self.unLabel = Label(self.login_page_frame, fg=self.fontColor, text="Username", bg="white",
                             font=(self.font, 15, "normal"), bd=0)
        self.unLabel.place(x=115, y=211)

        self.unEntry = Entry(self.login_page_frame, fg="black", bg=self.textBoxColor, width=17, bd=0,
                             font=(self.font, 15, "normal"), justify="center")
        self.unEntry.place(x=123, y=265)

        self.passLabel = Label(self.login_page_frame, fg=self.fontColor, text="Password", bg="white",
                               font=(self.font, 15, "normal"), bd=0)
        self.passLabel.place(x=230, y=360)

        self.passEntry = Entry(self.login_page_frame, fg="black", bg=self.textBoxColor, width=17, bd=0,
                               font=(self.font, 15, "normal"), justify="center", show="*")
        self.passEntry.place(x=123, y=411)

        def logfun():
            if Connection().check():
                try:
                    self.errorLabel.destroy()
                except:
                    pass
                userName = self.unEntry.get()
                password = self.passEntry.get()
                if len(userName) > 0 and len(password) > 0:
                    self.login_page_frame.destroy()
                else:
                    self.errorLabel = Label(self.login_page_frame, fg=self.errorColor,
                                            text="*Invalid username & password", bd=0, bg="white",
                                            font=(self.font, 10, "normal"))
                    self.errorLabel.place(x=122, y=455)
            else:
                ErrorPage(root=self.root, message="You're Disconnected from Server", parameterOption=True).draw()

        self.loginButton = Button(self.login_page_frame, bg="white", activebackground="white",
                                  bd=0, image=self.loginButtonPng, command=logfun)
        self.loginButton.photo = self.loginButtonPng
        self.loginButton.place(x=175, y=530)

    def destroy(self):
        self.login_page_frame.destroy()