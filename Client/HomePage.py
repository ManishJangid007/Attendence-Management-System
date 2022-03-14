from tkinter import *

class HomePage():
    def __init__(self, root, username):
        self.root = root
        self.username = username

    def draw(self):
        self.home_page_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.home_page_frame.place(x=0, y=0)