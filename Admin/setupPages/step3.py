from tkinter import *
from PIL import ImageTk, Image
from setupPages.step4 import Step4

class Step3():
    def __init__(self, root, parent):
        self.parent = parent
        self.root = root
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step3/background.png"))
        self.backButtPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step3/Button/back.png"))
        self.createDataPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step3/Button/create.png"))
        self.font = "Bahnschrift"
        self.primaryColor = "#ff793f"

    def draw(self):
        self.step3_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.step3_frame.place(x=0, y=0)

        self.background = Label(self.step3_frame, bg="white", bd=0, image=self.backgroundPng )
        self.background.photo = self.backgroundPng
        self.background.place(x=12, y=5)

        self.heading = Label(self.step3_frame, fg="black", text="Let's Setup Your", bd=0, bg="white", font=(self.font, 30, 'normal'))
        self.heading.place(x=725, y=300)

        self.heading1 = Label(self.step3_frame, fg=self.primaryColor, text="Database", bd=0, bg="white",
                             font=(self.font, 30, 'normal'))
        self.heading1.place(x=725, y=350)

        def back():
            self.destroy()

        self.backButt = Button(self.step3_frame, bg="white", activebackground="white", bd=0,
                               image=self.backButtPng, command=back)
        self.backButt.photo = self.backButtPng
        self.backButt.place(x=20, y=15)

        def create():
            Step4(root=self.root, parent=self.step3_frame).draw()

        self.createData = Button(self.step3_frame, bg="white", activebackground="white", bd=0,
                               image=self.createDataPng, command=create)
        self.createData.photo = self.createDataPng
        self.createData.place(x=725, y=450)

    def destroy(self):
        self.step3_frame.destroy()

