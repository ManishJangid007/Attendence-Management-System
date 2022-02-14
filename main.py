from LoginPage import *
from ErrorPage import *
from Connection import *
from tkinter import *

root = Tk()
root.title("Attendence Manager")
# 1366 x 768
root.geometry("1080x650")
root.resizable(False, False)
root.iconbitmap("Assets/icon.ico")

LoginPage(root).draw()

if Connection().check() == False:
    ErrorPage(root, parameterOption=True).draw()

root.mainloop()
