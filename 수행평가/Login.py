from tkinter import *
from RegisterForm import registerform
from memberDB import memberDb
from member import member
from Lobby import lobby
import tkinter.messagebox


class login:

    def onClick(self):
        self.root.destroy()
        rg = registerform()
        rg.play()

    def toLobby(self):
        print(self.op1.get())
        self.root.destroy()
        lobby1 = lobby()
        mb = member()
        mb.setId(self.op1.get())
        lobby1.play()

    def loginPro(self):
        id = self.op1.get()
        pwd = self.op2.get()
        db = memberDb()

        if id == "":
            tkinter.messagebox.showwarning("아이디 오류", "ID를 입력해주십시오.")
        elif pwd == "":
            tkinter.messagebox.showinfo("패스워드 오류", "password를 입력해주십시오.")

        if db.check_Id(id, pwd) == 1:
            tkinter.messagebox.showinfo("로그인 완료","로그인 되었습니다!")
            self.toLobby()


        elif db.check_Id(id,pwd) == 3:
            tkinter.messagebox.showinfo("패스워드 오류", "password가 틀렸습니다.")
        else:
            tkinter.messagebox.showinfo("아이디 오류", "ID가 틀렸습니다.")

    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x250')
        self.root.title("Login")

        self.op1 = StringVar()
        self.op2 = StringVar()

        label_0 = Label(self.root, text="로그인", width=20, font=("bold", 19))
        label_0.place(x=65, y=23)

        label_1 = Label(self.root, text="ID", width=20, font=("bold", 10))
        label_1.place(x=25, y=90)

        entry_1 = Entry(self.root, textvariable=self.op1)
        entry_1.place(x=155, y=90)

        label_2 = Label(self.root, text="Password", width=20, font=("bold", 10))
        label_2.place(x=20, y=130)

        entry_2 = Entry(self.root, textvariable=self.op2)
        entry_2.place(x=155, y=130)

        button1 = Button(self.root, text='로그인', width=12, bg='#114B8A', fg='white', command=self.loginPro).place(x=100, y=180)
        button2 = Button(self.root, text='회원가입', width=12, bg='#114B8A', fg='white', command=self.onClick).place(x=220, y=180)

    def play(self):
        self.root.mainloop()



l= login()
l.play()
