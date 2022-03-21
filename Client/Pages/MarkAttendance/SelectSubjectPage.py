from tkinter import *
import tkinter as tk
from Scrollbar import scrollbar
from PIL import ImageTk, Image
import datetime
from tkinter import messagebox
from ServerSide.SelectOperation import SelectOperation
from Eff import Eff
from Pages.MarkAttendance.MarkAttendancePage import MarkAttendancePage

class SelectSubjectPage():
    def __init__(self, parent, username):
        self.parent = parent
        self.username = username
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"
        self.secondaryTextColor = "#474545"
        self.orangePrimColor = "#FF8C64"
        self.primaryTextColor = "#0F4189"
        self.refreshButPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Home_Page_Assets/Buttons/refreshbutton.png"
            )
        )

    def draw(self):
        self.frame = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.frame.place(x=0, y=0)

        rawCurrentDate = str(datetime.date.today())
        currentDate = rawCurrentDate.split("-")

        dateLabel = Label(self.frame, text=f"Date :- {currentDate[2]}-{currentDate[1]}-{currentDate[0]}", fg="black",
                          bg=self.ligBluePrimColor,
                          bd=0, font=(self.font, 12, "normal"))
        dateLabel.place(x=300, y=15)

        refreshBut = Button(self.frame, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                            image=self.refreshButPng, command=self.refresh)
        refreshBut.photo = self.refreshButPng
        refreshBut.place(x=620, y=12)

        selectLabel = Label(self.frame, text="Select a", fg=self.secondaryTextColor, bg=self.ligBluePrimColor,
                            bd=0, font=(self.font, 25, "normal"))
        selectLabel.place(x=250, y=50)

        subjectLabel = Label(self.frame, text="Subject", fg=self.orangePrimColor, bg=self.ligBluePrimColor,
                            bd=0, font=(self.font, 25, "normal"))
        subjectLabel.place(x=380, y=50)

        canvas = tk.Canvas(self.frame, bg=self.ligBluePrimColor, bd=0, width=730, height=420,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=420)

        self.scrol = scrollbar(canvas, canvas)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=100)

        margin = Label(content_frame, bd=0, bg=self.ligBluePrimColor)
        margin.grid(row=0, column=0, padx=370)

        date = f"{currentDate[2]}-{currentDate[1]}-{currentDate[0]}"
        def select(data, username):
            if SelectOperation().checkSubjectAttendance(date, data[3]):
                messagebox.showinfo(title="Already Exist", message="You Already Marked Attendance Successfully")
            else:
                MarkAttendancePage(self.parent, data, username).draw()

        def drawTile(row, data):
            if SelectOperation().checkSubjectAttendance(date, data[3]):
                l = Label(content_frame, bd=0, bg=self.ligBluePrimColor, text=f"'{data[0]}'    {data[1]} {data[2]}{(Eff(int(data[2])).get())} Year", fg="#0F9D58",
                          font=(self.font, 20, "bold"))
                l.grid(row=row, column=0, pady=10)
                # l.bind("<Button-1>", lambda e: select(data, self.username))
            else:
                l = Label(content_frame, bd=0, bg=self.ligBluePrimColor,
                          text=f"'{data[0]}'    {data[1]} {data[2]}{(Eff(int(data[2])).get())} Year",
                          fg=self.primaryTextColor,
                          font=(self.font, 20, "bold"))
                l.grid(row=row, column=0, pady=10)
                l.bind("<Button-1>", lambda e: select(data, self.username))

        rawData = SelectOperation().getSubjectAccordingToTeacher(self.username)

        if len(rawData) > 0:
            row = 1
            for data in rawData:
                drawTile(row, data)
                row+=1

        else:
            empty = Label(content_frame, bd=0, bg=self.ligBluePrimColor, text="It's Empty Here", fg=self.primaryTextColor,
                      font=(self.font, 20, "bold"))
            empty.grid(row=1, column=0, padx=10)

    def refresh(self):
        self.frame.destroy()
        self.draw()