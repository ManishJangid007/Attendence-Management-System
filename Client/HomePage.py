from tkinter import *
from PIL import ImageTk, Image
from Pages.MarkAttendance.SelectSubjectPage import SelectSubjectPage
from ServerSide.SelectOperation import SelectOperation
from Pages.SearchAttendance.SearchPage import SearchPage
from Pages.TodayReport.TodayReportPage import TodayReportPage
from Pages.YesterdayReport.YesterdayReportPage import YesterdayReportPage
from Pages.TeacherList.TeacherListPage import TeacherListPage
from Pages.StudentList.StudentListPage import StudentListPage
from Pages.CourseList.CourseListPage import CourseListPage
from Pages.Account.AccountPage import AccountPage

class HomePage():
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.backgroundPng = ImageTk.PhotoImage(
            file=(
                "Assets/Home_Page_Assets/background.png"
            )
        )
        self.logoutButPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Home_Page_Assets/Buttons/logout.png"
            )
        )
        self.ligBluePrimColor = "#F2F8FF"
        self.menu_bar_color = "#F78888"
        self.side_panel_color = "#FBE8A6"
        self.font = "Bahnschrift"
        self.sidePanelActive = "#1E1E1E"
        self.sidePanelNonActive = "grey"

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

        self.side_panel()

    def destroy(self):
        self.home_page_frame.destroy()

    def side_panel(self):
        self.SidePanel = Frame(self.home_page_frame, bg=self.side_panel_color, width=275, height=524)
        self.SidePanel.place(x=21, y=103)

        searchPng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Home_Page_Assets/Buttons/search.png"
            )
        )

        searchNonActivePng = ImageTk.PhotoImage(
            Image.open(
                "Assets/Home_Page_Assets/Buttons/searchnonactive.png"
            )
        )

        def deselect():
            self.search.config(fg=self.sidePanelNonActive)
            self.searchIcon.config(image=searchNonActivePng)
            self.searchIcon.photo = searchNonActivePng
            self.markAtt.config(fg=self.sidePanelNonActive)
            self.todayReport.config(fg=self.sidePanelNonActive)
            self.yesterdayReport.config(fg=self.sidePanelNonActive)
            self.teachersList.config(fg=self.sidePanelNonActive)
            self.studentsList.config(fg=self.sidePanelNonActive)
            self.coursesList.config(fg=self.sidePanelNonActive)
            self.account.config(fg=self.sidePanelNonActive)

        self.search_main_panel()

        def searchFun():
            deselect()
            self.searchIcon.config(image=searchPng)
            self.searchIcon.photo = searchPng
            self.search.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.search_main_panel()

        self.searchIcon = Label(self.SidePanel, bd=0, bg=self.side_panel_color, image=searchPng)
        self.searchIcon.photo = searchPng
        self.searchIcon.place(x=18, y=24)
        self.searchIcon.bind("<Button-1>", lambda e: searchFun())

        self.search = Label(self.SidePanel, text="Search", bg=self.side_panel_color, bd=0,
                            fg=self.sidePanelActive, font=(self.font, 20, 'normal'))
        self.search.place(x=60, y=19)
        self.search.bind("<Button-1>", lambda e: searchFun())

        def markAtt():
            deselect()
            self.markAtt.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.mark_attendance_panel()

        self.markAtt = Label(self.SidePanel, text="Mark Attendance", bg=self.side_panel_color, bd=0,
                                 fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.markAtt.place(x=20, y=75)
        self.markAtt.bind("<Button-1>", lambda e: markAtt())

        def todayReportFun():
            deselect()
            self.todayReport.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.today_report_main_panel()

        self.todayReport = Label(self.SidePanel, text="Today's Report", bg=self.side_panel_color, bd=0,
                                 fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.todayReport.place(x=20, y=135)
        self.todayReport.bind("<Button-1>", lambda e: todayReportFun())

        def yesterdayReportFun():
            deselect()
            self.yesterdayReport.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.yesterday_report_main_panel()

        self.yesterdayReport = Label(self.SidePanel, text="Yesterday's Report", bg=self.side_panel_color, bd=0,
                                     fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.yesterdayReport.place(x=20, y=195)
        self.yesterdayReport.bind("<Button-1>", lambda e: yesterdayReportFun())

        def teacherListFun():
            deselect()
            self.teachersList.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.teacher_list_main_panel()

        self.teachersList = Label(self.SidePanel, text="Teacher's List", bg=self.side_panel_color, bd=0,
                                     fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.teachersList.place(x=20, y=255)
        self.teachersList.bind("<Button-1>", lambda e: teacherListFun())

        def studentListFun():
            deselect()
            self.studentsList.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.student_list_main_panel()

        self.studentsList = Label(self.SidePanel, text="Student's List", bg=self.side_panel_color, bd=0,
                                  fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.studentsList.place(x=20, y=315)
        self.studentsList.bind("<Button-1>", lambda e: studentListFun())

        def courseListFun():
            deselect()
            self.coursesList.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.course_list_main_panel()

        self.coursesList = Label(self.SidePanel, text="Course's List", bg=self.side_panel_color, bd=0,
                                  fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.coursesList.place(x=20, y=375)
        self.coursesList.bind("<Button-1>", lambda e: courseListFun())

        def accountFun():
            deselect()
            self.account.config(fg=self.sidePanelActive)
            self.destroy_all_main_panel()
            self.account_main_panel()

        self.account = Label(self.SidePanel, text="Account", bg=self.side_panel_color, bd=0,
                                 fg=self.sidePanelNonActive, font=(self.font, 20, 'normal'))
        self.account.place(x=20, y=435)
        self.account.bind("<Button-1>", lambda e: accountFun())

        # <!--------All Main Panel's Start's From Here---------!>

    def search_main_panel(self):
        self.search_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.search_main_frame.place(x=323, y=103)

        SearchPage(self.search_main_frame).draw()

    def mark_attendance_panel(self):
        self.mark_attendance_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.mark_attendance_main_frame.place(x=323, y=103)

        SelectSubjectPage(self.mark_attendance_main_frame, self.username).draw()

    def today_report_main_panel(self):
        self.today_report_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.today_report_main_frame.place(x=323, y=103)

        TodayReportPage(self.today_report_main_frame).draw()

    def yesterday_report_main_panel(self):
        self.yesterday_report_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.yesterday_report_main_frame.place(x=323, y=103)

        YesterdayReportPage(self.yesterday_report_main_frame).draw()

    def teacher_list_main_panel(self):
        self.teacher_list_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.teacher_list_main_frame.place(x=323, y=103)

        TeacherListPage(self.teacher_list_main_frame).draw()

    def student_list_main_panel(self):
        self.student_list_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.student_list_main_frame.place(x=323, y=103)

        StudentListPage(self.student_list_main_frame).draw()

    def course_list_main_panel(self):
        self.course_list_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.course_list_main_frame.place(x=323, y=103)

        CourseListPage(self.course_list_main_frame).draw()

    def account_main_panel(self):
        self.account_main_frame = Frame(self.home_page_frame, bg=self.ligBluePrimColor, width=730, height=524)
        self.account_main_frame.place(x=323, y=103)

        AccountPage(self.account_main_frame).draw()

    def destroy_all_main_panel(self):
        try:
            self.search_main_frame.destroy()
        except:
            pass
        try:
            self.mark_attendance_main_frame.destroy()
        except:
            pass
        try:
            self.today_report_main_frame.destroy()
        except:
            pass
        try:
            self.yesterday_report_main_frame.destroy()
        except:
            pass
        try:
            self.teacher_list_main_frame.destroy()
        except:
            pass
        try:
            self.student_list_main_frame.destroy()
        except:
            pass
        try:
            self.course_list_main_frame.destroy()
        except:
            pass
        try:
            self.account_main_frame.destroy()
        except:
            pass