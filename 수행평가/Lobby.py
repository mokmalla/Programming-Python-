from tkinter import *
from memberDB import memberDb
from tkinter import PhotoImage
from pageCalculator import page

class lobby:

    def onClick1(self):
        pass

    #페이지 계산 화면으로 넘어가는 함수
    def onClick2(self):
        pagepage = page(self.member_name, self.member_id)
        pagepage.play()


    def __init__(self, name, id):
        self.rId = ""
        self.member_name = name
        self.member_id = id
        self.root = Tk()
        self.root.geometry('500x350')
        self.root.title("로비")

        mbdb = memberDb()

        background_image = PhotoImage(file="lobby_background.gif")
        background_label = Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        background_label.image = background_image

        label1 = Label(self.root, text=self.member_name + '님 환영합니다!').place(x=205, y=20)

        button1 = Button(self.root, text = '달성도 보기', width=20, height=2, bg='#B50FA9', fg='white', command=self.onClick1).place(x=183,y=270)
        button2 = Button(self.root, text='쪽수 계산기', width=20, height=2, bg='#750F87', fg='white', command=self.onClick2).place(x=183, y=220)

    #로비화면을 실행해주는 함수
    def play(self):
        self.root.mainloop()

#lolo = lobby()
#lolo.play()