from tkinter import *
from memberDB import memberDb
from tkinter import PhotoImage
from member import member

class lobby:
    def onClick1(self):

    def onClick2(self):


    def __init__(self):
        self.rId = ""
        self.root = Tk()
        self.root.geometry('500x350')
        self.root.title("로비")

        mb = member()
        id = mb.getId()
        mbdb = memberDb()
        member_name = mbdb.selectName(mb.getId())

        background_image = PhotoImage(file="lobby_background.gif")
        background_label = Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        background_label.image = background_image

        label1 = Label(self.root, text= str(member_name) + '님 어서오세요').place(x=183, y=10)

        button1 = Button(self.root, text = '달성도 보기', width=20, height=2, bg='#B50FA9', fg='white', command=onClick1).place(x=183,y=270)
        button2 = Button(self.root, text='쪽수 계산기', width=20, height=2, bg='#750F87', fg='white', command=onClick2).place(x=183, y=220)

    def play(self):
        self.root.mainloop()

#lolo = lobby()
#lolo.play()