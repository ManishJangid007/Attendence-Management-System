from tkinter import *
import tkinter as tk
from Scrollbar import scrollbar
from PIL import ImageTk, Image

class SearchResultPage():
    def __init__(self, parent, course, year):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"
        self.course = course
        self.year = year
        self.backButPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/buttons/back.png"))
        self.cardPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/card.png"))
        self.viewPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/buttons/view.png"))
        self.eff = "st"
        if year == 2:
            self.eff = "nd"
        elif year == 3:
            self.eff = "rd"
        elif year >= 4:
            self.eff = "th"

    def draw(self):
        self.searchResultFrame = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.searchResultFrame.place(x=0, y=0)

        hCourse = Label(self.searchResultFrame, bd=0, bg=self.ligBluePrimColor, text=f"{self.course} {self.year}{self.eff}", fg="black", font=(self.font, 20, 'normal'), justify="center")
        hCourse.place(x=70, y=9)

        canvas = tk.Canvas(self.searchResultFrame, bg=self.ligBluePrimColor, bd=0, width=730, height=470,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=470)

        self.scrol = scrollbar(canvas, canvas, height=210)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=50)

        def drawCard(row, col, id, firstname, lastname):
            c = Label(content_frame, bd=0, bg=self.ligBluePrimColor, image=self.cardPng)
            c.photo = self.cardPng
            c.grid(row=row, column=col, rowspan=4, padx=25, pady=10)

            id = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="white", text=id, font=(self.font, 15, 'normal'))
            id.grid(row=row, column=col)

            fn = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="white", text=firstname, font=(self.font, 15, 'normal'))
            fn.grid(row=row+1, column=col)

            ln = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="white", text=lastname,
                       font=(self.font, 15, 'normal'))
            ln.grid(row=row + 2, column=col)

            bt = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.viewPng)
            bt.photo = self.viewPng
            bt.grid(row=row+3, column=col)


        row = 0
        col = 0
        for i in range(0, 101):
            drawCard(row, col, f"aryaid{i}", "firstname", "lastname")
            col += 1
            if col > 2:
                col = 0
            if col == 0:
                row += 4

        def back():
            self.destroy()

        backButt = Button(self.searchResultFrame, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                          image=self.backButPng, command=back)
        backButt.photo = self.backButPng
        backButt.place(x=10, y=10)

    def destroy(self):
        self.searchResultFrame.destroy()