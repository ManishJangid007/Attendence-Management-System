from tkinter import *
import tkinter as tk
import datetime
from datetime import timedelta
from PIL import ImageTk, Image
from daysOnMonth import daysOfMonth
from searchPanelFrames.step1 import SearchStep1
from Admin.Scrollbar import scrollbar

class HomePage():
    def __init__(self, root, username):
        self.username = username
        self.root = root
        self.backgroundPng = ImageTk.PhotoImage(file=("Assets/Home_Page_Assets/background.png"))
        self.settingsPng = ImageTk.PhotoImage(file=("Assets/Home_Page_Assets/buttons/settings.png"))
        self.orangePrimColor = "#FF8C64"
        self.bluePrimColor = "#87A0C4"
        self.ligBluePrimColor = "#F2F8FF"
        self.primaryTextColor = "#0F4189"
        self.font = "Bahnschrift"
        self.menuActive = "#000000"
        self.menuNonActive = "#3A3A3A"
        self.sidePanelActive = "#1E1E1E"
        self.sidePanelNonActive = "#FFFFFF"

    def draw(self):
        self.home_page_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.home_page_frame.place(x=0, y=0)

        self.background = Label(self.home_page_frame, bg="white", bd=0, image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=12, y=5)

        self.menu_bar = Frame(self.home_page_frame, bg=self.orangePrimColor, width=1032, height=63)
        self.menu_bar.place(x=21, y=15)

        self.attendance_side_panel()

        userHeading = Label(self.menu_bar, text=f"@{self.username}", bg=self.orangePrimColor, bd=0, fg=self.primaryTextColor, font=(self.font, 25, 'normal'))
        userHeading.place(x=8 , y=5)

        def attendanceFun():
            self.deselect_menu()
            self.attendence.config(fg=self.menuActive)
            self.destroy_all_side_panel()
            self.destroy_all_main_panel()
            self.attendance_side_panel()


        self.attendence = Label(self.menu_bar, text="Attendance", bg=self.orangePrimColor, bd=0, fg=self.menuActive, font=(self.font, 20, 'normal'))
        self.attendence.place(x=450, y=11)
        self.attendence.bind("<Button-1>", lambda e: attendanceFun())

        def teacherFun():
            self.deselect_menu()
            self.teacher.config(fg=self.menuActive)
            self.destroy_all_side_panel()
            self.destroy_all_main_panel()
            self.teacher_side_panel()


        self.teacher = Label(self.menu_bar, text="Teacher", bg=self.orangePrimColor, bd=0,
                             fg=self.menuNonActive, font=(self.font, 20, 'normal'))
        self.teacher.place(x=610, y=11)
        self.teacher.bind("<Button-1>", lambda e: teacherFun())

        def studentFun():
            self.deselect_menu()
            self.student.config(fg=self.menuActive)
            self.destroy_all_side_panel()
            self.destroy_all_main_panel()
            self.student_side_panel()


        self.student = Label(self.menu_bar, text="Student", bg=self.orangePrimColor, bd=0,
                             fg=self.menuNonActive, font=(self.font, 20, 'normal'))
        self.student.place(x=725, y=11)
        self.student.bind("<Button-1>", lambda e: studentFun())

        def coursesFun():
            self.deselect_menu()
            self.courses.config(fg=self.menuActive)
            self.destroy_all_side_panel()
            self.destroy_all_main_panel()
            self.courses_side_panel()


        self.courses = Label(self.menu_bar, text="Courses", bg=self.orangePrimColor, bd=0,
                             fg=self.menuNonActive, font=(self.font, 20, 'normal'))
        self.courses.place(x=840, y=11)
        self.courses.bind("<Button-1>", lambda e: coursesFun())

        def settingsFun():
            self.deselect_menu()
            self.destroy_all_side_panel()
            self.destroy_all_main_panel()
            self.settings_side_panel()


        self.settingsButton = Button(self.menu_bar, bg=self.orangePrimColor, activebackground=self.orangePrimColor, bd=0, image=self.settingsPng, command=settingsFun)
        self.settingsButton.photo = self.settingsPng
        self.settingsButton.place(x=975, y=12)

    def destroy(self):
        self.home_page_frame.destroy()

    def deselect_menu(self):
        self.attendence.config(fg=self.menuNonActive)
        self.student.config(fg=self.menuNonActive)
        self.teacher.config(fg=self.menuNonActive)
        self.courses.config(fg=self.menuNonActive)



        # <!----Side Panels Sarting from Here---!>




    # this is "ATTENDANCE'S" side panel

    def attendance_side_panel(self):
        self.attSidePanel = Frame(self.home_page_frame, bg=self.bluePrimColor, width=275, height=524)
        self.attSidePanel.place(x=21, y=103)

        searchPng = ImageTk.PhotoImage(file=("Assets/Home_Page_Assets/buttons/search.png"))

        self.search_main_panel()

        def deselect():
            try:
                self.todayReport.config(fg=self.sidePanelNonActive)
                self.yesterdayReport.config(fg=self.sidePanelNonActive)
                self.search.config(fg=self.sidePanelNonActive)
            except:
                pass

        def searchFun():
            deselect()
            self.search.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.search_main_panel()

        searchIcon = Label(self.attSidePanel, bd=0, bg=self.bluePrimColor, image=searchPng)
        searchIcon.photo = searchPng
        searchIcon.place(x=18, y=24)

        self.search = Label(self.attSidePanel, text="Search", bg=self.bluePrimColor, bd=0,
                             fg=self.sidePanelActive, font=(self.font, 20, 'normal'))
        self.search.place(x=40, y=15)
        self.search.bind("<Button-1>", lambda e: searchFun())

        def todayReportFun():
            deselect()
            self.todayReport.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.todays_report_main_panel()

        self.todayReport = Label(self.attSidePanel, text="Today's Report", bg=self.bluePrimColor, bd=0,
                             fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.todayReport.place(x=20, y=75)
        self.todayReport.bind("<Button-1>", lambda e: todayReportFun())

        def yesterdayReportFun():
            deselect()
            self.yesterdayReport.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.yesterday_report_main_panel()

        self.yesterdayReport = Label(self.attSidePanel, text="Yesterday's Report", bg=self.bluePrimColor, bd=0,
                             fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.yesterdayReport.place(x=20, y=135)
        self.yesterdayReport.bind("<Button-1>", lambda e: yesterdayReportFun())


    def destroy_attendance_side_panel(self):
        self.attSidePanel.destroy()

    # this is "TEACHER'S" side panel

    def teacher_side_panel(self):
        self.teacherSidePanel = Frame(self.home_page_frame, bg=self.bluePrimColor, width=275, height=524)
        self.teacherSidePanel.place(x=21, y=103)

        self.add_teacher_main_panel()

        def deselect():
            try:
                self.addTeacher.config(fg=self.sidePanelNonActive)
                self.removeTeacher.config(fg=self.sidePanelNonActive)
                self.teacherlist.config(fg=self.sidePanelNonActive)
            except:
                pass

        def addTeacherFun():
            deselect()
            self.addTeacher.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.add_teacher_main_panel()


        self.addTeacher = Label(self.teacherSidePanel, text="Add Teacher", bg=self.bluePrimColor, bd=0,
                                 fg=self.sidePanelActive, font=(self.font, 20, 'normal'))
        self.addTeacher.place(x=20, y=15)
        self.addTeacher.bind("<Button-1>", lambda e: addTeacherFun())

        def removeTeacherFun():
            deselect()
            self.removeTeacher.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()

        self.removeTeacher = Label(self.teacherSidePanel, text="Remove Teacher", bg=self.bluePrimColor, bd=0,
                                fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.removeTeacher.place(x=20, y=75)
        self.removeTeacher.bind("<Button-1>", lambda e: removeTeacherFun())

        def teacherListFun():
            deselect()
            self.teacherlist.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()

        self.teacherlist = Label(self.teacherSidePanel, text="Teacher's List", bg=self.bluePrimColor, bd=0,
                                   fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.teacherlist.place(x=20, y=135)
        self.teacherlist.bind("<Button-1>", lambda e: teacherListFun())

    def destroy_teacher_side_panel(self):
        self.teacherSidePanel.destroy()

    # this is "STUDENT'S" side panel

    def student_side_panel(self):
        self.studentSidePanel = Frame(self.home_page_frame, bg=self.bluePrimColor, width=275, height=524)
        self.studentSidePanel.place(x=21, y=103)

        def deselect():
            try:
                self.addStudent.config(fg=self.sidePanelNonActive)
                self.removeStudent.config(fg=self.sidePanelNonActive)
                self.studentList.config(fg=self.sidePanelNonActive)
            except:
                pass

        def addStudentFun():
            deselect()
            self.addStudent.config(fg=self.sidePanelActive)

        self.addStudent = Label(self.studentSidePanel, text="Add Student", bg=self.bluePrimColor, bd=0,
                                fg=self.sidePanelActive, font=(self.font, 20, 'normal'))
        self.addStudent.place(x=20, y=15)
        self.addStudent.bind("<Button-1>", lambda e: addStudentFun())

        def removestudentFun():
            deselect()
            self.removeStudent.config(fg=self.sidePanelActive)

        self.removeStudent = Label(self.studentSidePanel, text="Remove Student", bg=self.bluePrimColor, bd=0,
                                   fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.removeStudent.place(x=20, y=75)
        self.removeStudent.bind("<Button-1>", lambda e: removestudentFun())

        def studentListFun():
            deselect()
            self.studentList.config(fg=self.sidePanelActive)

        self.studentList = Label(self.studentSidePanel, text="Student's List", bg=self.bluePrimColor, bd=0,
                                 fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.studentList.place(x=20, y=135)
        self.studentList.bind("<Button-1>", lambda e: studentListFun())

    def destroy_student_side_panel(self):
        self.studentSidePanel.destroy()

    # this is "COURSES" side panel


    def courses_side_panel(self):
        self.coursesSidePanel = Frame(self.home_page_frame, bg=self.bluePrimColor, width=275, height=524)
        self.coursesSidePanel.place(x=21, y=103)

        def deselect():
            try:
                self.addCourses.config(fg=self.sidePanelNonActive)
                self.removeCourses.config(fg=self.sidePanelNonActive)
                self.coursesList.config(fg=self.sidePanelNonActive)
            except:
                pass

        def addCoursesFun():
                deselect()
                self.addCourses.config(fg=self.sidePanelActive)

        self.addCourses = Label(self.coursesSidePanel, text="Add Course", bg=self.bluePrimColor, bd=0,
                                    fg=self.sidePanelActive, font=(self.font, 20, 'normal'))
        self.addCourses.place(x=20, y=15)
        self.addCourses.bind("<Button-1>", lambda e: addCoursesFun())


        def removeCoursesFun():
            deselect()
            self.removeCourses.config(fg=self.sidePanelActive)

        self.removeCourses = Label(self.coursesSidePanel, text="Remove Course", bg=self.bluePrimColor, bd=0,
                                   fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.removeCourses.place(x=20, y=75)
        self.removeCourses.bind("<Button-1>", lambda e: removeCoursesFun())

        def coursesListFun():
            deselect()
            self.coursesList.config(fg=self.sidePanelActive)

        self.coursesList = Label(self.coursesSidePanel, text="Courses List", bg=self.bluePrimColor, bd=0,
                                 fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.coursesList.place(x=20, y=135)
        self.coursesList.bind("<Button-1>", lambda e: coursesListFun())

    def destroy_courses_side_panel(self):
        self.coursesSidePanel.destroy()

    # this is "SETTINGS" side panel

    def settings_side_panel(self):
        self.settingsSidePanel = Frame(self.home_page_frame, bg=self.bluePrimColor, width=275, height=524)
        self.settingsSidePanel.place(x=21, y=103)

        def deselect():
            try:
                self.addAdmin.config(fg=self.sidePanelNonActive)
                self.removeAdmin.config(fg=self.sidePanelNonActive)
                self.changePassword.config(fg=self.sidePanelNonActive)
                self.changeUsername.config(fg=self.sidePanelNonActive)
            except:
                pass

        def addAdminFun():
            deselect()
            self.addAdmin.config(fg=self.sidePanelActive)

        self.addAdmin = Label(self.settingsSidePanel, text="Add Admin", bg=self.bluePrimColor, bd=0,
                                fg=self.sidePanelActive, font=(self.font, 20, 'normal'))
        self.addAdmin.place(x=20, y=15)
        self.addAdmin.bind("<Button-1>", lambda e: addAdminFun())

        def removeAdminFun():
            deselect()
            self.removeAdmin.config(fg=self.sidePanelActive)

        self.removeAdmin = Label(self.settingsSidePanel, text="Remove Admin", bg=self.bluePrimColor, bd=0,
                              fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.removeAdmin.place(x=20, y=75)
        self.removeAdmin.bind("<Button-1>", lambda e: removeAdminFun())

        def changePasswordFun():
            deselect()
            self.changePassword.config(fg=self.sidePanelActive)

        self.changePassword = Label(self.settingsSidePanel, text="Change Password", bg=self.bluePrimColor, bd=0,
                              fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.changePassword.place(x=20, y=135)
        self.changePassword.bind("<Button-1>", lambda e: changePasswordFun())

        def changeUsernameFun():
            deselect()
            self.changeUsername.config(fg=self.sidePanelActive)

        self.changeUsername = Label(self.settingsSidePanel, text="Change Username", bg=self.bluePrimColor, bd=0,
                              fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.changeUsername.place(x=20, y=195)
        self.changeUsername.bind("<Button-1>", lambda e: changeUsernameFun())

        def logoutFun():
            self.destroy()

        self.logout = Label(self.settingsSidePanel, text="Logout :)", bg=self.bluePrimColor, bd=0,
                              fg=self.sidePanelNonActive, font=(self.font, 15, 'normal'))
        self.logout.place(x=90, y=485)
        self.logout.bind("<Button-1>", lambda e: logoutFun())

    def destroy_settings_side_panel_frame(self):
        self.settingsSidePanel.destroy()

    def destroy_all_side_panel(self):
        try:
            self.destroy_attendance_side_panel()
        except:
            pass
        try:
            self.destroy_teacher_side_panel()
        except:
            pass
        try:
            self.destroy_student_side_panel()
        except:
            pass
        try:
            self.destroy_courses_side_panel()
        except:
            pass
        try:
            self.destroy_settings_side_panel_frame()
        except:
            pass




    # <!-----All Main Panels Are Here-----!>


    # <!-------Attendence Main Panels---------!>


    def yesterday_report_main_panel(self):

        textColor = "#0F4189"
        horizontalDivider = ImageTk.PhotoImage(file=("Assets/horizontalDivider.png"))

        rawData = [["BCA", 2002, 3000, 5002],
                   ["BBA", 2002, 3000, 5002],
                   ["MBA", 2002, 3000, 5002],
                   ["MCA", 2002, 3000, 5002],
                   ["PGDCA", 2002, 3000, 5002]]

        self.yesterday_main_panel = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.yesterday_main_panel.place(x=323, y=103)

        canvas = tk.Canvas(self.yesterday_main_panel, bg=self.ligBluePrimColor, bd=0, width=730, height=524,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=524)
        # content_frame = ttk.Frame(canvas)

        # self.scrollbar = ttk.Scrollbar(self.home_page_frame, orient=VERTICAL, command=canvas.yview)
        # self.scrollbar.grid(ipady=300, padx=1060)

        scrol = scrollbar(canvas, canvas, height=235)
        scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrol.get().set)

        canvas.place(x=0, y=0)

        self.date = Label(content_frame, text=f"Date:-{datetime.date.today() - timedelta(days=1)}",
                          bg=self.ligBluePrimColor, bd=0, font=(self.font, 15, 'normal'), justify="center")
        self.date.grid(row=0, columnspan=5, padx=300, pady=10)

        row = 0

        for data in rawData:
            Label(content_frame, text=data[0], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 25, 'bold'),
                  justify="center").grid(row=row + 1, columnspan=5, padx=200, pady=20)

            Label(content_frame, text="Present", fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'),
                  justify="center").grid(row=row + 2, column=0, pady=12, padx=70)

            Label(content_frame, text=data[1], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 3, column=0)

            Label(content_frame, text="Absent", fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'),
                  justify="center").grid(row=row + 2, column=1, padx=70)

            Label(content_frame, text=data[2], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 3, column=1)

            Label(content_frame, text="Total", fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 2, column=2, padx=70)

            Label(content_frame, text=data[3], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 3, column=2)

            horizontalbar = Label(content_frame, bg=self.ligBluePrimColor, bd=0, image=horizontalDivider)
            horizontalbar.photo = horizontalDivider
            horizontalbar.grid(row=row + 4, columnspan=5, pady=40)

            row += 4

    def destroy_yesterday_report_main_panel(self):
        self.yesterday_main_panel.destroy()

    def todays_report_main_panel(self):
        textColor = "#0F4189"
        horizontalDivider = ImageTk.PhotoImage(file=("Assets/horizontalDivider.png"))
        refreshButPng = ImageTk.PhotoImage(file=("Assets/Home_Page_Assets/todaypanel/refreshbutton.png"))

        rawData = [["BCA", 0, 0, 0],
                   ["BBA", 0, 0, 0],
                   ["MBA", 0, 0, 0],
                   ["MCA", 0, 0, 0],
                   ["PGDCA", 0, 0, 0]]

        self.todays_main_panel = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.todays_main_panel.place(x=323, y=103)

        message = Label(self.todays_main_panel, text="Students : 100/1000",
                       bg=self.ligBluePrimColor, bd=0, font=(self.font, 15, 'normal'), justify="center")
        message.place(x=290, y=7)

        def refresh():
            self.destroy_todays_report_main_panel()
            self.todays_report_main_panel()

        refreshBut = Button(self.todays_main_panel, bd=0, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor,image=refreshButPng, command=refresh)
        refreshBut.photo = refreshButPng
        refreshBut.place(x=650, y=5)

        canvas = tk.Canvas(self.todays_main_panel, bg=self.ligBluePrimColor, bd=0, width=730, height=485,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=485)
        # content_frame = ttk.Frame(canvas)

        # self.scrollbar = ttk.Scrollbar(self.home_page_frame, orient=VERTICAL, command=canvas.yview)
        # self.scrollbar.grid(ipady=300, padx=1060)

        scrol = scrollbar(canvas, canvas, height=215)
        scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrol.get().set)

        canvas.place(x=0, y=40)

        row = 0

        date = Label(content_frame, text=f"Date:-{datetime.date.today()}",
                     bg=self.ligBluePrimColor, bd=0, font=(self.font, 15, 'normal'), justify="center")
        date.grid(row=row, columnspan=5, padx=300, pady=10)

        for data in rawData:
            Label(content_frame, text=data[0], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 25, 'bold'),
                  justify="center").grid(row=row + 1, columnspan=5, padx=200, pady=20)

            Label(content_frame, text="Present", fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'),
                  justify="center").grid(row=row + 2, column=0, pady=12, padx=70)

            Label(content_frame, text=data[1], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 3, column=0)

            Label(content_frame, text="Absent", fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'),
                  justify="center").grid(row=row + 2, column=1, padx=70)

            Label(content_frame, text=data[2], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 3, column=1)

            Label(content_frame, text="Total", fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 2, column=2, padx=70)

            Label(content_frame, text=data[3], fg=textColor, bg=self.ligBluePrimColor, bd=0,
                  font=(self.font, 20, 'normal'), justify="center").grid(row=row + 3, column=2)

            horizontalbar = Label(content_frame, bg=self.ligBluePrimColor, bd=0, image=horizontalDivider)
            horizontalbar.photo = horizontalDivider
            horizontalbar.grid(row=row + 4, columnspan=5, pady=40)

            row += 4


    def destroy_todays_report_main_panel(self):
        self.todays_main_panel.destroy()

    def search_main_panel(self):
        self.search_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.search_main_frame.place(x=323, y=103)

        secondaryTextColor = "#474545"

        rawDate = str(datetime.date.today())
        date = rawDate.split("-")

        backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/searchpanel/background.png"))
        searchPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/searchpanel/buttons/search.png"))


        background = Label(self.search_main_frame, bg=self.ligBluePrimColor, bd=0, image=backgroundPng)
        background.photo = backgroundPng
        background.place(x=22, y=70)

        attLabel = Label(self.search_main_frame, text="Attendance", fg=self.orangePrimColor, bg=self.ligBluePrimColor, bd=0, font=(self.font, 30, "normal"))
        attLabel.place(x=180, y=7)

        mangeLabel = Label(self.search_main_frame, text="Manager", fg=secondaryTextColor, bg=self.ligBluePrimColor,
                         bd=0, font=(self.font, 30, "normal"))
        mangeLabel.place(x=400, y=7)

        dayLabel = Label(self.search_main_frame, text="Day :", fg="white", bg=self.bluePrimColor,
                           bd=0, font=(self.font, 25, "normal"))
        dayLabel.place(x=50, y=75)

        dayEntry = Entry(self.search_main_frame, fg=secondaryTextColor, bg=self.ligBluePrimColor, width=7, bd=0, font=(self.font, 15, "normal"), justify="center")
        dayEntry.place(x=135, y=85)

        monthLabel = Label(self.search_main_frame, text="Month :", fg="white", bg=self.bluePrimColor,
                         bd=0, font=(self.font, 25, "normal"))
        monthLabel.place(x=228, y=75)

        monthEntry = Entry(self.search_main_frame, fg=secondaryTextColor, bg=self.ligBluePrimColor, width=7, bd=0,
                         font=(self.font, 15, "normal"), justify="center")
        monthEntry.place(x=347, y=85)

        yearLabel = Label(self.search_main_frame, text="Year :", fg="white", bg=self.bluePrimColor,
                           bd=0, font=(self.font, 25, "normal"))
        yearLabel.place(x=440, y=75)

        yearEntry = Entry(self.search_main_frame, fg=secondaryTextColor, bg=self.ligBluePrimColor, width=7, bd=0,
                           font=(self.font, 15, "normal"), justify="center")
        yearEntry.place(x=535, y=85)

        currentYear = int(date[0])
        currentDay = int(date[2])
        currentMonth = int(date[1])

        dayEntry.insert(0, int(date[2]))
        monthEntry.insert(0, int(date[1]))
        yearEntry.insert(0, int(date[0]))

        messageLabel =  Label(self.search_main_frame, text="Search Attendance for Specific Date :)", fg=secondaryTextColor, bg=self.ligBluePrimColor,
                         bd=0, font=(self.font, 12, "normal"))
        messageLabel.place(x=230, y=140)

        def search(day, month, year):
            messageLabel.config(fg=secondaryTextColor, text="Search Attendance for Specific Date :)")
            if year <= currentYear:
                if year == currentYear:
                    if month <= currentMonth:
                        if month <= 12 and month >= 1:
                            if day >= 1 and day <= daysOfMonth(month, year):
                                if month == currentMonth:
                                    if day <= currentDay:
                                        SearchStep1(parent=self.search_main_frame, day=day, month=month, year=year).draw()
                                    else:
                                        messageLabel.config(fg="red", text="*Enter valid date (day)")
                                else:
                                    if day >= 1 and day <= daysOfMonth(month, year):
                                        SearchStep1(parent=self.search_main_frame,
                                                    day=day, month=month, year=year).draw()
                                    else:
                                        messageLabel.config(fg="red", text="*Enter valid date (day)")
                            else:
                                messageLabel.config(fg="red", text="*Enter valid date (day)")
                        else:
                            messageLabel.config(fg="red", text="*There are only 12 months in a year")
                    else:
                        messageLabel.config(fg="red", text="*Month is not Valid")
                else:
                    if month <= 12 and month >= 1:
                        if day >= 1 and day <= daysOfMonth(month, year):
                            SearchStep1(parent=self.search_main_frame,
                                        day=day, month=month, year=year).draw()
                        else:
                            messageLabel.config(fg="red", text="*Enter valid date (day)")
                    else:
                        messageLabel.config(fg="red", text="*There are only 12 months in a year")
            else:
                messageLabel.config(fg="red", text="*enter correct year!")

        searchButt = Button(self.search_main_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=searchPng, command=lambda: search(int(dayEntry.get()), int(monthEntry.get()), int(yearEntry.get())))
        searchButt.photo = searchPng
        searchButt.place(x=645, y=85)


    def destroy_search_main_panel(self):
        self.search_main_frame.destroy()


            # <!---------Teacher Main Panels----------!>


    def add_teacher_main_panel(self):
        self.add_teacher_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.add_teacher_frame.place(x=323, y=103)

        backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/teacherpanel/background.png"))
        addPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/teacherpanel/buttons/add.png"))

        background = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, image=backgroundPng)
        background.photo = backgroundPng
        background.place(x=100, y=60)

        nameLabel = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="black", text="Full Name", font=(self.font, 15, "normal"))
        nameLabel.place(x=100, y=30)

        nameEntry = Entry(self.add_teacher_frame, bg="white", bd=0, width=14, justify="center", font=(self.font, 21, 'normal'))
        nameEntry.place(x=109.5, y=64)

        usernameLabel = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="black", text="Username",
                          font=(self.font, 15, "normal"))
        usernameLabel.place(x=400, y=30)

        usernameEntry = Entry(self.add_teacher_frame, bg="white", bd=0, width=14, justify="center",
                          font=(self.font, 21, 'normal'))
        usernameEntry.place(x=411, y=64)

        emailLabel = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="black", text="E-mail",
                              font=(self.font, 15, "normal"))
        emailLabel.place(x=100, y=143)

        emailEntry = Entry(self.add_teacher_frame, bg="white", bd=0, width=14, justify="center",
                              font=(self.font, 21, 'normal'))
        emailEntry.place(x=109.5, y=176)

        passwordLabel = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="black", text="Password",
                           font=(self.font, 15, "normal"))
        passwordLabel.place(x=400, y=143)

        passwordEntry = Entry(self.add_teacher_frame, bg="white", bd=0, width=14, justify="center",
                           font=(self.font, 21, 'normal'), show="*")
        passwordEntry.place(x=411, y=176)

        phoneLabel = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="black", text="Phone No.",
                              font=(self.font, 15, "normal"))
        phoneLabel.place(x=100, y=261)

        phoneEntry = Entry(self.add_teacher_frame, bg="white", bd=0, width=14, justify="center",
                              font=(self.font, 21, 'normal'))
        phoneEntry.place(x=109.5, y=293)

        confirmPassLabel = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="black", text="Confirm Password",
                           font=(self.font, 15, "normal"))
        confirmPassLabel.place(x=400, y=261)

        confirmPassEntry = Entry(self.add_teacher_frame, bg="white", bd=0, width=14, justify="center",
                           font=(self.font, 21, 'normal'), show="*")
        confirmPassEntry.place(x=411, y=293)

        error1 = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="red", text="", font=(self.font, 10, 'normal'))
        error1.place(x=110, y=108)

        error2 = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error2.place(x=412, y=108)

        error3 = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error3.place(x=110, y=220)

        error4 = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error4.place(x=412, y=220)

        error5 = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error5.place(x=110, y=336)

        error6 = Label(self.add_teacher_frame, bg=self.ligBluePrimColor, bd=0, fg="red", text="",
                       font=(self.font, 10, 'normal'))
        error6.place(x=412, y=336)

        def clear_error():
            error1.config(text="") #name
            error2.config(text="") #username
            error3.config(text="") #email
            error4.config(text="") #password
            error5.config(text="") #phone no.
            error6.config(text="") #confirmpass

        def add_fun():
            clear_error()
            validate = True
            name = nameEntry.get()
            username = usernameEntry.get()
            email = emailEntry.get()
            password = passwordEntry.get()
            phone = phoneEntry.get()
            confirmPass = confirmPassEntry.get()

            if len(name) < 4 or len(name) > 25:
                validate = False
                error1.config(text="*name character's should be(4-25)")

            if len(username) < 4 or len(username) > 12:
                validate = False
                error2.config(text="*username character's should be(4-12)")
            # verify duplicate username

            if len(email) < 5:
                validate = False
                error3.config(text="*enter valid email")

            if len(password) < 8 or len(password) > 18:
                validate = False
                error4.config(text="*password character's should be(8-18)")

            if len(phone) == 10:
                num = list(phone)
                for d in num:
                    asa = ord(d)
                    for i in range(47, 59):
                        if asa == i:
                            break
                        elif i > 57:
                            validate = False
                            error5.config(text="*enter valid number")
            else:
                validate = False
                error5.config(text="*enter valid number")

            if len(confirmPass) > 0:
                if confirmPass != password:
                    validate = False
                    error6.config(text="*password not match")
            else:
                validate = False
                error6.config(text="*don't leave this field blank")

            if validate:
                # fire your query here!
                clear_error()
                print("Done!")



        addButton = Button(self.add_teacher_frame, bg=self.ligBluePrimColor, activebackground=self.ligBluePrimColor, bd=0, image=addPng, command=add_fun)
        addButton.photo = addPng
        addButton.place(x=328, y=420)


    def destroy_add_teacher_main_panel(self):
        self.add_teacher_frame.destroy()

    def destroy_all_main_panel(self):
        try:
            self.destroy_yesterday_report_main_panel()
        except:
            pass
        try:
            self.destroy_todays_report_main_panel()
        except:
            pass
        try:
            self.destroy_search_main_panel()
        except:
            pass
        try:
            self.destroy_add_teacher_main_panel()
        except:
            pass