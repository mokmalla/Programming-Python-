import tkinter.ttk
from tkinter import *
from pageCalculatorPro import pagePro

class page:
    def __init__(self, name, id):
        korean = 0
        math = 0
        english = 0
        science = 0
        jsp = 0
        ds = 0
        python = 0
        self.member_name = name
        self.member_id = id
        self.root = Tk()
        self.root.geometry('400x500')
        self.root.title("페이지 계산")

        self.entry_first= ["","","","","","",""]
        self.entry_last = ["","","","","","",""]

        label1= Label(self.root, text = '페이지 입력', width =20,font=("bold", 19)).place(x=60, y=15)

        #---------------------오늘 날짜 입력 ------------------------------------------------
        label2 = Label(self.root, text = '오늘 날짜 : ').place(x=50, y=70)

        self.combo1_value = StringVar()
        self.combo2_value = StringVar()
        self.combo3_value = StringVar()

        #년
        self.combobox1 = tkinter.ttk.Combobox(self.root, width=5,  textvariable=self.combo1_value)
        self.combobox1['values'] = ('2019', '2020')
        self.combobox1.place(x=135,y=70)
        self.combobox1.current(0)

        label3 = Label(self.root, text = '년').place(x=195, y=70)

        #월
        months = [ str(i) for i in range(1,12+1)]
        self.combobox2 = tkinter.ttk.Combobox(self.root, width=2, values=months, textvariable=self.combo2_value)
        self.combobox2.place(x=223, y=70)
        self.combobox2.set("1")

        label4 = Label(self.root, text='월').place(x=260, y=70)

        #일
        days = [str(i) for i in range(1, 31+1)]
        self.combobox3 = tkinter.ttk.Combobox(self.root, width=2, values=days, textvariable=self.combo3_value)
        self.combobox3.place(x=283, y=70)
        self.combobox3.set("1")

        label4 = Label(self.root, text='일').place(x=320, y=70)
        #-

        self.first_year = str(self.combo1_value.get())
        self.first_month = str(self.combo2_value.get())
        self.first_day = str(self.combo3_value.get())


        #------------------------------목표 날짜 입력 ---------------------------------------------------

        label5 = Label(self.root, text='목표 날짜 : ').place(x=50, y=100)

        self.combo4_value = StringVar()
        self.combo5_value = StringVar()
        self.combo6_value = StringVar()

        #년
        years = ["2019", "2020"]
        self.combobox4 = tkinter.ttk.Combobox(self.root, width=5, values=years, textvariable=self.combo4_value)
        self.combobox4.place(x=135, y=100)
        self.combobox4.set("2019")

        label6 = Label(self.root, text='년').place(x=195, y=100)

        #월
        months = [str(i) for i in range(1, 12 + 1)]
        self.combobox5 = tkinter.ttk.Combobox(self.root, width=2, values=months, textvariable=self.combo5_value)
        self.combobox5.place(x=223, y=100)
        self.combobox5.set("1")

        label7 = Label(self.root, text='월').place(x=260, y=100)

        #일
        days = [str(i) for i in range(1, 31 + 1)]
        self.combobox6 = tkinter.ttk.Combobox(self.root, width=2, values=days, textvariable=self.combo6_value)
        self.combobox6.place(x=283, y=100)
        self.combobox6.set("1")

        label8 = Label(self.root, text='일').place(x=320, y=100)
        #-

        self.last_year = self.combobox4.get()
        self.last_month = self.combobox5.get()
        self.last_day = self.combobox6.get()


        #----------------과목 & 페이지 입력 ----------------------------------------
        self.subjects = ["국어", "수학", "영어", "과학", "JSP", "DS", "Python"]
        yyy=[145,185,225, 265, 305, 345, 385]
        self.op = ["","","","","","",""]
        self.first_page = ["","","","","","",""]
        self.last_page = ["","","","","","",""]

        for i in range(0,7):
            label = Label(self.root, text = self.subjects[i]).place(x=70,y=yyy[i])
            label = Label(self.root, text = ":"). place(x=120, y=yyy[i])

        for i in range (0, 7):
            self.entry_first[i] = StringVar()
            self.entry_last[i] = StringVar()
            self.first_page[i] = Entry(self.root, textvariable=self.entry_first[i], width=7).place(x=150,y=yyy[i])
            label = Label(self.root, text="쪽   ~").place(x=205, y=yyy[i])
            self.last_page[i] = Entry(self.root, textvariable=self.entry_last[i], width=7).place(x=250, y=yyy[i])
            label = Label(self.root, text="쪽").place(x=305, y=yyy[i])

        button1 = Button(self.root, text='다음', width=7 ,bg='#114B8A', fg='white', font=("bold", 12), command =self.onClick1).place(x=300, y=450)
        button2 = Button(self.root, text='←',bg='#114B8A', fg='white',font=("bold", 15), command=self.onClick2).place(x=10, y=10)


    #입력한 년,월,일을 하나의 str로 만들어주는 함수
    def sumDays(self,year, month, day):
        sum = ""
        if len(month) == 1:
            if len(day) ==1:
                sum = year+"0"+month+"0"+day
            else:
                sum = year+"0"+month+day
        else:
            if len(day) == 1:
                sum = year + month + "0" + day
            else:
                sum = year + month + day
        return sum

    #다음화면으로 넘어가고, 파일에 입력을 해주는 함수
    def onClick1(self):
        self.sum_first_day = self.sumDays(self.combo1_value.get(), self.combo2_value.get(), self.combo3_value.get())
        self.sum_last_day = self.sumDays(self.combo4_value.get(), self.combo5_value.get(), self.combo6_value.get())
        print(self.sum_last_day)
        f = open("page.txt", "w", encoding="utf8")
        for i in range(len(self.entry_first)):
            f.write(self.member_id+"\t"+self.sum_first_day+"\t"+self.sum_last_day+"\t"+str(self.entry_first[i].get())+"\t"+str(self.entry_last[i].get())+"\t"+str(self.subjects[i])+"\n")
        f.close()
        #pageNext = pagePro()
        #self.root.destroy()
        #pageNext.play()

    #현 화면을 없애주는 함수
    def onClick2(self):
        self.root.destroy()

    #pageCalculator 실행 함수
    def play(self):
        self.root.mainloop()
