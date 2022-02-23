from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from Admin.Scrollbar import scrollbar

class SearchStep4():
    def __init__(self, parent, day, month, year, course, courseYear, eff, subject):
        self.parent = parent
        self.day = day
        self.month = month
        self.year = year
        self.course = course
        self.courseYear = courseYear
        self.eff = eff
        self.subject = subject
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"
        self.primaryTextColor = "#0F4189"

    def draw(self):
        self.step4 = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.step4.place(x=0, y=0)

        backButtPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/searchpanel/buttons/back.png"))

        dateLabel = Label(self.step4, text=f"Search result of {self.day}-{self.month}-{self.year}", fg="black",
                          bg=self.ligBluePrimColor,
                          bd=0, font=(self.font, 12, "normal"))
        dateLabel.place(x=300, y=15)

        canvas = tk.Canvas(self.step4, bg=self.ligBluePrimColor, bd=0, width=730, height=470,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=470)

        scrol = scrollbar(canvas, canvas)
        scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrol.get().set)

        canvas.place(x=0, y=50)

        detail = Label(content_frame, bg=self.ligBluePrimColor, text=f"{self.course} {self.courseYear}{self.eff} Year\n{self.subject}",
                       fg="black", bd=0,
                       font=(self.font, 20, 'normal'))
        detail.grid(row=0, column=0, padx=300)

        def back4():
            self.destroy()

        backButt = Button(self.step4, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                          image=backButtPng, command=back4)
        backButt.photo = backButtPng
        backButt.place(x=10, y=10)

    def destroy(self):
        self.step4.destroy()