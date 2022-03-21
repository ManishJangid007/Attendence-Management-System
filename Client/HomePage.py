from tkinter import *
from PIL import ImageTk, Image
from Pages.MarkAttendance.SelectSubjectPage import SelectSubjectPage
from ServerSide.SelectOperation import SelectOperation

class HomePage():
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.backgroundPng = ImageTk.PhotoImage(file=("Assets/Home_Page_Assets/background.png"))
        self.logoutButPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Home_Page_Assets/Buttons/logout.png"
            )
        )
        self.ligBluePrimColor = "#F2F8FF"
        self.menu_bar_color = "#F78888"
        self.font = "Bahnschrift"

    def draw(self):
        self.home_page_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.home_page_frame.place(x=0, y=0)

        self.background = Label(self.home_page_frame, bg="white", bd=0, image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=12, y=5)

        self.menu_bar = Frame(self.home_page_frame, bg=self.menu_bar_color, width=1032, height=63)
        self.menu_bar.place(x=21, y=15)

        teacherName = Label(self.menu_bar, text=f"@{SelectOperation().getTeacherNameWithUserName(self.username)}", bg=self.menu_bar_color, bd=0,
                            fg="white", font=(self.font, 25, 'normal'))
        teacherName.place(x=8, y=5)

        logButt = Button(self.menu_bar, bd=0, bg=self.menu_bar_color, activebackground=self.menu_bar_color,
                            image=self.logoutButPng, command=self.destroy)
        logButt.photo = self.logoutButPng
        logButt.place(x=920, y=15)


        self.mark_attendance_panel = Frame(self.home_page_frame, bg=self.menu_bar_color, width=730, height=524)
        self.mark_attendance_panel.place(x=323, y=103)

        SelectSubjectPage(self.mark_attendance_panel, self.username).draw()

    def destroy(self):
        self.home_page_frame.destroy()
