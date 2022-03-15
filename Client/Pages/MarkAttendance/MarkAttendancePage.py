from tkinter import *
from Scrollbar import scrollbar
import tkinter as tk
from Eff import Eff
import datetime
from PIL import ImageTk, Image

class MarkAttendancePage():
    def __init__(self, parent, data, username):
        self.parent = parent
        self.data = data
        self.username = username
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"
        self.bluePrimColor = "#87A0C4"

    def draw(self):
        self.frame = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.frame.place(x=0, y=0)

        backButtPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/Buttons/back.png"))
        tilePng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/mark_attandance/tile.png"))

        rawCurrentDate = str(datetime.date.today())
        currentDate = rawCurrentDate.split("-")

        dateLabel = Label(self.frame, text=f"Date :- {currentDate[2]}-{currentDate[1]}-{currentDate[0]}", fg="black",
                          bg=self.ligBluePrimColor,
                          bd=0, font=(self.font, 12, "normal"))
        dateLabel.place(x=300, y=15)

        headingFrame = Frame(self.frame, bg=self.ligBluePrimColor, width=730, height=55)
        headingFrame.place(x=0, y=40)

        margin = Label(headingFrame, bd=0, bg=self.ligBluePrimColor)
        margin.grid(row=0, column=0, padx=370)

        heading = Label(headingFrame, bg=self.ligBluePrimColor, bd=0, fg="black",
                        text=f"{self.data[0]} {self.data[1]} {self.data[2]}{Eff(int(self.data[2])).get()} Year",
                        font=(self.font, 25, 'normal'), justify="center")
        heading.grid(row=0, column=0, sticky='')

        canvas = tk.Canvas(self.frame, bg=self.ligBluePrimColor, bd=0, width=730, height=420,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=420)

        self.scrol = scrollbar(canvas, canvas)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=100)

        def draw_tile(row, data):
            t = Label(content_frame, bd=0, bg=self.ligBluePrimColor, image=tilePng)
            t.photo = tilePng
            t.grid(row=row, column=0, columnspan=4, padx=20, pady=10)

            aid = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="black", text=data[0], font=(self.font, 15, 'normal'))
            aid.grid(row=row, column=0)

        draw_tile(0, "")
        draw_tile(1, "")

        def back():
            self.destroy()

        backButt = Button(self.frame, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor, image=backButtPng, command=back)
        backButt.photo = backButtPng
        backButt.place(x=10, y=10)

    def destroy(self):
        self.frame.destroy()
