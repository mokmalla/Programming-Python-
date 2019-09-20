l = [1, 2, 3]
try:
    print(l[1])
    print(l[2])
    print(l[4])
    #print(l[3]) #IndexRttot: list index out of range
except IndexError as e:
    print("인덱스 에러")
    print(e)
else:
    print("성공적으로 모든 코드를 실행")