fi = open("history.ama", "r", encoding="utf8")
while True:
    data =fi.readline()
    if not data:
        break
    print(data, end="")
fi.close()

#한줄 안에서 이름 가격,