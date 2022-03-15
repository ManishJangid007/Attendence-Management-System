from tkinter import *
from Scrollbar import scrollbar
import tkinter as tk
import datetime

class MarkAttendancePage():
    def __init__(self, parent, subject, course, year, username):
        self.parent = parent
        self.subject = subject
        self.course = course
        self.year = year
        self.username = username
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"

    def draw(self):
        self.frame = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.frame.place(x=0, y=0)

        rawCurrentDate = str(datetime.date.today())
        currentDate = rawCurrentDate.split("-")

        dateLabel = Label(self.frame, text=f"Date :- {currentDate[2]}-{currentDate[1]}-{currentDate[0]}", fg="black",
                          bg=self.ligBluePrimColor,
                          bd=0, font=(self.font, 12, "normal"))
        dateLabel.place(x=300, y=15)

        headingFrame = Frame(self.frame, bg="red", width=730, height=55)
        headingFrame.place(x=0, y=40)

        heading = Label(headingFrame, bg=self.ligBluePrimColor, bd=0, fg="black",
                        text=f"{self.subject} {self.course} {self.year} Year",
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