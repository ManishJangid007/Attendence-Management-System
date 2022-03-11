from tkinter import *
from PIL import ImageTk, Image
import datetime
from daysOnMonth import daysOfMonth

class AddStudentPage():
    def __init__(self, parent):
        self.parent = parent
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/background.png"))
        self.addPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/buttons/add.png"))
        self.ligBluePrimColor = "#F2F8FF"
        self.font = "Bahnschrift"

    def draw(self):
        background = Label(self.parent, bd=0, bg=self.ligBluePrimColor, image=self.backgroundPng)
        background.photo = self.backgroundPng
        background.place(x=100, y=25)

        studentIdLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="Student ID", font=(self.font, 14, 'normal'))
        studentIdLabel.place(x=237, y=0)

        studentIdEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                           font=(self.font, 21, 'normal'))
        studentIdEntry.place(x=241, y=29)
        studentIdEntry.insert(0, "AryaId")

        firstNameLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="First Name",
                               font=(self.font, 14, 'normal'))
        firstNameLabel.place(x=100, y=83)

        firstNameEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                               font=(self.font, 21, 'normal'))
        firstNameEntry.place(x=104, y=112)

        lastNameLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="Last Name",
                               font=(self.font, 14, 'normal'))
        lastNameLabel.place(x=387, y=83)

        lastNameEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                               font=(self.font, 21, 'normal'))
        lastNameEntry.place(x=391, y=112)

        fatherNameLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="Father's Name",
                               font=(self.font, 14, 'normal'))
        fatherNameLabel.place(x=100, y=166)

        fatherNameEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                              font=(self.font, 21, 'normal'))
        fatherNameEntry.place(x=104, y=196)

        motherNameLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="Mother's Name",
                                font=(self.font, 14, 'normal'))
        motherNameLabel.place(x=387, y=166)

        motherNameEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                                font=(self.font, 21, 'normal'))
        motherNameEntry.place(x=391, y=196)

        genderLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="Gender ( M / F / T )",
                                font=(self.font, 14, 'normal'))
        genderLabel.place(x=100, y=249)

        genderEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                                font=(self.font, 21, 'normal'))
        genderEntry.place(x=104, y=279)

        dobLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="Date of Birth",
                            font=(self.font, 14, 'normal'))
        dobLabel.place(x=387, y=249)

        dLabel = Label(self.parent, bd=0, bg="white", fg="black", text="D",
                    font=(self.font, 14, 'normal'))
        dLabel.place(x=395, y=284)

        dayEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=3, justify="center",
                            font=(self.font, 20, 'normal'))
        dayEntry.place(x=416, y=280)

        mLabel = Label(self.parent, bd=0, bg="white", fg="black", text="M",
                       font=(self.font, 14, 'normal'))
        mLabel.place(x=470, y=284)

        monthEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=3, justify="center",
                         font=(self.font, 20, 'normal'))
        monthEntry.place(x=493, y=280)

        yLabel = Label(self.parent, bd=0, bg="white", fg="black", text="Y",
                       font=(self.font, 14, 'normal'))
        yLabel.place(x=548, y=284)

        dobYearEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=4, justify="center",
                           font=(self.font, 20, 'normal'))
        dobYearEntry.place(x=568, y=280)

        emailLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="E-mail",
                            font=(self.font, 14, 'normal'))
        emailLabel.place(x=100, y=332)

        emailEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                            font=(self.font, 21, 'normal'))
        emailEntry.place(x=104, y=362)

        phoneLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="Phone No.",
                           font=(self.font, 14, 'normal'))
        phoneLabel.place(x=387, y=332)

        phoneEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                           font=(self.font, 21, 'normal'))
        phoneEntry.place(x=391, y=362)

        courseLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="Course",
                           font=(self.font, 14, 'normal'))
        courseLabel.place(x=100, y=415)

        courseEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                           font=(self.font, 21, 'normal'))
        courseEntry.place(x=104, y=446)

        yearLabel = Label(self.parent, bd=0, bg=self.ligBluePrimColor, fg="black", text="Year",
                            font=(self.font, 14, 'normal'))
        yearLabel.place(x=387, y=415)

        yearEntry = Entry(self.parent, bg="white", bd=0, width=15, justify="center",
                            font=(self.font, 21, 'normal'))
        yearEntry.place(x=391, y=446)

        def clear_errors():
            studentIdLabel.config(fg="black", text="Student ID")
            firstNameLabel.config(fg="black", text="First Name")
            lastNameLabel.config(fg="black", text="Last Name")
            fatherNameLabel.config(fg="black", text="Father's Name")
            motherNameLabel.config(fg="black", text="Mother's Name")
            genderLabel.config(fg="black", text="Gender ( M / F / T )")
            dobLabel.config(fg="black", text="Date of Birth")
            dLabel.config(fg="black", text="D")
            mLabel.config(fg="black", text="M")
            yLabel.config(fg="black", text="Y")
            emailLabel.config(fg="black", text="E-mail")
            phoneLabel.config(fg="black", text="Phone No.")
            courseLabel.config(fg="black", text="Course")
            yearLabel.config(fg="black", text="Year")

        def clear_fields():
            studentIdEntry.delete(0, END)
            studentIdEntry.insert(0, "AryaID")
            firstNameEntry.delete(0, END)
            lastNameEntry.delete(0, END)
            fatherNameEntry.delete(0, END)
            motherNameEntry.delete(0, END)
            genderEntry.delete(0, END)
            dayEntry.delete(0, END)
            monthEntry.delete(0, END)
            dobYearEntry.delete(0, END)
            emailEntry.delete(0, END)
            phoneEntry.delete(0, END)
            courseEntry.delete(0, END)
            yearEntry.delete(0, END)

        def add():
            clear_errors()
            validate = True
            student_id = studentIdEntry.get()
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

            if len(student_id) <= 3 or len(student_id) > 14:
                validate = False
                if len(student_id) == 0:
                    studentIdLabel.config(fg="red", text="Student ID (Field Blank)")
                else:
                    studentIdLabel.config(fg="red", text="Student ID (Length 4-14)")

            if len(first_name) <= 2 or len(first_name) > 19:
                validate = False
                if len(first_name) == 0:
                    firstNameLabel.config(fg="red", text="First Name (Field Blank)")
                else:
                    firstNameLabel.config(fg="red", text="First Name (Length 3-18)")

            if len(last_name) <= 2 or len(last_name) > 19:
                validate = False
                if len(last_name) == 0:
                    lastNameLabel.config(fg="red", text="Last Name (Field Blank)")
                else:
                    lastNameLabel.config(fg="red", text="Last Name (Length 3-18)")

            if len(father_name) <= 2 or len(father_name) > 25:
                validate = False
                if len(father_name) == 0:
                    fatherNameLabel.config(fg="red", text="Father's Name (Field Blank)")
                else:
                    fatherNameLabel.config(fg="red", text="Father's Name (Length 3-24)")

            if len(mother_name) <= 2 or len(mother_name) > 25:
                validate = False
                if len(mother_name) == 0:
                    motherNameLabel.config(fg="red", text="Mother's Name (Field Blank)")
                else:
                    motherNameLabel.config(fg="red", text="Mother's Name (Length 3-24)")

            if gender == "m" or gender == "M" or gender == "f" or gender == "F" or gender == "t" or gender == "T":
                pass
            else:
                validate = False
                genderLabel.config(fg="red")

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
                            dLabel.config(fg="red")
                            dobLabel.config(fg="red")
            else:
                validate = False
                dobValid = False
                dLabel.config(fg="red")
                dobLabel.config(fg="red")

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
                            mLabel.config(fg="red")
                            dobLabel.config(fg="red")
            else:
                validate = False
                dobValid = False
                mLabel.config(fg="red")
                dobLabel.config(fg="red")

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
                            yLabel.config(fg="red")
                            dobLabel.config(fg="red")
            else:
                validate = False
                dobValid = False
                yLabel.config(fg="red")
                dobLabel.config(fg="red")

            currentDate = str(datetime.date.today())
            rawDate = currentDate.split("-")
            currentYear = int(rawDate[0])
            if dobValid:
                if int(dob_year) >= currentYear-10 or int(dob_year) < 1950:
                    validate = False
                    yLabel.config(fg="red")
                    dobLabel.config(fg="red")

                if int(dob_month) < 1 or int(dob_month) > 12:
                    validate = False
                    mLabel.config(fg="red")
                    dobLabel.config(fg="red")

                if int(dob_day) < 1 or int(dob_day) > daysOfMonth(int(dob_month), int(dob_year)):
                    validate = False
                    dLabel.config(fg="red")
                    dobLabel.config(fg="red")

            if len(email) < 5:
                validate = False
                if len(email) == 0:
                    emailLabel.config(fg="red", text="E-mail (Field Blank)")
                else:
                    emailLabel.config(fg="red", text="E-mail (Length > 5)")

            if len(phone_no) == 10:
                num = list(phone_no)
                for d in num:
                    asa = ord(d)
                    for i in range(47, 59):
                        if asa == i:
                            break
                        elif i > 57:
                            validate = False
                            phoneLabel.config(fg="red")
            else:
                validate = False
                if len(phone_no) == 0:
                    phoneLabel.config(fg="red", text="Phone No. (Field Blank)")
                else:
                    phoneLabel.config(fg="red")

            if len(course) == 0:
                validate = False
                courseLabel.config(fg="red", text="Course (Field Blank)")

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
                            yearLabel.config(fg="red", text="Year (eg.1,2,3)")
            else:
                validate = False
                yearLabel.config(fg="red", text="Year (eg.1,2,3)")

            if yearValid:
                if int(year) < 1 or int(year) > 6:
                    validate = False
                    yearLabel.config(fg="red", text="Year (Not Valid)")

            if validate:
                dob = f"{dob_day}-{dob_month}-{dob_year}"
                clear_errors()
                clear_fields()
                print("Done!")


        addButton = Button(self.parent, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,
                           image=self.addPng, command=add)
        addButton.photo = self.addPng
        addButton.place(x=655, y=485)