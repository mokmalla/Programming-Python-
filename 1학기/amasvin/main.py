#main.py
from order import Order
from file_manager import FileManager

#주문내역 불러오고, 보여주자
file_manager = FileManager("history.bin")
#answer = input("주문내역을 볼까요?(y or n)")
#if answer == "y":
history=[]
try:
    history = file_manager.load()
    sum=0

    for h in history:
        print(h)
        sum += h.price
    print("여태까지 내가 아바스빈에 솓아부은 돈 : "+str(sum)+"원")
except FileNotFoundError:
    print("주문내역 x")
o = Order()
o.order_drink()

#주문내역 저장하자
file_manager.save(history+o.order_menu)