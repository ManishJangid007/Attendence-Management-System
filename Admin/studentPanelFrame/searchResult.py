from tkinter import *
import tkinter as tk
from Scrollbar import scrollbar
from PIL import ImageTk, Image
from tkinter import messagebox
from discriptivePages.studentDescriptionPage import StudentDesPage
from ServerSide.SelectOperation import SelectOperation
from ServerSide.UpdateOperation import UpdateOperation

class SearchResultPage():
    def __init__(self, parent, grandParent, course, year):
        self.parent = parent
        self.grandParent = grandParent
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"
        self.course = course
        self.year = year
        self.backButPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/buttons/back.png"))
        self.cardPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/card.png"))
        self.viewPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/buttons/view.png"))
        self.deletePng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/buttons/delete.png"))
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

        def deleteStudent(id):
            if messagebox.askyesno(title="Warning", message="This action can't be undone and you will lose all the data related to this student"):
                if UpdateOperation().deleteStudent(id):
                    self.searchResultFrame.destroy()
                    self.draw()
                    messagebox.showinfo(title="Success", message="Student Deleted Successfully")
                else:
                    messagebox.showerror(title="Error Occurred", message="Something Went Wrong")

        def view(id):
            StudentDesPage(self.grandParent, id).draw()

        def drawCard(row, col, aid, firstname, lastname):
            c = Label(content_frame, bd=0, bg=self.ligBluePrimColor, image=self.cardPng)
            c.photo = self.cardPng
            c.grid(row=row, column=col, rowspan=5, padx=25, pady=10)

            id = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="white", text=aid, font=(self.font, 15, 'normal'))
            id.grid(row=row, column=col, pady=10)

            fn = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="white", text=firstname, font=(self.font, 15, 'normal'))
            fn.grid(row=row+1, column=col)

            ln = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="white", text=lastname,
                       font=(self.font, 15, 'normal'))
            ln.grid(row=row + 2, column=col)

            bt = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.viewPng, command=lambda:view(aid))
            bt.photo = self.viewPng
            bt.grid(row=row+3, column=col)

            d = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor,
                       image=self.deletePng, command=lambda : deleteStudent(id=aid))
            d.photo = self.deletePng
            d.grid(row=row + 4, column=col, pady=15)

        rawData = SelectOperation().getStudentBasicInfo(self.course, self.year)

        if len(rawData) > 0:
            row = 0
            col = 0
            for data in rawData:
                drawCard(row, col, data[0], data[1], data[2])
                col += 1
                if col > 2:
                    col = 0
                if col == 0:
                    row += 5
        else:
            empty = Label(content_frame, bd=0, bg=self.ligBluePrimColor, fg="black", text="It's Empty Here", font=(self.font, 30, 'normal'))
            empty.grid(row=0, column=0, pady=10, padx=100)

        def back():
            self.destroy()

        backButt = Button(self.searchResultFrame, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                          image=self.backButPng, command=back)
        backButt.photo = self.backButPng
        backButt.place(x=10, y=10)

    def destroy(self):
        self.searchResultFrame.destroy()