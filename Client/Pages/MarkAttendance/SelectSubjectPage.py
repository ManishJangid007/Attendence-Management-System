from tkinter import *
import tkinter as tk

class SelectSubjectPage():
    def __init__(self, parent):
        self.parent = parent

    def draw(self):
        self.frame = Frame(self.parent, bg="white")