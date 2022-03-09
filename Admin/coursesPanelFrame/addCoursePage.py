from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from ServerSide.DuplicateVerification import DuplicateVerification
from ServerSide.InsertOperations import InsertOperations

class AddCoursePage():
    def __init__(self, parent):
        self.parent = parent
        self.cardPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/coursepanel/card2.png"))
        self.addPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/coursepanel/buttons/add.png"))
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.secondaryColor = "#4F4F4F"
        self.font = "Bahnschrift"

    def draw(self):
        card = Label(self.parent, bd=0, bg=self.ligBluePrimColor, image=self.cardPng)
        card.photo = self.cardPng
        card.place(x=188, y=87)

        cNLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg="white", text="New Course Name", font=(self.font, 25, 'normal'))
        cNLabel.place(x=222, y=120)

        cNEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                               font=(self.font, 19, 'normal'))
        cNEntry.place(x=269, y=182)

        cDLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg="white", text="Course Duration",
                        font=(self.font, 25, 'normal'))
        cDLabel.place(x=238, y=245)

        cDEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=6, justify="center",
                        font=(self.font, 19, 'normal'))
        cDEntry.place(x=284, y=307)

        yearLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg=self.secondaryColor, text="Years",
                        font=(self.font, 16, 'normal'))
        yearLabel.place(x=388, y=308)

        def add():
            course = cNEntry.get()
            year = int(cDEntry.get())

            validate = True

            if DuplicateVerification().dublicateCourse(course) == False:
                validate = False
                messagebox.showerror(title="Duplicate Entry", message="Course Already Exist !")

            if len(course) < 2 or len(course) > 25:
                validate = False

            if year < 1 or year > 6:
                validate = False

            if validate:
                if InsertOperations().insertCourses(course, year):
                    messagebox.showinfo(title="Success", message="Course Added Successfully")
                    cNEntry.delete(0, END)
                    cDEntry.delete(0, END)
                else:
                    messagebox.showerror(title="Error Occurred", message="Something Went Wrong !")


        addBut = Button(self.parent, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.addPng, command=add)
        addBut.photo = self.addPng
        addBut.place(x=330, y=370)
