from tkinter import *
from PIL import ImageTk, Image
from step1 import *
from step2 import *
from Admin.Connection import *
from Admin.LoginPage import *

class SetupPage():
    def __init__(self, root):
        self.root = root
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/background.png"))
        self.primaryColor = "#ff793f"
        self.textColor = "#333030"
        self.secondaryColor = "#3615f6"
        self.backgroundColor = "#f2f8ff"
        self.font = "Bahnschrift"
        self.initialButPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Buttons/initial.png"))
        self.reconnectButPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Buttons/reconnect.png"))

    def draw(self):
        self.setup_page_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.setup_page_frame.place(x=0, y=0)

        self.background = Label(self.setup_page_frame, bg="white", bd=0, image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=-98, y=-50)

        self.attLabel = Label(self.setup_page_frame, fg=self.primaryColor, text="Attendence", bd=0, bg=self.backgroundColor, font=(self.font, 32, "normal"))
        self.attLabel.place(x=150, y=90)

        self.msLabel = Label(self.setup_page_frame, fg=self.textColor, text="Management System", bd=0,
                              bg=self.backgroundColor, font=(self.font, 32, "normal"))
        self.msLabel.place(x=380, y=90)

        self.adminLabel = Label(self.setup_page_frame, fg=self.primaryColor, text="Admin", bd=0,
                             bg=self.backgroundColor, font=(self.font, 32, "normal"))
        self.adminLabel.place(x=340, y=150)

        self.portalLabel = Label(self.setup_page_frame, fg=self.textColor, text="Portal", bd=0,
                                bg=self.backgroundColor, font=(self.font, 32, "normal"))
        self.portalLabel.place(x=475, y=150)

        self.message0Label = Label(self.setup_page_frame, fg=self.textColor, text="We Could not Found Database,", bd=0,
                                 bg="white", font=(self.font, 20, "normal"))
        self.message0Label.place(x=630, y=480)

        self.message1Label = Label(self.setup_page_frame, fg=self.textColor,
                                   text="Would You Like to Begin", bd=0,
                                   bg="white", font=(self.font, 20, "normal"))
        self.message1Label.place(x=630, y=520)

        self.message1Label = Label(self.setup_page_frame, fg=self.textColor,
                                   text="or Try to", bd=0,
                                   bg="white", font=(self.font, 20, "normal"))
        self.message1Label.place(x=630, y=560)

        self.errorMessage = Label(self.setup_page_frame, fg="red",
                                   text="", bd=0,
                                   bg="white", font=(self.font, 10, "normal"))
        self.errorMessage.place(x=650, y=610)

        def start_setup():
            Step1(root=self.root, parent=self.setup_page_frame).draw()

        self.initialBut = Button(self.setup_page_frame, bg="white", activebackground="white", bd=0, image=self.initialButPng, command=start_setup)
        self.initialBut.photo = self.initialButPng
        self.initialBut.place(x=930, y=523)

        def reconnect():
            if Connection().check():
                if Connection().check_database():
                    self.destroy()
                    LoginPage(self.root).draw()
                else:
                    self.errorMessage.config(text="*We Could not Found Database")
            else:
                self.errorMessage.config(text="*We Could not Found Server")

        self.reconnectBut = Button(self.setup_page_frame, bg="white", activebackground="white", bd=0,
                                 image=self.reconnectButPng, command=reconnect)
        self.reconnectBut.photo = self.reconnectButPng
        self.reconnectBut.place(x=745, y=563)

    def destroy(self):
        self.setup_page_frame.destroy()

