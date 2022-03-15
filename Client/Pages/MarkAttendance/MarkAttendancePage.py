from tkinter import *
from Scrollbar import scrollbar
import tkinter as tk
from Eff import Eff
import datetime
from PIL import ImageTk, Image
from ServerSide.SelectOperation import SelectOperation
from tkinter import messagebox
from ServerSide.InsertOperation import InsertOperation

class MarkAttendancePage():
    def __init__(self, parent, data, username):
        self.parent = parent
        self.data = data
        self.username = username
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"
        self.bluePrimColor = "#87A0C4"
        self.presentPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Home_Page_Assets/mark_attandance/Buttons/present.png"
            )
        )
        self.absentAllPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Home_Page_Assets/mark_attandance/Buttons/absentall.png"
            )
        )
        self.undoPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Home_Page_Assets/mark_attandance/Buttons/undo.png"
            )
        )
        self.submitPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Home_Page_Assets/mark_attandance/Buttons/submit.png"
            )
        )

    def draw(self):
        self.frame = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.frame.place(x=0, y=0)

        backButtPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/Buttons/back.png"))
        tilePng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/mark_attandance/tile.png"))

        rawData = SelectOperation().getStudentAccordingToYear(self.data[4], self.data[2])
        data_length = len(rawData)

        rawCurrentDate = str(datetime.date.today())
        currentDate = rawCurrentDate.split("-")

        dateLabel = Label(self.frame, text=f"Date :- {currentDate[2]}-{currentDate[1]}-{currentDate[0]}", fg="black",
                          bg=self.ligBluePrimColor,
                          bd=0, font=(self.font, 12, "normal"))
        dateLabel.place(x=300, y=15)

        headingFrame = Frame(self.frame, bg=self.ligBluePrimColor, width=730, height=55)
        headingFrame.place(x=0, y=40)

        margin = Label(headingFrame, bd=0, bg=self.ligBluePrimColor)
        margin.grid(row=0, column=0, padx=370)

        heading = Label(headingFrame, bg=self.ligBluePrimColor, bd=0, fg="black",
                        text=f"{self.data[0]} {self.data[1]} {self.data[2]}{Eff(int(self.data[2])).get()} Year",
                        font=(self.font, 25, 'normal'), justify="center")
        heading.grid(row=0, column=0, sticky='')

        countLabel = Label(self.frame, bg=self.ligBluePrimColor, bd=0, fg="black",
                        text="",
                        font=(self.font, 20, 'normal'), justify="center")
        countLabel.place(x=20, y=470)

        canvas = tk.Canvas(self.frame, bg=self.ligBluePrimColor, bd=0, width=730, height=360,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=360)

        self.scrol = scrollbar(canvas, canvas, height=153)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=100)

        presentStudent = []

        def updateCount():
            countLabel.config(text=f"{len(presentStudent)} / {data_length}")

        def present(aid, undoButton, presentButton):
            presentStudent.append(aid)
            undoButton.config(state="active")
            presentButton.config(state="disabled")
            updateCount()

        def undo(aid, undoButton, presentButton):
            presentStudent.remove(aid)
            undoButton.config(state="disabled")
            presentButton.config(state="active")
            updateCount()

        def draw_tile(row, data):
            t = Label(content_frame, bd=0, bg=self.ligBluePrimColor, image=tilePng)
            t.photo = tilePng
            t.grid(row=row, column=0, columnspan=4, padx=20, pady=10)

            aid = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="black", text=data[0], font=(self.font, 15, 'normal'))
            aid.grid(row=row, column=0)

            name = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="black", text=data[1],
                        font=(self.font, 15, 'normal'))
            name.grid(row=row, column=1)

            ub = Button()

            ab = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.presentPng, command=lambda: present(data[0], ub, ab))
            ab.photo = self.presentPng
            ab.grid(row=row, column=2)

            ub = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.undoPng, state="disabled", command=lambda: undo(data[0], ub, ab))
            ub.photo = self.undoPng
            ub.grid(row=row, column=3)

        if data_length > 0:
            row=0
            for data in rawData:
                draw_tile(row, data)
                row+=1

            countLabel.config(text=f"0 / {data_length}")

            presentAllButt = Button(self.frame, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                                image=self.absentAllPng)
            presentAllButt.photo = self.absentAllPng
            presentAllButt.place(x=425, y=475)

            print(self.data)
            def submit():
                if len(presentStudent) > 0:
                    teacher_id = SelectOperation().getTeacherId(self.username)
                    print(presentStudent)
                    InsertOperation().insertAttendance(rawData, presentStudent, self.data[4], self.data[2], teacher_id, self.data[3])
                else:
                    messagebox.showerror(title="No Data", message="Mark Attendance First !")

            submitButt = Button(self.frame, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                              image=self.submitPng, command=submit)
            submitButt.photo = self.submitPng
            submitButt.place(x=590, y=475)

        def back():
            self.destroy()

        backButt = Button(self.frame, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor, image=backButtPng, command=back)
        backButt.photo = backButtPng
        backButt.place(x=10, y=10)

    def destroy(self):
        self.frame.destroy()
