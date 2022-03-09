from tkinter import *
from PIL import ImageTk, Image
from Scrollbar import scrollbar
import tkinter as tk
import datetime
from discriptivePages.teacherDescriptionPage import TeacherDisPage
from ServerSide.SelectOperation import SelectOperation

class TeacherListPage():
    def __init__(self, parent, grandParent):
        self.parent = parent
        self.grandParent = grandParent
        self.tilePng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/teacherpanel/tile.png"))
        self.profilePng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/teacherpanel/buttons/profile.png"))
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"

    def draw(self):
        canvas = tk.Canvas(self.parent, bg=self.ligBluePrimColor, bd=0, width=730, height=524,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=524)

        scrol = scrollbar(canvas, canvas, height=237)
        scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrol.get().set)

        canvas.place(x=0, y=0)

        date = Label(content_frame, bd=0, bg=self.ligBluePrimColor, fg="black", text=f"Date :- {datetime.date.today()}",
                     font=(self.font, 12, 'normal'))
        date.grid(row=0, columnspan=3, padx=100)

        def view(id, username):
            TeacherDisPage(self.grandParent, self.parent, id, username).draw()

        def drawTile(row, username, name, id):
            tile = Label(content_frame, bd=0, bg=self.ligBluePrimColor, image=self.tilePng)
            tile.photo = self.tilePng
            tile.grid(row=row, columnspan=3, pady=10, padx=20)

            l1 = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="black", text=username,
                       font=(self.font, 15, 'normal'))
            l1.grid(row=row, column=0, padx=30, sticky="w")

            l2 = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="black", text=name,
                       font=(self.font, 15, 'normal'))
            l2.grid(row=row, column=1)

            b2 = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor,
                        image=self.profilePng, command=lambda : view(id, username))
            b2.photo = self.profilePng
            b2.grid(row=row, column=2, padx=30, sticky="e")

        data = SelectOperation().getTeacherBasicInfo()

        row = 1

        for d in data:
            drawTile(row, d[0], d[1], d[2])
            row+=1

