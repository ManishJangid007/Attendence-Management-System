from tkinter import *
import tkinter as tk
from Scrollbar import scrollbar
from PIL import ImageTk, Image
from tkinter import messagebox
from discriptivePages.editTeacherPage import EditTeacherPage
from ServerSide.SelectOperation import SelectOperation
from ServerSide.UpdateOperation import UpdateOperation

class TeacherDisPage():
    def __init__(self, parent, id, username):
        self.parent = parent
        self.username = username
        self.id = id
        self.closePng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/close.png"
            )
        )
        self.editPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/edit.png"
            )
        )
        self.refreshPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/refresh.png"
            )
        )
        self.dividerPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/horizontalDivider.png"
            )
        )
        self.unassignPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/unassign.png"
            )
        )
        self.deleteProfilePng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/deleteprofile.png"
            )
        )
        self.orangePrimColor = "#FF8C64"
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"
        self.greyColor = "#606060"

    def draw(self):
        self.teacherFrame = Frame(self.parent, bd=0, bg="white", height=650, width=1080)
        self.teacherFrame.place(x=0, y=0)

        rawData = SelectOperation().getTeacherProfile(self.id)

        usernameLabel = Label(self.teacherFrame, bd=0, bg="white", text=self.username, fg=self.orangePrimColor, font=(self.font, 30, 'normal'))
        usernameLabel.place(x=80, y=9)

        canvas = tk.Canvas(self.teacherFrame, bg="white", bd=0, width=1080, height=580,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg="white", width=1080, height=580)

        self.scrol = scrollbar(canvas, canvas, height=265, hp=1061)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=70)

        nameLabel = Label(content_frame, bd=0, bg="white", fg="black", text=f"Name : {rawData[0]}", font=(self.font, 25, 'normal'), justify="right")
        nameLabel.grid(row=0, column=0, pady=20, columnspan=3)

        divider = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider.photo = self.dividerPng
        divider.grid(row=1, column=0, padx=350, columnspan=3)

        emailLabel = Label(content_frame, bd=0, bg="white", fg="black",
                           text=f"Email : {rawData[1]}",
                           font=(self.font, 25, 'normal'), justify="right")
        emailLabel.grid(row=2, column=0, pady=20, columnspan=3)

        divider1 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider1.photo = self.dividerPng
        divider1.grid(row=3, column=0, padx=350, columnspan=3)

        phoneLabel = Label(content_frame, bd=0, bg="white", fg="black",
                           text=f"Phone No. : {rawData[2]}",
                           font=(self.font, 25, 'normal'), justify="right")
        phoneLabel.grid(row=4, column=0, pady=20, columnspan=3)

        divider2 = Label(content_frame, bd=0, bg="white", image=self.dividerPng)
        divider2.photo = self.dividerPng
        divider2.grid(row=5, column=0, padx=350, columnspan=3)

        subLabel = Label(content_frame, bd=0, bg="white", fg="black",
                           text="Subjects :-",
                           font=(self.font, 25, 'normal'), justify="right")
        subLabel.grid(row=6, column=0, pady=20, columnspan=3)

        rawSubject = SelectOperation().getTeacherSubjects(self.id)

        def un_assign(subject_id):
            if messagebox.askyesno(title="Warning !", message="Are you sure you want Un-assign this subject"):
                if UpdateOperation().removeTeacherFromSubject(subject_id):
                    self.refresh()
                    messagebox.showinfo(title="Success", message="Subject Un-Assigned")
                else:
                    messagebox.showerror(title="Error Occurred !", message="Something Went Wrong !")


        def drawSubject(row, sn, subject_id, subject):
            s = Label(content_frame, bd=0, bg="white", fg=self.greyColor, text=f"{sn}.", font=(self.font, 20, 'normal'))
            s.grid(row=row, column=0, pady=10)

            sub = Label(content_frame, bd=0, bg="white", fg=self.greyColor, text=subject, font=(self.font, 20, 'normal'))
            sub.grid(row=row, column=1, pady=10)

            b = Button(content_frame, bd=0, bg="white", activebackground="white", image=self.unassignPng, command=lambda:un_assign(subject_id))
            b.photo = self.unassignPng
            b.grid(row=row, column=2, pady=10)

        if len(rawSubject) > 0:
            row=7
            sn=1
            for data in rawSubject:
                drawSubject(row, sn, data[0], data[1])
                row+=1
                sn+=1
        else:
            notLabel = Label(content_frame, bd=0, bg="white", fg="black",
                             text="It's Empty Here !",
                             font=(self.font, 25, 'normal'), justify="right")
            notLabel.grid(row=7, column=0, pady=20, columnspan=3)

        def deleteProfile(tid, username):
            if messagebox.askyesno(title="Warning !", message=f"Are you sure,\n you want to delete user = '{username}'"):
                if UpdateOperation().deleteTeacher(tid):
                    messagebox.showinfo(title="Success", message="Teacher Deleted Successfully !")
                else:
                    messagebox.showerror(title="Error Occurred", message="Something Went Wrong !")
                self.destroy()

        deleteProBut = Button(self.teacherFrame, bd=0, bg="white", activebackground="white", image=self.deleteProfilePng,
                            command=lambda :deleteProfile(self.id, self.username))
        deleteProBut.photo = self.deleteProfilePng
        deleteProBut.place(x=920, y=20)

        def edit():
            EditTeacherPage(self.teacherFrame, self.id, self.username, rawData[0], rawData[1], rawData[2]).draw()

        editBut = Button(self.teacherFrame, bd=0, bg="white", activebackground="white", image=self.editPng, command=edit)
        editBut.photo = self.editPng
        editBut.place(x=835, y=20)

        def refresh():
            self.refresh()

        refreshBut = Button(self.teacherFrame, bd=0, bg="white", activebackground="white", image=self.refreshPng, command=refresh)
        refreshBut.photo = self.refreshPng
        refreshBut.place(x=735, y=20)

        def close():
            self.destroy()

        closeBut = Button(self.teacherFrame, bd=0, bg="white", activebackground="white", image=self.closePng, command=close)
        closeBut.photo = self.closePng
        closeBut.place(x=20, y=20)


    def destroy(self):
        self.teacherFrame.destroy()

    def refresh(self):
        self.destroy()
        self.draw()