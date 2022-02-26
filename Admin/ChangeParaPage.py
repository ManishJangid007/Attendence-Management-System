from tkinter import *
from PIL import ImageTk, Image
from Admin.ServerSide.Connection import *

class ParaPage():
    def __init__(self, root, parent):
        self.root = root
        self.parent = parent
        #assets
        self.ccp_backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Error_Page_Assets/connectbg.png"))
        self.cancelButtonPng = ImageTk.PhotoImage(Image.open("Assets/Error_Page_Assets/Button/cancel.png"))
        self.connectButtonPng = ImageTk.PhotoImage(Image.open("Assets/Error_Page_Assets/Button/connect.png"))
        self.fontColor = "#0f4189"
        self.font = "Bahnschrift"
        self.backgroundColor = "#f2f8ff"
        self.inputBgColor = "#6c63ff"
        self.messageBgColor = "#3f3d56"

    def draw(self, ):
        self.ccp_frame = Frame(self.root, bd=0, bg="white", height=650, width=1080)
        self.ccp_frame.place(x=0, y=0)

        self.ccp_background = Label(self.ccp_frame, bd=0, bg="white", image=self.ccp_backgroundPng)
        self.ccp_background.photo = self.ccp_backgroundPng
        self.ccp_background.place(x=12, y=5)

        self.heading = Label(self.ccp_background, text="Enter Your Configuration", bd=0, bg=self.backgroundColor,
                                fg=self.fontColor, font=(self.font, 40, "normal"))
        self.heading.place(x=420, y=23)

        self.ipLabel = Label(self.ccp_background, text="IP", bd=0, bg=self.inputBgColor,
                             fg="white", font=(self.font, 20, "normal"))
        self.ipLabel.place(x=30, y=170)

        self.ipEntry = Entry(self.ccp_frame, fg="white", bg=self.inputBgColor, width=17, bd=0,
                             font=(self.font, 20, "normal"), justify="left")
        self.ipEntry.place(x=90, y=175)

        self.userLabel = Label(self.ccp_background, text="User", bd=0, bg=self.inputBgColor,
                             fg="white", font=(self.font, 20, "normal"))
        self.userLabel.place(x=30, y=268)

        self.userEntry = Entry(self.ccp_frame, fg="white", bg=self.inputBgColor, width=14, bd=0,
                             font=(self.font, 20, "normal"), justify="left")
        self.userEntry.place(x=125, y=275)

        self.passLabel = Label(self.ccp_background, text="Password", bd=0, bg=self.inputBgColor,
                             fg="white", font=(self.font, 20, "normal"))
        self.passLabel.place(x=30, y=376)

        self.passEntry = Entry(self.ccp_frame, fg="white", bg=self.inputBgColor, width=10, bd=0,
                             font=(self.font, 20, "normal"), justify="left", show="*")
        self.passEntry.place(x=190, y=383)

        def set_message(message, x, y):
            self.messageLabel = Label(self.ccp_frame, bd=0, fg="white", bg=self.messageBgColor, text=message,
                                      font=(self.font, 20, "normal"))
            self.messageLabel.place(x=x, y=y)

        set_message(message="{ Welcome }", x=795, y=335)

        def cancel():
            self.destroy()

        self.cancelButton = Button(self.ccp_frame, bd=0, bg=self.backgroundColor, activebackground=self.backgroundColor, image=self.cancelButtonPng, command=cancel)
        self.cancelButton.photo = self.cancelButtonPng
        self.cancelButton.place(x=30, y=20)

        def connect():
            ip = self.ipEntry.get()
            user = self.userEntry.get()
            passw = self.passEntry.get()
            if len(ip) <= 0 or len(user) <= 0:
                set_message("{ Enter \n Configuration }", x=770, y=320)
                return

            lconn = LocalConnection()
            lconn.set_parameters(ip, user, passw)

            conn = Connection()
            if conn.check():
                self.parent.destroy()
                self.destroy()
            else:
                set_message(message="{ Can't Connect \n to the Network }", x=770, y=320)

        self.connectButton = Button(self.ccp_frame, bd=0, bg=self.backgroundColor, activebackground=self.backgroundColor,
                                   image=self.connectButtonPng, command=connect)
        self.connectButton.photo = self.connectButtonPng
        self.connectButton.place(x=135, y=470)

    def destroy(self):
        self.ccp_frame.destroy()
