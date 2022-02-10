from tkinter import *
from PIL import ImageTk, Image

class Step4():
    def __init__(self, root, parent):
        self.parent = parent
        self.root = root
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step4/background.png"))
        self.font = "Bahnschrift"
        self.primaryColor = "#ff793f"

    def draw(self):
        self.step4_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.step4_frame.place(x=0, y=0)

        self.background = Label(self.step4_frame, bg="white", bd=0, image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=12, y=5)

        self.h1 = Label(self.step4_frame, fg="black", text="Set Back and", bd=0, bg="white", font=(self.font, 33, 'normal'))
        self.h1.place(x=650, y=250)

        self.h2 = Label(self.step4_frame, fg=self.primaryColor, text="Relax.", bd=0, bg="white",
                        font=(self.font, 33, 'normal'))
        self.h2.place(x=920, y=250)

        self.h3 = Label(self.step4_frame, fg="black", text="While We Setting Up", bd=0, bg="white",
                        font=(self.font, 33, 'normal'))
        self.h3.place(x=645, y=310)

        self.h4 = Label(self.step4_frame, fg="black", text="Thing For You...", bd=0, bg="white",
                        font=(self.font, 33, 'normal'))
        self.h4.place(x=700, y=370)

        self.h5 = Label(self.step4_frame, fg="black", text="*Note : Do Not Close The Application", bd=0, bg="white",
                        font=(self.font, 12, 'normal'))
        self.h5.place(x=780, y=600)

        def next_step():
            self.destroy()

        self.root.after(2000, next_step)

    def destroy(self):
        self.step4_frame.destroy()

