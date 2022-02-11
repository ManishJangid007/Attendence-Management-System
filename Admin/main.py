from SetupPage import *
from tkinter import *

root = Tk()
root.title("Attendence Manager")
# 1366 x 768
root.geometry("1080x650")
root.resizable(False, False)

SetupPage(root).draw()

root.mainloop()
