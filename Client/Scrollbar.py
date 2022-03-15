from tkinter import ttk
from tkinter import *

class scrollbar():
    def __init__(self, on, scroll, height=185, hp=710):
        self.on = on
        self.scroll = scroll
        self.height = height
        self.hp = hp

    def draw(self):
        self.scrollbar = ttk.Scrollbar(self.on, orient=VERTICAL, command=self.scroll.yview)
        self.scrollbar.grid(ipady=self.height, padx=self.hp)

    def redraw(self):
        self.scrollbar.grid(ipady=self.hp, padx=self.height)

    def destroy(self):
        self.scrollbar.grid_remove()

    def get(self):
        return self.scrollbar