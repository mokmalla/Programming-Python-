for i in range(1,100,1):
  number =  str(i)
  count = 0
  
  for j in range(0,len(number),1):
    num= number[j]
    if(num == '3' or num == '6'or num =='9'):
     count+=1

  if count == 0:
    print(i)
  else:
    print("짝"*count)