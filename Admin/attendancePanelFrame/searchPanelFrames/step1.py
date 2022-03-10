from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from attendancePanelFrame.searchPanelFrames.step2 import SearchStep2
from Scrollbar import scrollbar

class SearchStep1():
    def __init__(self, parent, grandParent, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.parent = parent
        self.grandParent = grandParent
        self.font = "Bahnschrift"
        self.ligBluePrimColor = "#F2F8FF"
        self.secondaryTextColor = "#474545"
        self.orangePrimColor = "#FF8C64"
        self.primaryTextColor = "#0F4189"

    def draw(self):
        self.step1 = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.step1.place(x=0, y=0)

        backButtPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/searchpanel/buttons/back.png"))

        dateLabel = Label(self.step1, text=f"Search result of {self.day}-{self.month}-{self.year}", fg="black", bg=self.ligBluePrimColor,
                         bd=0, font=(self.font, 12, "normal"))
        dateLabel.place(x=300, y=15)

        selectLabel = Label(self.step1, text="Select a", fg=self.secondaryTextColor, bg=self.ligBluePrimColor,
                         bd=0, font=(self.font, 25, "normal"))
        selectLabel.place(x=280, y=50)

        courseLabel = Label(self.step1, text="Course", fg=self.orangePrimColor, bg=self.ligBluePrimColor,
                                bd=0, font=(self.font, 25, "normal"))
        courseLabel.place(x=410, y=50)

        rawDataC = ["BCA", "BBA", "PGDCA", "MCA", "MBA", "Fashion Desining", "Interior Desining", "BA", "BCOM", "BSC"]
        rawDataCourse = [["BCA", 3], ["BBA", 3], ["PGDCA", 2], ["MBA", 2], ["Fashion Designing", 1], ["Interior Designing", 1], ["BA", 3], ["BCOM", 3], ["BSC", 3]]

        canvas = tk.Canvas(self.step1, bg=self.ligBluePrimColor, bd=0, width=730, height=420,
                               highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=420)

        self.scrol = scrollbar(canvas, canvas)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=100)

        def drawButton(data, row):
            l = Label(content_frame, bd=0, bg=self.ligBluePrimColor, text=data[0], fg=self.primaryTextColor, font=(self.font, 20, "bold"))
            l.grid(row=row, column=0, padx=280, pady=10)
            l.bind("<Button-1>", lambda e: SearchStep2(parent=self.parent, grandParent=self.grandParent, day=self.day, month=self.month, year=self.year, course=data).draw())

        row = 0
        for data in rawDataCourse:
            drawButton(data, row)
            row += 1

        def back1():
            self.destroy()

        backButt = Button(self.step1, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor, image=backButtPng, command=back1)
        backButt.photo = backButtPng
        backButt.place(x=10, y=10)

    def destroy(self):
        self.scrol.destroy()
        self.step1.destroy()