from tkinter import *
from PIL import ImageTk, Image
from Admin.LoginPage import LoginPage

class Step5():
    def __init__(self, root):
        self.root = root
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step5/background.png"))
        self.skipButPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step5/Button/skip.png"))
        self.setButPng =ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step5/Button/set.png"))
        self.bubblePng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step5/bubble.png"))
        self.primaryColor = "#FF8C64"
        self.font = "Bahnschrift"

    def draw(self):
        self.step5_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.step5_frame.place(x=0, y=0)

        self.background = Label(self.step5_frame, bg="white", bd=0, image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=12, y=5)

        self.weLabel = Label(self.step5_frame, fg=self.primaryColor, text="We", bd=0, bg="white",
                             font=(self.font, 40, 'normal'))
        self.weLabel.place(x=685, y=198)

        self.areLabel = Label(self.step5_frame, fg="black", text="Are", bd=0, bg="white",
                             font=(self.font, 40, 'normal'))
        self.areLabel.place(x=775, y=198)

        self.liveLabel = Label(self.step5_frame, fg="black", text="Live", bd=0, bg="white",
                              font=(self.font, 40, 'normal'))
        self.liveLabel.place(x=872, y=198)

        self.bubble = Label(self.step5_frame, bg="white", bd=0, image=self.bubblePng)
        self.bubble.photo = self.bubblePng
        self.bubble.place(x=900, y=10)

        self.setLabel = Label(self.step5_frame, fg="black", text="Set", bd=0, bg="white",
                              font=(self.font, 25, 'normal'))
        self.setLabel.place(x=615, y=270)

        self.userLabel = Label(self.step5_frame, fg=self.primaryColor, text="Username", bd=0, bg="white",
                              font=(self.font, 25, 'normal'))
        self.userLabel.place(x=670, y=270)

        self.andLabel = Label(self.step5_frame, fg="black", text="And", bd=0, bg="white",
                               font=(self.font, 25, 'normal'))
        self.andLabel.place(x=830, y=270)

        self.passLabel = Label(self.step5_frame, fg=self.primaryColor, text="Password", bd=0, bg="white",
                              font=(self.font, 25, 'normal'))
        self.passLabel.place(x=895, y=270)

        self.andLabel = Label(self.step5_frame, fg="black", text="For", bd=0, bg="white",
                               font=(self.font, 25, 'normal'))
        self.andLabel.place(x=760, y=310)

        self.andLabel = Label(self.step5_frame, fg=self.primaryColor, text="Admin", bd=0, bg="white",
                              font=(self.font, 25, 'normal'))
        self.andLabel.place(x=820, y=310)

        self.usernameLabel = Label(self.step5_frame, fg="black", text="Username", bd=0, bg="white",
                              font=(self.font, 20, 'normal'))
        self.usernameLabel.place(x=510, y=390)

        self.usernameEntry = Entry(self.step5_frame, fg="black", bg=self.primaryColor, width=19, bd=0,
                               font=(self.font, 20, "normal"), justify="center")
        self.usernameEntry.place(x=698, y=392)

        self.passwordLabel = Label(self.step5_frame, fg="black", text="Password", bd=0, bg="white",
                                   font=(self.font, 20, 'normal'))
        self.passwordLabel.place(x=511, y=455)

        self.passEntry = Entry(self.step5_frame, fg="black", bg=self.primaryColor, width=19, bd=0,
                               font=(self.font, 20, "normal"), justify="center", show="*")
        self.passEntry.place(x=698, y=459)

        self.cPassLabel = Label(self.step5_frame, fg="black", text="Confirm Password", bd=0, bg="white",
                                   font=(self.font, 20, 'normal'))
        self.cPassLabel.place(x=405, y=520)

        self.cPassEntry = Entry(self.step5_frame, fg="black", bg=self.primaryColor, width=19, bd=0,
                               font=(self.font, 20, "normal"), justify="center", show="*")
        self.cPassEntry.place(x=698, y=525)

        self.defaultLabel = Label(self.step5_frame, fg="black", text="Default :-", bd=0, bg="white",
                                   font=(self.font, 15, 'normal'))
        self.defaultLabel.place(x=10, y=480)

        self.dUserPassLabel = Label(self.step5_frame, fg="black", text="Username : admin@root \n Password : admin@123", bd=0, bg="white",
                                   font=(self.font, 15, 'normal'), justify="left")
        self.dUserPassLabel.place(x=15, y=505)

        self.errorMessage = Label(self.step5_frame, fg="red", text="", bd=0, bg="white",
                                   font=(self.font, 12, 'normal'), justify="left")
        self.errorMessage.place(x=700, y=573)

        def skip():
            self.destroy()
            LoginPage(self.root).draw()

        self.skipBut = Button(self.step5_frame, bg="white", activebackground="white", bd=0,
                               image=self.skipButPng, command=skip)
        self.skipBut.photo = self.skipButPng
        self.skipBut.place(x=760, y=600)

        def set():
            self.errorMessage.config(text="")
            username = self.usernameEntry.get()
            password = self.passEntry.get()
            cpassword = self.cPassEntry.get()

            if len(username) > 0 and len(password) > 0:
                if len(username) >= 5:
                    if len(username) <= 12:
                        if len(password) >= 8:
                            if len(password) <= 18:
                                if password == cpassword:
                                    LoginPage(self.root).draw()
                                else:
                                    self.errorMessage.config(text="*Password could not match")
                            else:
                                self.errorMessage.config(text="*Password is too long (8-18)")
                        else:
                            self.errorMessage.config(text="*Use Minimum 8 Characters For Password")
                    else:
                        self.errorMessage.config(text="*Username is too Long (5-12)")
                else:
                    self.errorMessage.config(text="*Username is too Short (5-12)")
            else:
                self.errorMessage.config(text="*Don't leave the fields Blank")

        self.setBut = Button(self.step5_frame, bg="white", activebackground="white", bd=0,
                              image=self.setButPng, command=set)
        self.setBut.photo = self.setButPng
        self.setBut.place(x=860, y=600)

    def destroy(self):
        self.step5_frame.destroy()

