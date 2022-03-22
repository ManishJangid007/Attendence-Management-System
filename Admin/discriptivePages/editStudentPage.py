from tkinter import *
from PIL import ImageTk, Image
import datetime
from daysOnMonth import daysOfMonth
from ServerSide.SelectOperation import SelectOperation
from ServerSide.UpdateOperation import UpdateOperation
from tkinter import messagebox

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

        rawData = SelectOperation().getStudentProfile(self.aryaId)

        firstNameLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="First Name :",
                               font=(self.font, 20, 'normal'))
        firstNameLabel.place(x=132, y=125)

        firstNameEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                               font=(self.font, 21, 'normal'))
        firstNameEntry.place(x=299.5, y=128)
        firstNameEntry.insert(0, rawData[1])

        rawDobData = rawData[6]
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
        dayEntry.insert(0, dobData[0])

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
        dobYearEntry.insert(0, dobData[2])

        lastNameLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Last Name :",
                               font=(self.font, 20, 'normal'))
        lastNameLabel.place(x=137, y=200)

        lastNameEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                               font=(self.font, 21, 'normal'))
        lastNameEntry.place(x=299.5, y=203)
        lastNameEntry.insert(0, rawData[2])

        emailLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Email :",
                              font=(self.font, 20, 'normal'))
        emailLabel.place(x=640, y=200)

        emailEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                              font=(self.font, 21, 'normal'))
        emailEntry.place(x=742, y=203)
        emailEntry.insert(0, rawData[9])

        fatherNameLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Father's Name :",
                              font=(self.font, 20, 'normal'))
        fatherNameLabel.place(x=92, y=276)

        fatherNameEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                              font=(self.font, 21, 'normal'))
        fatherNameEntry.place(x=299.5, y=278)
        fatherNameEntry.insert(0, rawData[3])

        phoneLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Phone No. :",
                                font=(self.font, 20, 'normal'))
        phoneLabel.place(x=585, y=276)

        phoneEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                           font=(self.font, 21, 'normal'))
        phoneEntry.place(x=742, y=278)
        phoneEntry.insert(0, rawData[8])

        motherNameLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Mother's Name :",
                                font=(self.font, 20, 'normal'))
        motherNameLabel.place(x=86, y=351)

        motherNameEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                                font=(self.font, 21, 'normal'))
        motherNameEntry.place(x=299.5, y=353)
        motherNameEntry.insert(0, rawData[4])

        courseLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Course :",
                                font=(self.font, 20, 'normal'))
        courseLabel.place(x=621, y=351)

        courseEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                           font=(self.font, 21, 'normal'))
        courseEntry.place(x=742, y=353)
        courseEntry.insert(0, SelectOperation().getCourseName(rawData[12]))

        genderLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Gender :",
                                font=(self.font, 20, 'normal'))
        genderLabel.place(x=181, y=426)

        gen = ""
        if str(rawData[5]).startswith("M") or str(rawData[5]).startswith("m"):
            gen = "M"
        elif str(rawData[5]).startswith("F") or str(rawData[5]).startswith("f"):
            gen = "F"
        elif str(rawData[5]).startswith("T") or str(rawData[5]).startswith("t"):
            gen = "T"

        genderEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                                font=(self.font, 21, 'normal'))
        genderEntry.place(x=299.5, y=428)
        genderEntry.insert(0, gen)

        yearLabel = Label(self.editStudentFrame, bd=0, bg=self.bluePrimColor, fg="black", text="Year :",
                            font=(self.font, 20, 'normal'))
        yearLabel.place(x=654, y=426)

        yearEntry = Entry(self.editStudentFrame, bg=self.ligBluePrimColor, bd=0, width=16, justify="center",
                            font=(self.font, 21, 'normal'))
        yearEntry.place(x=742, y=428)
        yearEntry.insert(0, rawData[10])

        error1 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="", font=(self.font, 14, 'normal'))
        error1.place(x=300, y=167)

        error2 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="",
                       font=(self.font, 14, 'normal'))
        error2.place(x=300, y=242)

        error3 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="",
                       font=(self.font, 14, 'normal'))
        error3.place(x=300, y=317)

        error4 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="",
                       font=(self.font, 14, 'normal'))
        error4.place(x=300, y=392)

        error5 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="",
                       font=(self.font, 14, 'normal'))
        error5.place(x=300, y=467)

        error6 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="",
                       font=(self.font, 14, 'normal'))
        error6.place(x=742, y=167)

        error7 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="",
                       font=(self.font, 14, 'normal'))
        error7.place(x=742, y=242)

        error8 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="",
                       font=(self.font, 14, 'normal'))
        error8.place(x=742, y=317)

        error9 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="",
                       font=(self.font, 14, 'normal'))
        error9.place(x=742, y=392)

        error10 = Label(self.editStudentFrame, bg=self.bluePrimColor, fg="red", text="",
                       font=(self.font, 14, 'normal'))
        error10.place(x=742, y=467)

        def clear_error():
            error1.config(text="")
            error2.config(text="")
            error3.config(text="")
            error4.config(text="")
            error5.config(text="")
            error6.config(text="")
            error7.config(text="")
            error8.config(text="")
            error9.config(text="")
            error10.config(text="")

        def update_info():
            clear_error()
            validate = True
            first_name = firstNameEntry.get()
            last_name = lastNameEntry.get()
            father_name = fatherNameEntry.get()
            mother_name = motherNameEntry.get()
            gender = genderEntry.get()
            dob_day = dayEntry.get()
            dob_month = monthEntry.get()
            dob_year = dobYearEntry.get()
            email = emailEntry.get()
            phone_no = phoneEntry.get()
            course = courseEntry.get()
            year = yearEntry.get()

            if len(first_name) <= 2 or len(first_name) > 19:
                validate = False
                if len(first_name) == 0:
                    error1.config(text="*Field Blank")
                else:
                    error1.config(text="*Length 3-18")

            if len(last_name) <= 2 or len(last_name) > 19:
                validate = False
                if len(last_name) == 0:
                    error2.config(text="*Field Blank")
                else:
                    error2.config(text="*Length 3-18")

            if len(father_name) <= 2 or len(father_name) > 25:
                validate = False
                if len(father_name) == 0:
                    error3.config(text="*Field Blank")
                else:
                    error3.config(text="*Length 3-24")

            if len(mother_name) <= 2 or len(mother_name) > 25:
                validate = False
                if len(mother_name) == 0:
                    error4.config(text="*Field Blank")
                else:
                    error4.config(text="*Length 3-24")

            if gender == "m" or gender == "M" or gender == "f" or gender == "F" or gender == "t" or gender == "T":
                if gender == "m" or gender == "M":
                    gender = "Male"
                if gender == "f" or gender == "F":
                    gender = "Female"
                if gender == "t" or gender == "T":
                    gender = "Transgender"
            else:
                validate = False
                error5.config(text="*Type Right Letter (M/F/T)")

            dobValid = False
            if len(dob_day) >= 1 and len(dob_day) <= 2:
                dobValid = True
                num = list(dob_day)
                for d in num:
                    asa = ord(d)
                    for i in range(47, 59):
                        if asa == i:
                            break
                        elif i > 57:
                            validate = False
                            dobValid = False
                            error6.config(text="*Enter Correct DOB")
            else:
                validate = False
                dobValid = False
                error6.config(text="*Enter Correct DOB")

            if len(dob_month) >= 1 and len(dob_month) <= 2:
                dobValid = True
                num = list(dob_month)
                for d in num:
                    asa = ord(d)
                    for i in range(47, 59):
                        if asa == i:
                            break
                        elif i > 57:
                            validate = False
                            dobValid = False
                            error6.config(text="*Enter Correct DOB")
            else:
                validate = False
                dobValid = False
                error6.config(text="*Enter Correct DOB")

            if len(dob_year) == 4:
                dobValid = True
                num = list(dob_year)
                for d in num:
                    asa = ord(d)
                    for i in range(47, 59):
                        if asa == i:
                            break
                        elif i > 57:
                            validate = False
                            dobValid = False
                            error6.config(text="*Enter Correct DOB")
            else:
                validate = False
                dobValid = False
                error6.config(text="*Enter Correct DOB")

            currentDate = str(datetime.date.today())
            rawDate = currentDate.split("-")
            currentYear = int(rawDate[0])
            if dobValid:
                if int(dob_year) >= currentYear - 16 or int(dob_year) < 1950:
                    validate = False
                    error6.config(text="*Enter Correct DOB")

                if int(dob_month) < 1 or int(dob_month) > 12:
                    validate = False
                    error6.config(text="*Enter Correct DOB")

                if int(dob_day) < 1 or int(dob_day) > daysOfMonth(int(dob_month), int(dob_year)):
                    validate = False
                    error6.config(text="*Enter Correct DOB")

            if len(email) < 5:
                validate = False
                if len(email) == 0:
                    error7.config(text="*Field Blank")
                else:
                    error7.config(text="*Length > 5")

            if len(phone_no) == 10:
                num = list(phone_no)
                for d in num:
                    asa = ord(d)
                    for i in range(47, 59):
                        if asa == i:
                            break
                        elif i > 57:
                            validate = False
                            error8.config(text="Enter Correct Phone No.")
            else:
                validate = False
                if len(phone_no) == 0:
                    error8.config(text="*Field Blank")
                else:
                    error8.config(text="Enter Correct Phone No.")

            if len(course) == 0:
                validate = False
                error9.config(text="*Field Blank")
            else:
                if SelectOperation().checkExistenceCourse(course) == False:
                    validate = False
                    error9.config(text="*Course Not Found")

            yearValid = False
            if len(year) > 0:
                yearValid = True
                num = list(year)
                for d in num:
                    asa = ord(d)
                    for i in range(47, 59):
                        if asa == i:
                            break
                        elif i > 57:
                            validate = False
                            yearValid = False
                            error10.config(text="*eg.1,2,3")
            else:
                validate = False
                error10.config(text="*eg.1,2,3")

            if yearValid:
                if int(year) < 1 or int(year) > 6:
                    validate = False
                    error10.config(fg="red", text="*Year Not Valid")
                else:
                    try:
                        if int(year) > SelectOperation().getCourseDuration(course):
                            validate = False
                            error10.config(fg="red", text="*Year Not Valid")
                    except:
                        pass

            if validate:
                dob = f"{dob_day}-{dob_month}-{dob_year}"
                clear_error()
                if UpdateOperation().updateStudent(self.aryaId, first_name, last_name, father_name, mother_name, gender, dob, phone_no, email, year, course):
                    messagebox.showinfo(title="Success", message="Info. Updated Successfully")
                else:
                    messagebox.showerror(title="Error Occurred", message="Something Went Wrong !")


        updateBut = Button(self.editStudentFrame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor,
                           image=self.updateInfoPng, command=update_info)
        updateBut.photo = self.updateInfoPng
        updateBut.place(x=470, y=530)


        def back():
            self.destroy()

        backBut = Button(self.editStudentFrame, bd=0, bg="white", activebackground="white", image=self.backPng, command=back)
        backBut.photo = self.backPng
        backBut.place(x=20, y=20)

    def destroy(self):
        self.editStudentFrame.destroy()

