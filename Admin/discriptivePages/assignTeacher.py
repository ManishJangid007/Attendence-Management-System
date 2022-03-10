from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from Scrollbar import scrollbar
from ServerSide.SelectOperation import SelectOperation

class AssignTeacherPage():
    def __init__(self, parent, course, year, subject):
        self.parent = parent
        self.course = course
        self.year = year
        if self.year == 1:
            self.eff = "st"
        elif self.year == 2:
            self.eff = "nd"
        elif self.year == 3:
            self.eff = "rd"
        elif self.year >= 4:
            self.eff = "th"
        self.subject = subject
        self.backPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/back.png"
            )
        )
        self.assignPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/assign.png"
            )
        )
        self.dividerPng = ImageTk.PhotoImage(Image.open("Assets/longHorizontalDivider.png"))
        self.orangePrimColor = "#FF8C64"
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"

    def draw(self):
        self.assignTFrame = Frame(self.parent, bd=0, bg="white", width=1080, height=650)
        self.assignTFrame.place(x=0, y=0)

        headingLabel = Label(self.assignTFrame, text=f"{self.course} {self.year}{self.eff} Year", bg="white", fg=self.orangePrimColor,
                            font=(self.font, 30, 'normal'))
        headingLabel.place(x=80, y=8)

        subHeading = Label(self.assignTFrame, text=f"Assign Teacher For '{self.subject}'", bg="white", fg="black",
                            font=(self.font, 20, 'normal'))
        subHeading.place(x=80, y=70)

        canvas = tk.Canvas(self.assignTFrame, bg="white", bd=0, width=1080, height=530,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg="white", width=1080, height=530)

        self.scrol = scrollbar(canvas, canvas, height=240, hp=1061)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=120)

        rawTeacherList = SelectOperation().getTeacherBasicInfo()

        def assign(tid):
            print(self.course)
            print(self.year)
            print(self.subject)
            print(tid)
            self.parent.destroy()
            self.destroy()


        def drawTile(row, sn, username, teacher_name, tid):
            s = Label(content_frame, bd=0, bg="white", fg="black", text=f"{sn}.", font=(self.font, 20, 'normal'))
            s.grid(row=row, column=0, pady=10)

            u = Label(content_frame, bd=0, bg="white", fg="black", text=username, font=(self.font, 20, 'normal'))
            u.grid(row=row, column=1, pady=10)

            n = Label(content_frame, bd=0, bg="white", fg="black", text=teacher_name, font=(self.font, 20, 'normal'))
            n.grid(row=row, column=2, pady=10)

            b = Button(content_frame, bd=0, bg="white", activebackground="white", image=self.assignPng, command=lambda:assign(tid))
            b.photo = self.assignPng
            b.grid(row=row, column=3, pady=10)

            d = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
            d.photo = self.dividerPng
            d.grid(row=row+1, columnspan=4, padx=10, pady=10)

        row = 0
        sn = 1
        for data in rawTeacherList:
            drawTile(row, sn, data[0], data[1], data[2])
            row += 2
            sn += 1

        def back():
            self.destroy()

        backBut = Button(self.assignTFrame, bd=0, bg="white", activebackground="white", image=self.backPng, command=back)
        backBut.photo = self.backPng
        backBut.place(x=20, y=20)

    def destroy(self):
        self.assignTFrame.destroy()

