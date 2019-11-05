from tkinter import *

class page:
    def __init__(self):
        korean = 0
        math = 0
        english = 0
        science = 0
        jsp = 0
        ds = 0
        python = 0

        self.root = Tk()
        self.root.geometry('400x500')
        self.root.title("페이지 계산")

        label1= Label(self.root, text = '페이지 입력', width =20,font=("bold", 19)).place(x=68, y=15)
        label2 = Label(self.root, text = '오늘 날짜').place(x=30, y= 100)

        years = ['2019', '2020']
        c = StringVar()
        droplist = OptionMenu(self.root, c, *years)
        droplist.config(width=15)
        c.set('select your country')
        droplist.place(x=240, y=280)



        label1 = Label(self.root, text = '국어' )

        button1 = Button(self.root, text='다음', width=7 ,bg='#114B8A', fg='white', font=("bold", 12)).place(x=300, y=450)
        button2 = Button(self.root, text='←',bg='#114B8A', fg='white',font=("bold", 15)).place(x=10, y=10)

    183
    def play(self):
        self.root.mainloop()

lala = page()
lala.play()