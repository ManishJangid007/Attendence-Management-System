from tkinter import *
import tkinter as tk
from Scrollbar import scrollbar
from PIL import ImageTk, Image

class CourseListPage():
    def __init__(self, parent):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"
        self.viewButPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/coursepanel/buttons/view.png"))
        self.cardPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/coursepanel/card.png"))

    def draw(self):
        rawData = [["BCA", 3],
                   ["BBA", 3],
                   ["MBA", 2],
                   ["MCA", 2],
                   ["PGDCA", 2],
                   ["Fashion Designing", 1],
                   ["Interior Designing", 4],
                   ["B.Com", 3],
                   ["M.Com", 2],
                   ["B.Tech", 3],
                   ["M.Tech", 5],
                   ["Hotel Management", 3],
                   ["Akajsbkjb Ajsdbhskjbv, aihsgfshjkdb", 4]]

        canvas = tk.Canvas(self.parent, bg=self.ligBluePrimColor, bd=0, width=730, height=520,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=520)

        self.scrol = scrollbar(canvas, canvas, height=235)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=0)
        # course, year

        def view(course):
            print(course)

        def drawCard(row, col, course, year):
            c = Label(content_frame, bd=0, bg=self.ligBluePrimColor, image=self.cardPng)
            c.photo = self.cardPng
            c.grid(rowspan=3, row=row, column=col, padx=25, pady=5)

            l1 = Label(content_frame, bd=0, bg=self.bluePrimColor, wraplength=200, fg="white", text=course, font=(self.font, 20, 'normal'))
            l1.grid(row=row, column=col)

            l2 = Label(content_frame, bd=0, bg=self.bluePrimColor, wraplength=200, fg="white", text=f"{year} Year", font=(self.font, 20, 'normal'))
            l2.grid(row=row+1, column=col)

            b = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.viewButPng, command=lambda : view(course))
            b.photo = self.viewButPng
            b.grid(row=row+2, column=col, pady=5)


        row = 0
        col = 0
        for data in rawData:
            drawCard(row, col, data[0], data[1])
            col += 1
            if col > 2:
                col = 0
                row += 3
