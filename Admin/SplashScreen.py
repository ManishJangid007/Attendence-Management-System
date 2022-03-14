from tkinter import *
from PIL import ImageTk, Image
import random

class SplashScreen():
    def __init__(self, parent):
        self.parent = parent
        self.images = ["Assets/Splash_Screens/sp1.png",
                          "Assets/Splash_Screens/sp2.png",
                          "Assets/Splash_Screens/sp3.png",
                          "Assets/Splash_Screens/sp4.png",
                          "Assets/Splash_Screens/sp5.png",
                          "Assets/Splash_Screens/sp6.png",
                          "Assets/Splash_Screens/sp7.png",
                          "Assets/Splash_Screens/sp8.png",
                          "Assets/Splash_Screens/sp9.png",
                          "Assets/Splash_Screens/sp10.png",
                          "Assets/Splash_Screens/sp11.png",
                          "Assets/Splash_Screens/sp12.png",
                          "Assets/Splash_Screens/sp13.png",
                          "Assets/Splash_Screens/sp14.png"]
        self.backgroundPng = ImageTk.PhotoImage(
            Image.open(
                self.images[random.randrange(0, 14)]
            )
        )
        self.orangePrimColor = "#FF8C64"
        self.font = "Bahnschrift"
        self.blueText = "#0F4189"
        self.greyText = "#4C4C4C"

    def draw(self):
        self.spFrame = Frame(self.parent, bg="white", width=1080, height=650)
        self.spFrame.place(x=0, y=0)

        background = Label(self.spFrame, bd=0, bg="white", image=self.backgroundPng)
        background.photo = self.backgroundPng
        background.place(x=12, y=5)

        l1 = Label(self.spFrame, bd=0, bg="white", text="Attendance", fg=self.orangePrimColor, font=(self.font, 45, 'normal'))
        l1.place(x=30, y=170)

        l2 = Label(self.spFrame, bd=0, bg="white", text="Management", fg=self.blueText,
                   font=(self.font, 40, 'normal'))
        l2.place(x=30, y=250)

        l3 = Label(self.spFrame, bd=0, bg="white", text="System !", fg=self.blueText,
                   font=(self.font, 40, 'normal'))
        l3.place(x=30, y=330)

        l4 = Label(self.spFrame, bd=0, bg="white", text="Loading Please Wait...", fg=self.greyText,
                   font=(self.font, 20, 'normal'))
        l4.place(x=780, y=590)

        dev = Label(self.spFrame, bd=0, bg="white", text="Dev.User.V1.0.0", fg=self.greyText,
                   font=(self.font, 20, 'normal'))
        dev.place(x=30, y=590)

    def destroy(self):
        self.spFrame.destroy()
