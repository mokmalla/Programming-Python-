import tkinter.ttk
from tkinter import *

class pagePro:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x500')
        self.root.title("페이지 계산")

        self.first_page = 0
        self.last_page = 0
        self.first_day =["", "", "", "", "", "", ""]
        self.last_day =["", "", "", "", "", "", ""]
        self.subjects =["", "", "", "", "", "", ""]
        fi = open("page.txt", "r", encoding="utf8")
        while True:
            data = fi.readline()
            if not data:
                break
            for i in range(0,5):
                for j in range(0, 7):
                    self.l[i][j] = data.split()
        fi.close()



    def play(self):
        self.root.mainloop()