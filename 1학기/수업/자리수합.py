while True:
  number = input()
  StringNumber = str(number)
  sum = 0
  for i in range(0,len(StringNumber),1):
    sum+=int(StringNumber[i])
  print("각 자리 수의 합 :",sum)