from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from Scrollbar import scrollbar
from tkinter import messagebox
from discriptivePages.editStudentPage import EditStudentPage
from ServerSide.SelectOperation import SelectOperation
from ServerSide.UpdateOperation import UpdateOperation

class StudentDesPage():
    def __init__(self, parent, aryaId):
        self.parent = parent
        self.aryaId = aryaId
        self.orangePrimColor = "#FF8C64"
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"
        self.greyColor = "#606060"
        self.closePng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/close.png"
            )
        )
        self.deleteProfilePng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/deleteprofile.png"
            )
        )
        self.refreshPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/refresh.png"
            )
        )
        self.editPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/edit.png"
            )
        )
        self.generateReportPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/genreport.png"
            )
        )
        self.dividerPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/horizontalDivider.png"
            )
        )
    def draw(self):
        self.studentFrame = Frame(self.parent, bd=0, bg="white", height=650, width=1080)
        self.studentFrame.place(x=0, y=0)

        aryaIdLabel = Label(self.studentFrame, bd=0, bg="white", text=self.aryaId, fg=self.orangePrimColor,
                              font=(self.font, 30, 'normal'))
        aryaIdLabel.place(x=80, y=9)

        canvas = tk.Canvas(self.studentFrame, bg="white", bd=0, width=1080, height=580,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg="white", width=1080, height=580)

        self.scrol = scrollbar(canvas, canvas, height=265, hp=1061)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=70)

        rawData = SelectOperation().getStudentProfile(self.aryaId)

        nameLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Name : {rawData[1]} {rawData[2]}",
                          font=(self.font, 25, 'normal'), justify="right")
        nameLabel.grid(row=0, column=0, pady=20)

        divider = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider.photo = self.dividerPng
        divider.grid(row=1, column=0, padx=350)

        fatherNameLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Father Name : {rawData[3]}",
                          font=(self.font, 25, 'normal'), justify="right")
        fatherNameLabel.grid(row=2, column=0, pady=20)

        divider1 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider1.photo = self.dividerPng
        divider1.grid(row=3, column=0, padx=350)

        motherNameLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Mother Name : {rawData[4]}",
                                font=(self.font, 25, 'normal'), justify="right")
        motherNameLabel.grid(row=4, column=0, pady=20)

        divider2 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider2.photo = self.dividerPng
        divider2.grid(row=5, column=0, padx=350)

        genderLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Gender : {rawData[5]}",
                                font=(self.font, 25, 'normal'), justify="right")
        genderLabel.grid(row=6, column=0, pady=20)

        divider3 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider3.photo = self.dividerPng
        divider3.grid(row=7, column=0, padx=350)

        dobLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Date of Birth : {rawData[6]}",
                            font=(self.font, 25, 'normal'), justify="right")
        dobLabel.grid(row=8, column=0, pady=20)

        divider4 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider4.photo = self.dividerPng
        divider4.grid(row=9, column=0, padx=350)

        ageLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Age : {rawData[7]}",
                         font=(self.font, 25, 'normal'), justify="right")
        ageLabel.grid(row=10, column=0, pady=20)

        divider7 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider7.photo = self.dividerPng
        divider7.grid(row=11, column=0, padx=350)

        phoneLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Phone No. : {rawData[8]}",
                         font=(self.font, 25, 'normal'), justify="right")
        phoneLabel.grid(row=12, column=0, pady=20)

        divider5 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider5.photo = self.dividerPng
        divider5.grid(row=13, column=0, padx=350)

        emailLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Email : {rawData[9]}",
                           font=(self.font, 25, 'normal'), justify="right")
        emailLabel.grid(row=14, column=0, pady=20)

        divider6 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider6.photo = self.dividerPng
        divider6.grid(row=15, column=0, padx=350)

        sessionLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Session : {rawData[11]}",
                           font=(self.font, 25, 'normal'), justify="right")
        sessionLabel.grid(row=16, column=0, pady=20)

        divider8 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider8.photo = self.dividerPng
        divider8.grid(row=17, column=0, padx=350)

        eff = ""
        if int(rawData[10]) == 1:
            eff = "st"
        elif int(rawData[10]) == 2:
            eff = "nd"
        elif int(rawData[10]) == 3:
            eff = "rd"
        elif int(rawData[10]) >= 4:
            eff = "th"

        courseLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Course : {SelectOperation().getCourseName(rawData[12])} {rawData[10]}{eff} Year",
                           font=(self.font, 25, 'normal'), justify="right")
        courseLabel.grid(row=18, column=0, pady=20)

        divider6 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider6.photo = self.dividerPng
        divider6.grid(row=19, column=0, padx=350)

        def generateReport(id):
            print(id)

        generateReportBut = Button(content_frame, bd=0, bg="white", image=self.generateReportPng, command=lambda : generateReport(self.aryaId))
        generateReportBut.photo = self.generateReportPng
        generateReportBut.grid(row=20, column=0, pady=20)

        def edit(id):
            EditStudentPage(self.studentFrame, id).draw()

        editBut = Button(self.studentFrame, bd=0, bg="white", activebackground="white", image=self.editPng, command=lambda :edit(self.aryaId))
        editBut.photo = self.editPng
        editBut.place(x=950, y=20)

        def refresh():
            self.refresh()

        refreshBut = Button(self.studentFrame, bd=0, bg="white", activebackground="white", image=self.refreshPng, command=refresh)
        refreshBut.photo = self.refreshPng
        refreshBut.place(x=850, y=20)

        def close():
            self.destroy()

        closeBut = Button(self.studentFrame, bd=0, bg="white", activebackground="white", image=self.closePng, command=close)
        closeBut.photo = self.closePng
        closeBut.place(x=20, y=20)

    def destroy(self):
        self.studentFrame.destroy()

    def refresh(self):
        self.destroy()
        self.draw()

