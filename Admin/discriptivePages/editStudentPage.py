from tkinter import *
from PIL import ImageTk, Image

class EditStudentPage():
    def __init__(self, parent, aryaId):
        self.parent = parent
        self.aryaId = aryaId
        self.orangePrimColor = "#FF8C64"
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"
        self.backPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/back.png"
            )
        )
        self.cardPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/bigCard2.png"
            )
        )
        self.updateInfoPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/updateInfo.png"
            )
        )
    def draw(self):
        self.editStudentFrame = Frame(self.parent, bd=0, bg="white", height=650, width=1080)
        self.editStudentFrame.place(x=0, y=0)

        aryaIdLabel = Label(self.editStudentFrame, bd=0, bg="white", text=self.aryaId, fg=self.orangePrimColor,
                            font=(self.font, 30, 'normal'))
        aryaIdLabel.place(x=80, y=9)

        card = Label(self.editStudentFrame, bd=0, bg="white", image=self.cardPng)
        card.photo = self.cardPng
        card.place(x=53, y=78)

        rawData = ["Firstname", "Lastname", "Fathername", "Mothername", "M", "2001-11-10", "8619771079",
                   "Email1997@gmail.com", "BCA", "1"]

        firstNameLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="First Name :",
                               font=(self.font, 20, 'normal'))
        firstNameLabel.place(x=132, y=125)

        firstNameEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                               font=(self.font, 21, 'normal'))
        firstNameEntry.place(x=299.5, y=128)
        firstNameEntry.insert(0, rawData[0])

        rawDobData = rawData[5]
        dobData = rawDobData.split("-")

        dobLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="DOB :",
                         font=(self.font, 20, 'normal'))
        dobLabel.place(x=655, y=125)

        dLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="D",
                       font=(self.font, 14, 'normal'))
        dLabel.place(x=756, y=100)

        dayEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=3, justify="center",
                         font=(self.font, 20, 'normal'))
        dayEntry.place(x=740, y=129)
        dayEntry.insert(0, dobData[2])

        mLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="M",
                       font=(self.font, 14, 'normal'))
        mLabel.place(x=838, y=100)

        monthEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=3, justify="center",
                           font=(self.font, 20, 'normal'))
        monthEntry.place(x=823, y=129)
        monthEntry.insert(0, dobData[1])

        yLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Y",
                       font=(self.font, 14, 'normal'))
        yLabel.place(x=923, y=100)

        dobYearEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=5, justify="center",
                             font=(self.font, 20, 'normal'))
        dobYearEntry.place(x=907.5, y=129)
        dobYearEntry.insert(0, dobData[0])

        lastNameLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Last Name :",
                               font=(self.font, 20, 'normal'))
        lastNameLabel.place(x=137, y=200)

        lastNameEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                               font=(self.font, 21, 'normal'))
        lastNameEntry.place(x=299.5, y=203)
        lastNameEntry.insert(0, rawData[1])

        emailLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Email :",
                              font=(self.font, 20, 'normal'))
        emailLabel.place(x=640, y=200)

        emailEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                              font=(self.font, 21, 'normal'))
        emailEntry.place(x=742, y=203)
        emailEntry.insert(0, rawData[7])

        fatherNameLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Father's Name :",
                              font=(self.font, 20, 'normal'))
        fatherNameLabel.place(x=92, y=276)

        fatherNameEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                              font=(self.font, 21, 'normal'))
        fatherNameEntry.place(x=299.5, y=278)
        fatherNameEntry.insert(0, rawData[2])

        phoneLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Phone No. :",
                                font=(self.font, 20, 'normal'))
        phoneLabel.place(x=585, y=276)

        phoneEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                           font=(self.font, 21, 'normal'))
        phoneEntry.place(x=742, y=278)
        phoneEntry.insert(0, rawData[6])

        motherNameLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Mother's Name :",
                                font=(self.font, 20, 'normal'))
        motherNameLabel.place(x=86, y=351)

        motherNameEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                                font=(self.font, 21, 'normal'))
        motherNameEntry.place(x=299.5, y=353)
        motherNameEntry.insert(0, rawData[3])

        courseLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Course :",
                                font=(self.font, 20, 'normal'))
        courseLabel.place(x=621, y=351)

        courseEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                           font=(self.font, 21, 'normal'))
        courseEntry.place(x=742, y=353)
        courseEntry.insert(0, rawData[8])

        genderLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Gender :",
                                font=(self.font, 20, 'normal'))
        genderLabel.place(x=181, y=426)

        genderEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                                font=(self.font, 21, 'normal'))
        genderEntry.place(x=299.5, y=428)
        genderEntry.insert(0, rawData[4])

        yearLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Year :",
                            font=(self.font, 20, 'normal'))
        yearLabel.place(x=654, y=426)

        yearEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                            font=(self.font, 21, 'normal'))
        yearEntry.place(x=742, y=428)
        yearEntry.insert(0, rawData[9])

        updateBut = Button(self.editStudentFrame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor,
                           image=self.updateInfoPng)
        updateBut.photo = self.updateInfoPng
        updateBut.place(x=470, y=530)

        def back():
            self.destroy()

        backBut = Button(self.editStudentFrame, bd=0, bg="white", activebackground="white", image=self.backPng, command=back)
        backBut.photo = self.backPng
        backBut.place(x=20, y=20)

    def destroy(self):
        self.editStudentFrame.destroy()

