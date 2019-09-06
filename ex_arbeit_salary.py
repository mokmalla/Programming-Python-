#알바비 계산기
#일주일에 몇시간 일하는지
#몇주 일하는지
#시급 얼마인지
#주 15시간 이상이면, 주휴수당 지급
#주휴수당 : 주 5일 근무로 생각하고 1일치 더줌
week_time = int(input("일주일에 몇 시간 일해?"))
how_long = int(input("몇 주 일해?"))
how_much = int(input("시급 얼마야?"))
#2 주휴수당 계산
if week_time >= 15:
    week_time += (week_time/5)
#3
salary = week_time * how_long * how_much
print("알바비는", salary)