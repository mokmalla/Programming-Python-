from tkinter import *
from memberDB import memberDb
class registerform:

    def __init__(self):
        entry_1 = ""
        entry_2 = ""
        entry_3 = ""
        self.root = Tk()
        self.root.geometry('400x360')
        self.root.title("회원가입")

        self.op1 = StringVar()
        self.op2 = StringVar()
        self.op3 = StringVar()


        label_0 = Label(self.root, text="회원가입", width=20, font=("bold", 20))
        label_0.place(x=45, y=33)

        label_1 = Label(self.root, text="ID", width=20, font=("bold", 10))
        label_1.place(x=35, y=110)

        self.entry_1 = Entry(self.root, textvariable=self.op1)
        self.entry_1.place(x=170, y=110)

        label_2 = Label(self.root, text="Password", width=20, font=("bold", 10))
        label_2.place(x=30, y=160)

        self.entry_2 = Entry(self.root, textvariable=self.op2)
        self.entry_2.place(x=170, y=160)

        label_3 = Label(self.root, text="name", width=20, font=("bold", 10))
        label_3.place(x=35, y=210)

        self.entry_3 = Entry(self.root, textvariable=self.op3)
        self.entry_3.place(x=170, y=210)

        button1 = Button(self.root, text='가입', width=10, bg='#114B8A', fg='white',command=self.set_profile).place(x=120, y=270)
        button2 = Button(self.root, text='뒤로가기', width=10, bg='#114B8A', fg='white', command=self.load_module_func).place(x=220, y=270)

    def set_profile(self):
        id = self.op1.get()
        pwd = self.op2.get()
        name = self.op3.get()
        db = memberDb()
        db.insert(id,pwd,name)


    def load_module_func(self):
        self.root.destroy()
        mod = __import__('%s' % ("Login"), fromlist=["Login"])
        cls = getattr(mod, "login").play()

    def play(self):
        self.root.mainloop()
