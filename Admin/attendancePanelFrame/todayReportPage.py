from tkinter import *
import tkinter as tk
from PIL import ImageTk
from Scrollbar import scrollbar
import datetime
from ServerSide.SelectOperation import SelectOperation

class TodayReportPage():
    def __init__(self, parent):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"

    def draw(self):
        textColor = "#0F4189"
        horizontalDivider = ImageTk.PhotoImage(file=("Assets/horizontalDivider.png"))
        refreshButPng = ImageTk.PhotoImage(file=("Assets/Home_Page_Assets/todaypanel/refreshbutton.png"))

        rawData = SelectOperation().todayAttendanceReport()

        message = Label(self.parent, text=f"Students : {SelectOperation().todayTotalPresentReport()}/{SelectOperation().getTotalStudentCount()}",
                        bg=self.ligBluePrimColor, bd=0, font=(self.font, 15, 'normal'), justify="center")
        message.place(x=290, y=7)

        def refresh():
            self.draw()

        refreshBut = Button(self.parent, bd=0, bg=self.ligBluePrimColor,
                            activebackground=self.ligBluePrimColor, image=refreshButPng, command=refresh)
        refreshBut.photo = refreshButPng
        refreshBut.place(x=650, y=5)

        canvas = tk.Canvas(self.parent, bg=self.ligBluePrimColor, bd=0, width=730, height=485,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=485)

        scrol = scrollbar(canvas, canvas, height=215)
        scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrol.get().set)

        canvas.place(x=0, y=40)

        row = 0

        date = Label(content_frame, text=f"Date:-{datetime.date.today()}",
                     bg=self.ligBluePrimColor, bd=0, font=(self.font, 15, 'normal'), justify="center")
        date.grid(row=row, columnspan=5, padx=300, pady=10)

        for data in rawData:
            Label(content_frame, text=data[0], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 25, 'bold'),
                  justify="center").grid(row=row + 1, columnspan=5, padx=200, pady=20)

            Label(content_frame, text="Present", fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'),
                  justify="center").grid(row=row + 2, column=0, pady=12, padx=70)

            Label(content_frame, text=data[1], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 3, column=0)

            Label(content_frame, text="Absent", fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'),
                  justify="center").grid(row=row + 2, column=1, padx=70)

            Label(content_frame, text=data[2], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 3, column=1)

            Label(content_frame, text="Total", fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 2, column=2, padx=70)

            Label(content_frame, text=data[3], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 3, column=2)

            horizontalbar = Label(content_frame, bg=self.ligBluePrimColor, bd=0, image=horizontalDivider)
            horizontalbar.photo = horizontalDivider
            horizontalbar.grid(row=row + 4, columnspan=5, pady=40)

            row += 4