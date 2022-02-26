from tkinter import *
from PIL import ImageTk
from Admin.teacherPanelFrame.addTeacherPage import AddTeacherPage
from Admin.teacherPanelFrame.teacherListPage import TeacherListPage
from Admin.attendancePanelFrame.searchPage import SearchPage
from Admin.attendancePanelFrame.todayReportPage import TodayReportPage
from Admin.attendancePanelFrame.yesterdayReportPage import YesterdayReportPage
from Admin.studentPanelFrame.addStudentPage import AddStudentPage
from Admin.studentPanelFrame.studentListPage import StudentListPage

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

        def teacherListFun():
            deselect()
            self.teacherlist.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.teacher_list_main_panel()

        self.teacherlist = Label(self.teacherSidePanel, text="Teacher's List", bg=self.bluePrimColor, bd=0,
                                   fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.teacherlist.place(x=20, y=75)
        self.teacherlist.bind("<Button-1>", lambda e: teacherListFun())

    def destroy_teacher_side_panel(self):
        self.teacherSidePanel.destroy()

    # this is "STUDENT'S" side panel

    def student_side_panel(self):
        self.studentSidePanel = Frame(self.home_page_frame, bg=self.bluePrimColor, width=275, height=524)
        self.studentSidePanel.place(x=21, y=103)

        self.add_student_main_panel()

        def deselect():
            try:
                self.addStudent.config(fg=self.sidePanelNonActive)
                self.studentList.config(fg=self.sidePanelNonActive)
            except:
                pass

        def addStudentFun():
            deselect()
            self.addStudent.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.add_student_main_panel()

        self.addStudent = Label(self.studentSidePanel, text="Add Student", bg=self.bluePrimColor, bd=0,
                                fg=self.sidePanelActive, font=(self.font, 20, 'normal'))
        self.addStudent.place(x=20, y=15)
        self.addStudent.bind("<Button-1>", lambda e: addStudentFun())

        def studentListFun():
            deselect()
            self.studentList.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.student_list_main_panel()

        self.studentList = Label(self.studentSidePanel, text="Student's List", bg=self.bluePrimColor, bd=0,
                                 fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.studentList.place(x=20, y=75)
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
        self.yesterday_main_panel = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.yesterday_main_panel.place(x=323, y=103)

        YesterdayReportPage(self.yesterday_main_panel).draw()

    def destroy_yesterday_report_main_panel(self):
        self.yesterday_main_panel.destroy()

    def todays_report_main_panel(self):
        self.todays_main_panel = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.todays_main_panel.place(x=323, y=103)

        TodayReportPage(self.todays_main_panel).draw()

    def destroy_todays_report_main_panel(self):
        self.todays_main_panel.destroy()

    def search_main_panel(self):
        self.search_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.search_main_frame.place(x=323, y=103)

        SearchPage(self.search_main_frame).draw()

    def destroy_search_main_panel(self):
        self.search_main_frame.destroy()


            # <!---------Teacher Main Panels----------!>


    def add_teacher_main_panel(self):
        self.add_teacher_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.add_teacher_frame.place(x=323, y=103)

        AddTeacherPage(self.add_teacher_frame).draw()

    def destroy_add_teacher_main_panel(self):
        self.add_teacher_frame.destroy()

    def teacher_list_main_panel(self):
        self.teacher_list_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.teacher_list_frame.place(x=323, y=103)

        TeacherListPage(self.teacher_list_frame).draw()


    def destroy_teacher_list_main_panel(self):
        self.teacher_list_frame.destroy()

    def add_student_main_panel(self):
        self.add_student_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.add_student_frame.place(x=323, y=103)

        AddStudentPage(self.add_student_frame).draw()

    def destroy_add_student_main_panel(self):
        self.add_student_frame.destroy()

    def student_list_main_panel(self):
        self.student_list_frame = Frame(self.home_page_frame, bg="red", width=730, height=524)
        self.student_list_frame.place(x=323, y=103)

        StudentListPage(self.student_list_frame).draw()

    def destroy_student_list_main_panel(self):
        self.student_list_frame.destroy()

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
        try:
            self.destroy_teacher_list_main_panel()
        except:
            pass
        try:
            self.destroy_add_student_main_panel()
        except:
            pass
        try:
            self.destroy_student_list_main_panel()
        except:
            pass