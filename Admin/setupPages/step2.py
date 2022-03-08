from tkinter import ttk
import tkinter as tk
from setupPages.step3 import Step3
from tkinter import *
from PIL import ImageTk, Image
from ServerSide.Connection import *
from ChangeParaPage import ParaPage

class Step2():
    def __init__(self, root, onthis, parent):
        self.parent = parent
        self.onthis = onthis
        self.root = root
        self.textColor = "#333030"
        self.font = "Bahnschrift"
        self.headBackColor = "#E5E5E5"
        self.backgroundPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step2/background.png"))
        self.backButPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step2/Button/back.png"))
        self.startButPng = ImageTk.PhotoImage(Image.open("Assets/Setup_Page_Assets/Step2/Button/start.png"))
        self.setConButPng = ImageTk.PhotoImage(file=("Assets/Setup_Page_Assets/Buttons/configureconn.png"))

    def draw(self):
        self.step2_frame = Frame(self.root, bg="white", width=1080, height=650)
        self.step2_frame.place(x=0, y=0)

        self.background = Label(self.step2_frame, bg="white", bd=0, image=self.backgroundPng)
        self.background.photo = self.backgroundPng
        self.background.place(x=-98, y=-50)

        self.headLabel = Label(self.step2_frame, fg=self.textColor, text="You Need to Follow Some Steps \n To Setup Environment.", bd=0,
                                 bg=self.headBackColor, font=(self.font, 30, "normal"), justify="left")
        self.headLabel.place(x=340, y=80)

        def back():
            self.destroy()

        self.backBut = Button(self.step2_frame, bg="white", activebackground="white", bd=0,
                               image=self.backButPng, command=back)
        self.backBut.photo = self.backButPng
        self.backBut.place(x=170, y=10)

        if self.onthis:
            self.instruc = "1. Lorem Ipsum Lorem Ipsum Lorem Ipsum hfn\n\n" \
                           "2. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n"

        else:
            self.instruc = "1. Lorem Ipsum Lorem Ipsum Lorem Ipsum hfn\n\n" \
                           "200. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n" \
                           "3. Lorem Ipsum Lorem Ipsum Lorem Ipsum\n\n"

        # Scrollable Panel

        canvas = tk.Canvas(self.step2_frame, bg="white", bd=0, width=430, height=355, highlightthickness=0)


        content_frame = Frame(canvas, bg="white", width=430, height=355)
        #content_frame = ttk.Frame(canvas)

        scrollbar = ttk.Scrollbar(self.step2_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.grid(ipady=300, padx=1060)

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

        canvas.create_window((0,0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.place(x=595, y=255)

        insHeadLabel = Label(content_frame, bd=0, bg="white", text="{ Instructions }", justify="center", font=(self.font, 20, 'normal'))
        insHeadLabel.grid(row=0, column=1, padx=5)

        instructions =  Label(content_frame, bd=0, fg=self.textColor, bg="white", text=self.instruc, justify="left", font=(self.font, 15, 'normal'))
        instructions.grid(row=1, column=0, columnspan=3, padx=5, pady=8)

        def startSetup():
            try:
                self.errorMessage.destroy()
            except:
                pass
            if Connection().check():
                if Connection().check_database():
                    self.errorMessage = Label(content_frame, bd=0, bg="white", fg="green", text="*Another Instance of Database Found\nGo Back And Try To Reconnect",
                                              justify="center", font=(self.font, 10, 'normal'))
                    self.errorMessage.grid(row=2, column=1, pady=2)
                else:
                    Step3(self.root, self.step2_frame).draw()
            else:
                self.errorMessage = Label(content_frame, bd=0, bg="white", fg="red", text="*Cannot Find The Server", justify="center", font=(self.font, 10, 'normal'))
                self.errorMessage.grid(row=2, column=1, pady=2)

        self.setConBut = Button(content_frame, bg="white", activebackground="white", bd=0,
                                image=self.setConButPng,
                                command=lambda: ParaPage(self.root, content_frame, destroy_Parent=False).draw())
        self.setConBut.photo = self.setConButPng
        self.setConBut.grid(row=3, column=1, padx=5)

        startBut = Button(content_frame, bg="white", activebackground="white", bd=0,
                                 image=self.startButPng, command=startSetup)
        # startBut.photo = self.startButPng
        startBut.grid(row=4, column=1, padx=5)

    def destroy(self):
        self.step2_frame.destroy()
