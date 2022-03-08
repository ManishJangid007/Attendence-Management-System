from setupPages import SetupPage
from tkinter import *
from LoginPage import LoginPage
from ServerSide.Connection import *
from discriptivePages.editStudentPage import EditStudentPage
from HomePage import *

root = Tk()
root.title("Attendence Manager")
# 1366 x 768
root.geometry("1080x650")
root.resizable(False, False)
root.iconbitmap("Assets/icon.ico")

# EditStudentPage(root, "aryaID").draw()
HomePage(root, "username").draw()

# if Connection().check_database():
#     LoginPage(root).draw()
# else:
#     SetupPage(root).draw()

root.mainloop()
