fi = open("history.ama", "r", encoding="utf8")
while True:
    data =fi.readline()
    if not data:
        break
    #print(data, end="")
    l = data.split() #화이트스페이스 : \t,\n 띄어쓰기 있는 걸 다 자름
    sum += int(l[1])
    #총금액 계산하고 출력
print("총 금액 : "+str(sum)+"원")
fi.close()

#한줄 안에서 이름 가격,