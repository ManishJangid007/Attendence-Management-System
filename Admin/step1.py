from tkinter import *
from PIL import ImageTk, Image
from Admin.step2 import Step2

class Step1():
    def __init__(self, root, parent):
        self.root = root
        self.parent = parent
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step1/background.png"))
        self.closePng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step1/Button/close.png"))
        self.thisPcPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step1/Button/thispc.png"))
        self.remotePcPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step1/Button/remoteserver.png"))
        self.textColor = "#333030"
        self.font = "Bahnschrift"
        self.headBackColor = "#E5E5E5"

    def draw(self):
        self.step1_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.step1_frame.place(x=0, y=0)

        self.background = Label(self.step1_frame, bg="white", bd=0, image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=-98, y=-50)

        self.setEnvLabel = Label(self.step1_frame, fg=self.textColor, text="Setup Environment On ?", bd=0,
                              bg=self.headBackColor, font=(self.font, 30, "normal"))
        self.setEnvLabel.place(x=510, y=125)

        def thispcfun():
            Step2(root=self.root, onthis=True, parent=self.step1_frame).draw()

        self.thisPcBut = Button(self.step1_frame, bg="white", activebackground="white", bd=0,
                               image=self.thisPcPng, command=thispcfun)
        self.thisPcBut.photo = self.thisPcPng
        self.thisPcBut.place(x=648, y=400)

        def remotefun():
            Step2(root=self.root, onthis=False, parent=self.step1_frame).draw()

        self.remotePcBut = Button(self.step1_frame, bg="white", activebackground="white", bd=0,
                                image=self.remotePcPng, command=remotefun)
        self.remotePcBut.photo = self.remotePcPng
        self.remotePcBut.place(x=868, y=535)

        def close():
            self.destroy()

        self.closeBut = Button(self.step1_frame, bg="white", activebackground="white", bd=0,
                                 image=self.closePng, command=close)
        self.closeBut.photo = self.closePng
        self.closeBut.place(x=170, y=10)

    def destroy(self):
        self.step1_frame.destroy()
