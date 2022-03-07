from tkinter import *
from PIL import ImageTk, Image

class EditStudentPage():
    def __init__(self, parent, aryaId):
        self.parent = parent
        self.aryaId = aryaId
        self.orangePrimColor = "#FF8C64"
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"
        self.backPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/back.png"
            )
        )

    def draw(self):
        self.editStudentFrame = Frame(self.parent, bd=0, bg="white", height=650, width=1080)
        self.editStudentFrame.place(x=0, y=0)

        aryaIdLabel = Label(self.editStudentFrame, bd=0, bg="white", text=self.aryaId, fg=self.orangePrimColor,
                            font=(self.font, 30, 'normal'))
        aryaIdLabel.place(x=80, y=9)

        def back():
            self.destroy()

        backBut = Button(self.editStudentFrame, bd=0, bg="white", activebackground="white", image=self.backPng, command=back)
        backBut.photo = self.backPng
        backBut.place(x=20, y=20)

    def destroy(self):
        self.editStudentFrame.destroy()

