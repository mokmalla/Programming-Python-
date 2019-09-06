print("성적을 입력해주십시오")

korean = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
java = int(input("자바 점수 : "))
python = int(input("파이썬 점수 : "))
jsp = int(input("JSP 점수 : "))

avg = (korean + eng + math + java+ python + jsp) / 6
money = 0
if(avg >= 90):
    money = 100000
elif(avg >=80):
    money = 80000
elif(avg >= 70):
    money = 70000
elif(avg >= 60):
    money = 60000
else:
    money = 50000

print("총점",(korean + eng + math + java+ python + jsp),", 평균이 ",round(avg,2),"이므로, 용돈은 ",money,"원 입니다.")