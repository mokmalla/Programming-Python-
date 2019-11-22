#2409서혜림
#하루에 몇 쪽을 풀어야 시험 전 까지 공부를 다 끝낼 수 있을 지 계산해주는 프로그램
#Login.py에서 실행

from tkinter import *
from RegisterForm import registerform
from memberDB import memberDb
from Lobby import lobby
import tkinter.messagebox


class login:

    #회원가입 화면으로 넘어가는 함수
    def onClick(self):
        self.root.destroy()
        rg = registerform()
        rg.play()

    #다음 화면으로 이동하는 함수
    def toLobby(self):
        name = self.db.selectName(self.op1.get())

        self.root.destroy()
        lobby1 = lobby(name, self.op1.get())
        lobby1.play()

    #로그인 검사 함수
    def loginPro(self):
        id = self.op1.get()
        pwd = self.op2.get()
        self.db = memberDb()

        if id == "":
            tkinter.messagebox.showwarning("아이디 오류", "ID를 입력해주십시오.")
        elif pwd == "":
            tkinter.messagebox.showinfo("패스워드 오류", "password를 입력해주십시오.")

        elif self.db.check_Id(id, pwd) == 1:
            tkinter.messagebox.showinfo("로그인 완료","로그인 되었습니다!")
            self.toLobby()


        elif self.db.check_Id(id,pwd) == 3:
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

    #login 실행 함수
    def play(self):
        self.root.mainloop()


lo = login()
lo.play()