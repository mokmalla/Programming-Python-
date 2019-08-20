#시간 때우기
import time
time.sleep(0.1) #1초 자자

#화면 지우기
import os
os.system('cls')

n = 0

while(True):
  os.system('cls')
  print(" "*n+"O")
  n+=1 
  time.sleep(0.1) #0.1초 자자
