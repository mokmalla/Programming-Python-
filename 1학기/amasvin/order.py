from coffee import Coffee
from bubbletea import Bubbletea

class Order:
  _menus = [ Coffee("아메리카노", 1800), Bubbletea("딸기요거트", 3500) ]

  def __init__(self):
    self.order_menu = []
    self.order = None
  
  def show_menu(self):
    print("0: 아메리카노 1800원, 1: 딸기요거트 3500, ")
    
  def sum_price(self):
    sum = 0
    for drink in self.order_menu:
      sum+= drink.price
    
    return sum

  def order_drink(self):
    while True:
      #메뉴 보여주자
      self.show_menu()
      #주문받자
      #음료선택
      self.order = input("음료를 선택하세요: ")
      #   음료 객체 새엇ㅇ
      if self.order == "":  #메뉴 선택안하고 그냥 엔터치면 주문 끝
        break
      if int(self.order) == 0:
        drink = Coffee("아메리카노",  1800)
      elif int(self.order) == 1:
        drink = Bubbletea("딸기요거트", 3500)
      drink = Order._menus[int(self.order)]
      #   음료옵션 선정
      #음료옵션
      drink.order()
      #주문한 음료 리스트에 추가
      self.order_menu.append(drink)
       #반복
      #주문한 음료 출력
      for drink in self.order_menu:
        print(drink)
      #금액합계
    print("총금액 : "+str(self.sum_price())+"원")


o= Order()
o.order_drink()
아메리카노 = Drink("아메리카노", 1800)
아메리카노.order()
print(아메리카노)   #이름 : 아메리카노\t가격 : 1800

타로밀크티 = Bubbletea("타로밀크티", 3500)
타로밀크티.set_cup()
타로밀크티.set_ice()
타로밀크티.set_sugar()
타로밀크티.set_pearl()
print(타로밀크티)
