from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from Admin.searchPanelFrames.step3 import SearchStep3

class SearchStep2():
    def __init__(self, parent, grandParent, parentScroll, day, month, year, course):
        # self.parentScroll = parentScroll
        self.parent = parent
        self.grandParent = grandParent
        self.day = day
        self.month = month
        self.year = year
        self.course = course
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"
        self.primaryTextColor = "#0F4189"
        # self.parentScroll.destroy()

    def draw(self):
        self.step2 = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.step2.place(x=0, y=0)

        backButtPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/searchpanel/buttons/back.png"))

        dateLabel = Label(self.step2, text=f"Search result of {self.day}-{self.month}-{self.year}", fg="black",
                                  bg=self.ligBluePrimColor,
                                  bd=0, font=(self.font, 12, "normal"))
        dateLabel.place(x=300, y=15)

        canvas = tk.Canvas(self.step2, bg=self.ligBluePrimColor, bd=0, width=730, height=470,
                                   highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=470)
            # content_frame = ttk.Frame(canvas)

        self.scrollbar = ttk.Scrollbar(self.grandParent, orient=VERTICAL, command=canvas.yview)
        self.scrollbar.grid(ipady=300, padx=1060)

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrollbar.set)

        canvas.place(x=0, y=50)

        detail = Label(content_frame, bg=self.ligBluePrimColor, text=self.course[0], fg="black", bd=0, font=(self.font, 20, 'normal'))
        detail.grid(row=0, column=0, padx=300)

        def drawButton(data, row):
            eff = ""
            if data == 1:
                eff = "st"
            elif data == 2:
                eff = "nd"
            elif data == 3:
                eff = "rd"
            elif data >= 4:
                eff = "th"

            l = Label(content_frame, bd=0, bg=self.ligBluePrimColor, text=f"{data}{eff}", fg=self.primaryTextColor,
                      font=(self.font, 20, "bold"))
            l.grid(row=row, column=0, padx=280, pady=20)
            l.bind("<Button-1>", lambda e: SearchStep3(self.parent, self.grandParent, self.day, self.month, self.year, self.course[0], data, eff).draw())

        row = 1
        for i in range(1, self.course[1]+1):
            drawButton(i, row)
            row += 1

        def back2():
            self.scrollbar.destroy()
            self.destroy()
            # self.parentScroll.redraw()
            # self.parentScroll.redraw()
            #from Admin.searchPanelFrames.step1 import SearchStep1
            #SearchStep1(parent=self.parent, grandParent=self.grandParent, day=self.day, month=self.month, year=self.year)

        backButt = Button(self.step2, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                              image=backButtPng, command=back2)
        backButt.photo = backButtPng
        backButt.place(x=10, y=10)

    def destroy(self):
        self.step2.destroy()