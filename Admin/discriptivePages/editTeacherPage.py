from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from ServerSide.UpdateOperation import UpdateOperation

class EditTeacherPage():
    def __init__(self, parent, tid, username, name, email, phone):
        self.parent = parent
        self.tid = tid
        self.username = username
        self.name = name
        self.email = email
        self.phone = phone
        self.backPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/back.png"
            )
        )
        self.updateInfoPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/buttons/updateInfo.png"
            )
        )
        self.background = ImageTk.PhotoImage(
            Image.open(
                "Assets/Discription_Pages_Assets/bigCard.png"
            )
        )
        self.orangePrimColor = "#FF8C64"
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.font = "Bahnschrift"

    def draw(self):
        self.editTeacherFrame = Frame(self.parent, bd=0, bg="white", height=650, width=1080)
        self.editTeacherFrame.place(x=0, y=0)

        usernameLabel = Label(self.editTeacherFrame, bd=0, bg="white", text=self.username, fg=self.orangePrimColor,
                              font=(self.font, 30, 'normal'))
        usernameLabel.place(x=80, y=9)

        background = Label(self.editTeacherFrame, bd=0, bg="white", image=self.background)
        background.photo = self.background
        background.place(x=160, y=110)

        nameLabel = Label(self.editTeacherFrame, bd=0, bg=self.bluePrimColor, text="Name : ", fg="black",
                              font=(self.font, 22, 'normal'))
        nameLabel.place(x=284, y=183)

        nameEntry = Entry(self.editTeacherFrame, bd=0, bg=self.ligBluePrimColor, width=26, fg="black", font=(self.font, 22, 'normal'), justify="center")
        nameEntry.place(x=401.5, y=185)
        nameEntry.insert(0, self.name)

        emailLabel = Label(self.editTeacherFrame, bd=0, bg=self.bluePrimColor, text="Email : ", fg="black",
                          font=(self.font, 22, 'normal'))
        emailLabel.place(x=288, y=278)

        emailEntry = Entry(self.editTeacherFrame, bd=0, bg=self.ligBluePrimColor, width=26, fg="black", font=(self.font, 22, 'normal'),
                          justify="center")
        emailEntry.place(x=401.5, y=281)
        emailEntry.insert(0, self.email)

        phoneLabel = Label(self.editTeacherFrame, bd=0, bg=self.bluePrimColor, text="Phone No. : ", fg="black",
                           font=(self.font, 22, 'normal'))
        phoneLabel.place(x=228, y=376)

        phoneEntry = Entry(self.editTeacherFrame, bd=0, bg=self.ligBluePrimColor, width=26, fg="black", font=(self.font, 22, 'normal'),
                           justify="center")
        phoneEntry.place(x=401.5, y=377)
        phoneEntry.insert(0, str(self.phone))

        error1 = Label(self.editTeacherFrame, bd=0, bg=self.bluePrimColor, text="", fg="red",
                           font=(self.font, 15, 'normal'))
        error1.place(x=415, y=230)

        error2 = Label(self.editTeacherFrame, bd=0, bg=self.bluePrimColor, text="", fg="red",
                       font=(self.font, 15, 'normal'))
        error2.place(x=415, y=325)

        error3 = Label(self.editTeacherFrame, bd=0, bg=self.bluePrimColor, text="", fg="red",
                       font=(self.font, 15, 'normal'))
        error3.place(x=415, y=420)

        def clear_error():
            error1.config(text="")
            error2.config(text="")
            error3.config(text="")

        def updateInfo(id, name, email, phone):
            clear_error()
            validate = True
            if len(name) < 4 or len(name) > 25:
                validate = False
                error1.config(text="*name character's should be(4-25)")

            if len(email) < 5:
                validate = False
                error2.config(text="*enter valid email")

            if len(phone) == 10:
                num = list(phone)
                for d in num:
                    asa = ord(d)
                    for i in range(47, 59):
                        if asa == i:
                            break
                        elif i > 57:
                            validate = False
                            error3.config(text="*enter valid number")
            else:
                validate = False
                error3.config(text="*enter valid number")

            if validate:
                if UpdateOperation().updateTeacher(id, name, email, phone):
                    messagebox.showinfo(title="Success", message="Information Updated :)")
                else:
                    messagebox.showerror(title="Error Occurred", message="Something Went Wrong !")

        updateBut = Button(self.editTeacherFrame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.updateInfoPng, command=lambda :updateInfo(self.tid, nameEntry.get(), emailEntry.get(), phoneEntry.get()))
        updateBut.photo = self.updateInfoPng
        updateBut.place(x=540, y=485)

        def back():
            self.destroy()

        backBut = Button(self.editTeacherFrame, bd=0, bg="white", activebackground="white", image=self.backPng, command=back)
        backBut.photo = self.backPng
        backBut.place(x=20, y=20)

    def destroy(self):
        self.editTeacherFrame.destroy()