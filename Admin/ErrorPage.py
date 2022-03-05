from ChangeParaPage import *
from tkinter import *
from PIL import ImageTk
from ServerSide.Connection import *

class ErrorPage():
    def __init__(self, root, message="Can't Reach to the Server", parameterOption=False):
        self.message = message
        self.parameterOption = parameterOption
        self.root = root
        self.backgroundPng = ImageTk.PhotoImage(file="Assets/Error_Page_Assets/Background.png")
        self.fontColor = "#0f4189"
        self.font = "Bahnschrift"
        self.backgroundColor = "#f2f8ff"
        self.secondaryFontColor = "#666a7b"
        self.retryButtonPng = ImageTk.PhotoImage(file="Assets/Error_Page_Assets/Button/retry.png")
        self.ccpButtonPng = ImageTk.PhotoImage(file="Assets/Error_Page_Assets/Button/ccp.png")

    def draw(self):
        self.error_page_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.error_page_frame.place(x=0, y=0)

        self.background = Label(self.error_page_frame, bd=0, bg="white", image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=12, y=5)

        self.errorLabel = Label(self.error_page_frame, text="Error Occurred !", bd=0, bg=self.backgroundColor,
                                fg=self.fontColor, font=(self.font, 35, "normal"))
        self.errorLabel.place(x=390, y=20)

        self.messageLabel = Label(self.error_page_frame, text=self.message, bd=0, bg=self.backgroundColor,
                                fg=self.secondaryFontColor, font=(self.font, 15, "normal"))
        self.messageLabel.place(x=440, y=90)

        def retryfun():
            conn = Connection()
            if conn.check():
                if conn.check_database():
                    self.destroy()

        def ccpfun():
            ParaPage(root=self.root, parent=self.error_page_frame).draw()

        if self.parameterOption:
            self.retryButton = Button(self.error_page_frame, bg=self.backgroundColor,
                                      activebackground=self.backgroundColor, bd=0, image=self.retryButtonPng,
                                      command=retryfun)
            self.retryButton.photo = self.retryButtonPng
            self.retryButton.place(x=300, y=560)

            self.ccpButton = Button(self.error_page_frame, bg=self.backgroundColor,
                                      activebackground=self.backgroundColor, bd=0, image=self.ccpButtonPng, command=ccpfun)
            self.ccpButton.photo = self.ccpButtonPng
            self.ccpButton.place(x=450, y=560)
        else:
            self.retryButton = Button(self.error_page_frame, bg=self.backgroundColor, activebackground=self.backgroundColor, bd=0, image=self.retryButtonPng, command=retryfun)
            self.retryButton.photo = self.retryButtonPng
            self.retryButton.place(x=490, y=560)

    def destroy(self):
        self.error_page_frame.destroy()
