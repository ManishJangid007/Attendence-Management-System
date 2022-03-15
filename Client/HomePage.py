from tkinter import *
from PIL import ImageTk, Image

class HomePage():
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.backgroundPng = ImageTk.PhotoImage(file=("Assets/Home_Page_Assets/background.png"))
        self.ligBluePrimColor = "#F2F8FF"

    def draw(self):
        self.home_page_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.home_page_frame.place(x=0, y=0)

        self.background = Label(self.home_page_frame, bg="white", bd=0, image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=12, y=5)

        self.mark_attendance_panel = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.mark_attendance_panel.place(x=323, y=103)
