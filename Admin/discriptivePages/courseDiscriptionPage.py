from tkinter import *
import tkinter as tk
from tkinter import messagebox
from Scrollbar import scrollbar
from PIL import ImageTk, Image
from discriptivePages.assignTeacher import AssignTeacherPage
from ServerSide.SelectOperation import SelectOperation
from ServerSide.UpdateOperation import UpdateOperation
from ReturnEff import eff

class CourseDisPage():
    def __init__(self, parent, course, year):
        self.parent = parent
        self.course = course
        self.year = year
        self.textColor = "#0F4189"
        self.closePng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/close.png"
            )
        )
        self.assignTeacherPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/assignteacher.png"
            )
        )
        self.tile = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/yeartile.png"
            )
        )
        self.deletePng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/delete.png"
            )
        )
        self.dividerPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/longHorizontalDivider.png"
            )
        )
        self.orangePrimColor = "#FF8C64"
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"

    def draw(self):
        self.courseFrame = Frame(self.parent, bd=0, bg="white", height=650, width=1080)
        self.courseFrame.place(x=0, y=0)

        courseLabel = Label(self.courseFrame, text=self.course, bg="white", fg=self.orangePrimColor, font=(self.font, 30, 'normal'))
        courseLabel.place(x=80, y=8)

        canvas = tk.Canvas(self.courseFrame, bg="white", bd=0, width=1080, height=580,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg="white", width=1080, height=580)

        self.scrol = scrollbar(canvas, canvas, height=265, hp=1061)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=70)

        global row

        row = 0

        def assignTeacher(course, year, subject):
            AssignTeacherPage(self.courseFrame, course, year, subject).draw()

        def deleteSubject(year, subject):
            if messagebox.askyesno(title="Warning !", message="This action can't be undone this will affect your data, Are You Sure"):
                if UpdateOperation().deleteSubject(self.course, str(year), subject):
                    self.destroy()
                    self.draw()
                    messagebox.showinfo(title="Success", message="Subject Deleted Successfully !")

        def drawSubject(row, sn, subject, teacher, year):
            s = Label(content_frame, text=f"{sn}.", bd=0, bg="white", fg="black", font=(self.font, 20, 'normal'))
            s.grid(row=row, column=0, pady=10)

            l1 = Label(content_frame, text=subject, bd=0, bg="white", fg="black", font=(self.font, 20, 'normal'))
            l1.grid(row=row, column=1, pady=10)

            l2 = Label(content_frame, text=teacher, bd=0, bg="white", fg="black", font=(self.font, 20, 'normal'))
            l2.grid(row=row, column=2, pady=10)

            r = Button(content_frame, bd=0, bg="white", activebackground="white", image=self.deletePng, command=lambda: deleteSubject(year, subject))
            r.photo = self.deletePng
            r.grid(row=row, column=3, pady=10)

            b = Button(content_frame, bd=0, bg="white", activebackground="white", image=self.assignTeacherPng, command= lambda : assignTeacher(self.course, year, subject))
            b.photo = self.assignTeacherPng
            b.grid(row=row, column=4, pady=10, padx=40)

            d = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
            d.photo = self.dividerPng
            d.grid(row=row + 1, pady=10, columnspan=5)

        def drawYear(r, year):
            eff = ""
            if year == 1:
                eff = "st"
            if year == 2:
                eff = "nd"
            if year == 3:
                eff = "rd"
            if year >= 4:
                eff = "th"

            t = Label(content_frame, bg="white", bd=0, image=self.tile)
            t.photo = self.tile
            t.grid(row=r, columnspan=5)

            l = Label(content_frame, text=f"{year}{eff} Year", bd=0, bg=self.textColor, fg="white", font=(self.font, 25, 'normal'))
            l.grid(row=r, columnspan=5, padx=500, pady=10)

            rawSubject = SelectOperation().getTeacherAccordingToCourse(year, self.course)

            global row

            row+=1
            sn = 1
            if len(rawSubject) > 0:
                for data in rawSubject:
                    drawSubject(row, sn, data[0], data[1], year)
                    sn += 1
                    row+=2
            else:
                l = Label(content_frame, bg="white", bd=0, fg="black",
                          text=f"Please Add Some Subject in {year}{eff} Year", font=(self.font, 17, 'normal'))
                l.grid(row=row, columnspan=5, pady=10)

        for i in range(1, self.year+1):
            drawYear(row, i)
            row+=1

        def close():
            self.destroy()
        closeBut = Button(self.courseFrame, bg="white", bd=0, activebackground="white", image=self.closePng, command=close)
        closeBut.place(x=20, y=20)

    def destroy(self):
        self.courseFrame.destroy()
