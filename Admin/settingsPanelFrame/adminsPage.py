from tkinter import *
import tkinter as tk
from Scrollbar import scrollbar
from PIL import ImageTk, Image

class AdminsPage():
    def __init__(self, parent):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.textColor = "#0F4189"
        self.font = "Bahnschrift"
        self.tilePng = self.cardPng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/tile.png"))
        self.removePng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/buttons/remove.png"))
        self.blockPng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/buttons/block.png"))
        self.unblockPng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/buttons/unblock.png"))

    def draw(self):
        canvas = tk.Canvas(self.parent, bg=self.ligBluePrimColor, bd=0, width=730, height=520,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=520)

        self.scrol = scrollbar(canvas, canvas, height=235)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=0)

        def blockUnblock(button):
            button.config(image=self.unblockPng)
            button.photo = self.unblockPng

        def drawTile(row, user):
            t = Label(content_frame, bd=0, bg=self.ligBluePrimColor, image=self.tilePng)
            t.photo = self.tilePng
            t.grid(row=row, columnspan=3, pady=10, padx=20)

            l = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="black", text=user, font=(self.font, 15, 'normal'))
            l.grid(row=row, column=0, sticky='w', padx=30)

            b1 = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.blockPng, justify="right", command= lambda :blockUnblock(b1))
            b1.photo = self.blockPng
            b1.grid(row=row, column=1, sticky='e')

            b2 = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor,
                        image=self.removePng, justify="right")
            b2.photo = self.removePng
            b2.grid(row=row, column=2, sticky='e', padx=30)

        row=0
        for i in range(0, 11):
            drawTile(row, f"User{i}")
            row+=1
