from setupPages.SetupPage import SetupPage
from tkinter import *
from LoginPage import LoginPage
from ServerSide.Connection import *
from SplashScreen import SplashScreen

root = Tk()
root.title("Attendence Manager")
# 1366 x 768
root.geometry("1080x650")
root.resizable(False, False)
root.iconbitmap("Assets/icon.ico")

Sp = SplashScreen(root)
Sp.draw()

def start():
    if Connection().check_database():
        LoginPage(root).draw()
    else:
        SetupPage(root).draw()
    Sp.destroy()

root.after(2000, start)

root.mainloop()
