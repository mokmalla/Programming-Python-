from datetime import datetime

print("현재 날짜 시각 객체 얻기")
today = datetime.now()
print("today = datetime.now()", today)
print("년 월 일 : ",today.year, today.month, today.day)
print("시 분 초 : ", today.hour, today.minute, today.second)
print("요일 : ", today.weekday()) #0:월 1:화 2:수 ...
print("특정 날짜 시각 객체 만들기")
day = datetime(2019, 1, 1, 0,0,0)
print("day = datetime(2019, 1, 1, 0,0,0) : ", day) #2019년 1월 1일 0시 0분 0초
print("2019년부터 지나온 시간 구하기")
print("today - day : ", today-day)
#태어난지 며칠 지났는지?
day = datetime(2002, 4, 11, 11,36,0)
print("혜림이 태어난 지 ", today - day )

#올해 크리스마스 며칠 남았는지
day = datetime(2019,12,25,0,0,0)
print("크리스마스 까지 앞으로 ", today-day)

#내생일 며칠 남았는지?
print("내 생일까지 앞으로 ", today - datetime(2020, 4, 11,0,0,0))