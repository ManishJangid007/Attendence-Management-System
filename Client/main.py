from LoginPage import *
from ErrorPage import *
from ServerSide.Connection import *
from SplashScreen import SplashScreen
from tkinter import *

root = Tk()
root.title("Attendence Manager")
# 1366 x 768
root.geometry("1080x650")
root.resizable(False, False)
root.iconbitmap("Assets/icon.ico")

Sp = SplashScreen(root)
Sp.draw()

def start():
    conn = Connection()
    if conn.check():
        if conn.check_database():
            LoginPage(root).draw()
        else:
            LoginPage(root).draw()
            ErrorPage(root=root, message="Database Not Found")
    else:
        LoginPage(root).draw()
        ErrorPage(root, parameterOption=True).draw()

root.after(2000, start)

root.mainloop()
