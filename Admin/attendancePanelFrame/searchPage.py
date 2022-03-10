from attendancePanelFrame.searchPanelFrames.step1 import SearchStep1
import datetime
from tkinter import *
from PIL import ImageTk, Image
from daysOnMonth import daysOfMonth

class SearchPage():
    def __init__(self, parent, grandParent):
        self.parent = parent
        self.grandParent = grandParent
        self.font = "Bahnschrift"
        self.bluePrimColor = "#87A0C4"
        self.ligBluePrimColor = "#F2F8FF"
        self.orangePrimColor = "#FF8C64"

    def draw(self):
        secondaryTextColor = "#474545"
        rawDate = str(datetime.date.today())
        date = rawDate.split("-")

        backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/searchpanel/background.png"))
        searchPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/searchpanel/buttons/search.png"))

        background = Label(self.parent, bg=self.ligBluePrimColor, bd=0, image=backgroundPng)
        background.photo = backgroundPng
        background.place(x=22, y=70)

        attLabel = Label(self.parent, text="Attendance", fg=self.orangePrimColor, bg=self.ligBluePrimColor,
                         bd=0, font=(self.font, 30, "normal"))
        attLabel.place(x=180, y=7)

        mangeLabel = Label(self.parent, text="Manager", fg=secondaryTextColor, bg=self.ligBluePrimColor,
                           bd=0, font=(self.font, 30, "normal"))
        mangeLabel.place(x=400, y=7)

        dayLabel = Label(self.parent, text="Day :", fg="white", bg=self.bluePrimColor,
                         bd=0, font=(self.font, 25, "normal"))
        dayLabel.place(x=50, y=75)

        dayEntry = Entry(self.parent, fg=secondaryTextColor, bg=self.ligBluePrimColor, width=7, bd=0,
                         font=(self.font, 15, "normal"), justify="center")
        dayEntry.place(x=135, y=85)

        monthLabel = Label(self.parent, text="Month :", fg="white", bg=self.bluePrimColor,
                           bd=0, font=(self.font, 25, "normal"))
        monthLabel.place(x=228, y=75)

        monthEntry = Entry(self.parent, fg=secondaryTextColor, bg=self.ligBluePrimColor, width=7, bd=0,
                           font=(self.font, 15, "normal"), justify="center")
        monthEntry.place(x=347, y=85)

        yearLabel = Label(self.parent, text="Year :", fg="white", bg=self.bluePrimColor,
                          bd=0, font=(self.font, 25, "normal"))
        yearLabel.place(x=440, y=75)

        yearEntry = Entry(self.parent, fg=secondaryTextColor, bg=self.ligBluePrimColor, width=7, bd=0,
                          font=(self.font, 15, "normal"), justify="center")
        yearEntry.place(x=535, y=85)

        currentYear = int(date[0])
        currentDay = int(date[2])
        currentMonth = int(date[1])

        dayEntry.insert(0, str(date[2]))
        monthEntry.insert(0, str(date[1]))
        yearEntry.insert(0, str(date[0]))

        messageLabel = Label(self.parent, text="Search Attendance for Specific Date :)",
                             fg=secondaryTextColor, bg=self.ligBluePrimColor,
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
                                        SearchStep1(parent=self.parent, grandParent=self.grandParent,day=day, month=month,
                                                    year=year).draw()
                                    else:
                                        messageLabel.config(fg="red", text="*Enter valid date (day)")
                                else:
                                    if day >= 1 and day <= daysOfMonth(month, year):
                                        SearchStep1(parent=self.parent, grandParent=self.grandParent,
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
                            SearchStep1(parent=self.parent, grandParent=self.grandParent,
                                        day=day, month=month, year=year).draw()
                        else:
                            messageLabel.config(fg="red", text="*Enter valid date (day)")
                    else:
                        messageLabel.config(fg="red", text="*There are only 12 months in a year")
            else:
                messageLabel.config(fg="red", text="*enter correct year!")

        searchButt = Button(self.parent, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor,
                            image=searchPng,
                            command=lambda: search(int(dayEntry.get()), int(monthEntry.get()), int(yearEntry.get())))
        searchButt.photo = searchPng
        searchButt.place(x=645, y=85)