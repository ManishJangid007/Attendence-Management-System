from SetupPage import *
from tkinter import *
from Admin.LoginPage import LoginPage
from Admin.Connection import *
from Admin.HomePage import *

root = Tk()
root.title("Attendence Manager")
# 1366 x 768
root.geometry("1080x650")
root.resizable(False, False)
root.iconbitmap("Assets/icon.ico")

HomePage(root, "username").draw()

# if Connection().check_database():
#     LoginPage(root).draw()
# else:
#     SetupPage(root).draw()

root.mainloop()
