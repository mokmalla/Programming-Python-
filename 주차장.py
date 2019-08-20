import sys
while True:
  minutes = int(input())
  fee = 0
  if minutes <=30:
    fee = 2000
  else:
    minutes = minutes - 30
    fee += 2000
    fee+= (minutes//10)*1000	

    if minutes%10 != 0:
      fee+=1000

  if fee> 25000:
    fee=25000
  
  if minutes/60 >= 24:
    print("나가세요")
    break

  print("주차요금은", int(fee), "원입니다.")