from tkinter import *
import tkinter as tk
from Scrollbar import scrollbar
from PIL import ImageTk, Image
from ServerSide.SelectOperation import SelectOperation
from ServerSide.UpdateOperation import UpdateOperation
from tkinter import messagebox

class AdminsPage():
    def __init__(self, parent):
        self.parent = parent
        self.ligBluePrimColor = "#F2F8FF"
        self.bluePrimColor = "#87A0C4"
        self.textColor = "#0F4189"
        self.font = "Bahnschrift"
        self.tilePng = self.cardPng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/tile.png"))
        self.removePng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/buttons/remove.png"))
        self.blockPng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/buttons/block.png"))
        self.unblockPng = ImageTk.PhotoImage(
            Image.open("Assets/Home_Page_Assets/settingspanel/buttons/unblock.png"))

    def draw(self):
        self.admins_frame = Frame(self.parent, bg=self.ligBluePrimColor, width=730, height=524)
        self.admins_frame.place(x=0, y=0)
        canvas = tk.Canvas(self.admins_frame, bg=self.ligBluePrimColor, bd=0, width=730, height=520,
                           highlightthickness=0)

        content_frame = Frame(canvas, bg=self.ligBluePrimColor, width=730, height=520)

        self.scrol = scrollbar(canvas, canvas, height=235)
        self.scrol.draw()

        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrol.get().set)

        canvas.place(x=0, y=0)

        def blockUnblock(username):
            if SelectOperation().isBlocked(username):
                if UpdateOperation().unBlockAdmin(username):
                    self.refresh()
                    messagebox.showinfo(title="Success", message=f"Admin {username} Unblocked Successfully")
                else:
                    messagebox.showerror(title="Error Occurred", message="Something Went Wrong !")
            else:
                if UpdateOperation().blockAdmin(username):
                    self.refresh()
                    messagebox.showinfo(title="Success", message=f"Admin {username} Blocked Successfully")
                else:
                    messagebox.showerror(title="Error Occurred", message="Something Went Wrong !")

        def remove(username):
            if messagebox.askyesno(title="Warning !", message="This Action Can't Be Undone, Are you Sure"):
                if UpdateOperation().deleteAdmin(username):
                    self.refresh()
                    messagebox.showinfo(title="Success", message=f"Admin '{username}' Profile Deleted Successfully")
                else:
                    messagebox.showerror(title="Error Occurred", message="Something Went Wrong !")

        def drawTile(row, user):
            t = Label(content_frame, bd=0, bg=self.ligBluePrimColor, image=self.tilePng)
            t.photo = self.tilePng
            t.grid(row=row, columnspan=3, pady=10, padx=20)

            isHigh = SelectOperation().isPriorityHigh(user)

            if isHigh:
                l = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="black", text=f"{user}",
                          font=(self.font, 20, 'bold'))
                l.grid(row=row, column=0, columnspan=3, padx=30)
            else:
                l = Label(content_frame, bd=0, bg=self.bluePrimColor, fg="black", text=user, font=(self.font, 15, 'normal'))
                l.grid(row=row, column=0, sticky='w', padx=30)

            if SelectOperation().isBlocked(user):
                blockPng = self.unblockPng
            else:
                blockPng = self.blockPng

            if isHigh == False:
                b1 = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor, image=blockPng, justify="right", command= lambda :blockUnblock(user))
                b1.photo = blockPng
                b1.grid(row=row, column=1, sticky='e')

                b2 = Button(content_frame, bd=0, bg=self.bluePrimColor, activebackground=self.bluePrimColor,
                            image=self.removePng, justify="right", command=lambda :remove(user))
                b2.photo = self.removePng
                b2.grid(row=row, column=2, sticky='e', padx=30)

        rawData = SelectOperation().showAdmins()

        row=0
        for data in rawData:
            drawTile(row, data[1])
            row+=1

    def refresh(self):
        self.admins_frame.destroy()
        self.draw()