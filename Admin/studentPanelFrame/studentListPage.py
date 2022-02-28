from tkinter import *
from PIL import ImageTk, Image
from Admin.studentPanelFrame.searchResult import SearchResultPage

class StudentListPage():
    def __init__(self, parent):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.menuActive = "#000000"
        self.menuNonActive = "#606060"
        self.font = "Bahnschrift"
        self.searchbarPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/searchbar.png"))
        self.searchButPng = ImageTk.PhotoImage(Image.open("Assets/Home_Page_Assets/studentpanel/buttons/search.png"))
        self.dividerPng = ImageTk.PhotoImage(Image.open("Assets/horizontalDivider.png"))
        self.cArray = [Label()]
        self.yArray = [Label()]
        self.sYArray = [Label()]

    def draw(self):
        searchbar = Label(self.parent, bd=0, bg=self.ligBluePrimColor, image=self.searchbarPng)
        searchbar.photo = self.searchbarPng
        searchbar.place(x=48, y=35)

        rawData = [["BCA", 3],
                   ["BBA", 3],
                   ["MBA", 2],
                   ["MCA", 2],
                   ["PGDCA", 2],
                   ["Fashion Designing", 1],
                   ["Interior Designing", 4],
                   ["B.Com", 3],
                   ["M.Com", 2],
                   ["B.Tech", 3],
                   ["M.Tech", 5],
                   ["Hotel Management", 3]]

        courseLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg="white", text="Course :",
                            font=(self.font, 25, 'normal'))
        courseLabel.place(x=60, y=40)

        courseEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=13, justify="center",
                               font=(self.font, 19, 'normal'))
        courseEntry.place(x=205, y=47)

        yearLabel = Label(self.parent, bd=0, bg=self.bluePrimColor, fg="white", text="Year :",
                            font=(self.font, 25, 'normal'))
        yearLabel.place(x=410, y=40)

        yearEntry = Entry(self.parent, bg=self.ligBluePrimColor, bd=0, width=5, justify="center",
                            font=(self.font, 19, 'normal'))
        yearEntry.place(x=514, y=47)

        cFrame = Frame(self.parent, bg=self.ligBluePrimColor, width=635, height=220)
        cFrame.place(x=50, y=120)

        divider = Label(self.parent, bg=self.ligBluePrimColor, bd=0, image=self.dividerPng)
        divider.photo = self.dividerPng
        divider.place(x=150, y=360)

        yFrame = Frame(self.parent, bg=self.ligBluePrimColor, width=635, height=60)
        yFrame.place(x=250, y=380)

        def selectYear(label, data):
            try:
                self.sYArray[0].config(fg=self.menuNonActive)
            except:
                pass
            label.config(fg=self.menuActive)
            yearEntry.delete(0, END)
            yearEntry.insert(0, data)
            self.sYArray[0] = label

        def drawYear(row, col, data, initial):
            eff = "st"
            if data == 2:
                eff = "nd"
            elif data == 3:
                eff = "rd"
            elif data >= 4:
                eff = "th"

            if initial == 0:
                color = self.menuActive
                yearEntry.insert(0, data)
            else:
                color = self.menuNonActive

            l = Label(yFrame, bg=self.ligBluePrimColor, bd=0, fg=color, text=f"{data}{eff}",
                      font=(self.font, 17, 'normal'))
            l.grid(row=row, column=col, padx=20, pady=5)
            l.bind("<Button-1>", lambda e: selectYear(l, data))
            self.yArray.append(l)
            if initial == 0:
                self.sYArray[0] = l

        def selectCourse(label, data):
            try:
                for lab in self.yArray:
                    lab.destroy()
            except:
                pass
            try:
                self.cArray[0].config(fg=self.menuNonActive)
            except:
                pass
            label.config(fg=self.menuActive)
            self.cArray[0] = label
            courseEntry.delete(0, END)
            yearEntry.delete(0, END)
            courseEntry.insert(0, data[0])
            col = 0
            row = 0
            initial = 0
            for d in range(1, data[1]+1):
                drawYear(row, col, data=d, initial=initial)
                col += 1
                initial += 1
                if col == 3:
                    row += 1
                    col = 0

        def drawCourse(row, col, data, initial):
            if initial == 0:
                color = self.menuActive
            else:
                color = self.menuNonActive
            l = Label(cFrame, bg=self.ligBluePrimColor, bd=0, fg=color, text=data[0], font=(self.font, 17, 'normal'))
            l.grid(row=row, column=col, padx=10, pady=5)
            l.bind("<Button-1>", lambda e: selectCourse(l, data))
            if initial == 0:
                self.cArray[0] = l
                courseEntry.insert(0, data[0])
                col = 0
                initial1 = 0
                for i in range(1, data[1]+1):
                    drawYear(0, col, i, initial1)
                    col += 1
                    initial1 += 1

        row = 0
        col = 0
        initial = 0
        for d in rawData:
            drawCourse(row, col, d, initial)
            initial += 1
            if col == 3:
                row += 1
                col = 0
            col += 1

        def search(parent, course, year):
            SearchResultPage(parent, course, year).draw()

        searchBut = Button(self.parent, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=self.searchButPng, command=lambda : search(self.parent, courseEntry.get(), int(yearEntry.get())))
        searchBut.photo = self.searchButPng
        searchBut.place(x=620, y=48)
