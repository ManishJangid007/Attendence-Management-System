from tkinter import *
import tkinter as tk
from Admin.Scrollbar import scrollbar
from PIL import ImageTk, Image
from Admin.searchPanelFrames.step4 import SearchStep4

class SearchStep3():
    def __init__(self, parent, day, month, year, course, courseYear, eff):
        self.parent = parent
        # self.grandParent = grandParent
        self.day = day
        self.month = month
        self.year = year
        self.course = course
        self.courseYear = courseYear
        self.eff = eff
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"
        self.primaryTextColor = "#0F4189"

    def draw(self):
        self.step3 = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.step3.place(x=0, y=0)

        backButtPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/searchpanel/buttons/back.png"))

        dateLabel = Label(self.step3, text=f"Search result of {self.day}-{self.month}-{self.year}", fg="black",
                                      bg=self.ligBluePrimColor,
                                      bd=0, font=(self.font, 12, "normal"))
        dateLabel.place(x=300, y=15)

        rawData = ["C++", "Java", "Java Script", "C", "Computer Graphics", "DBMS", "Python"]

        canvas = tk.Canvas(self.step3, bg=self.ligBluePrimColor, bd=0, width=730, height=470,
                                       highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=470)
            # content_frame = ttk.Frame(canvas)

        # self.scrollbar = ttk.Scrollbar(self.grandParent, orient=VERTICAL, command=canvas.yview)
        # self.scrollbar.grid(ipady=300, padx=1060)

        self.scrol1 = scrollbar(canvas, canvas, height=210)
        self.scrol1.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol1.get().set)

        canvas.place(x=0, y=50)

        detail = Label(content_frame, bg=self.ligBluePrimColor, text=f"{self.course} {self.courseYear}{self.eff} Year", fg="black", bd=0,
                                   font=(self.font, 20, 'normal'))
        detail.grid(row=0, column=0, padx=300)

        def drawButton(data, row):
            l = Label(content_frame, bd=0, bg=self.ligBluePrimColor, text=data, fg=self.primaryTextColor,
                          font=(self.font, 20, "bold"))
            l.grid(row=row, column=0, padx=280, pady=20)
            l.bind("<Button-1>", lambda e: SearchStep4(parent=self.parent, day=self.day, month=self.month, year=self.year, course=self.course, courseYear=self.courseYear, eff=self.eff, subject=data).draw())

        row = 1
        for data in rawData:
            drawButton(data, row)
            row += 1

        def back3():
            self.destroy()
            # parent1.destroy()

        backButt = Button(self.step3, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                                      image=backButtPng, command=back3)
        backButt.photo = backButtPng
        backButt.place(x=10, y=10)

    def destroy(self):
        self.scrol1.destroy()
        self.step3.destroy()
