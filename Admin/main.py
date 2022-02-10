from SetupPage import *
from tkinter import *
from step2 import *
from step3 import *
from step4 import *

root = Tk()
root.title("Attendence Manager")
# 1366 x 768
root.geometry("1080x650")
root.resizable(False, False)

# Step2(root=root, onthis=False).draw()
SetupPage(root).draw()
# Step4(root).draw()

root.mainloop()
