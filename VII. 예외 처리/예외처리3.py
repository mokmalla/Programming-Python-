l = [1, 2, 3]
try:
    print(l[3]) #IndexRttot: list index out of range
except IndexError as e:
    print("인덱스 에러")
    print(e)