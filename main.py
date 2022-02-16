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

conn = Connection()

if conn.check():
    if conn.check_database():
        LoginPage(root).draw()
    else:
        ErrorPage(root=root, message="Database Not Found")
else:
    ErrorPage(root, parameterOption=True).draw()

root.mainloop()
