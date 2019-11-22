#아마스빈 주문 앱
#Drink <- Coffee
# <- Bubbletea
#Order
# 메뉴 보여주기
# 음료 주문하기
# 주문한 음료 보여주기
# 총 금액 계산하기

class Drink:
  _cups=["레귤러","점보"]
  _ices=["0%", "50%", "100%", "150%"]
  _sugars=["0%", "50%", "100%", "150%"]

  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.cup = 0   #기본값
    self.ice = 2
    self.sugar = 3
  
  def __str__(self):
    return "이름 : "+self.name+"\t가격 : "+str(self.price)\
      +"원\t컵:"+Drink._cups[self.cup]\
      +"\t얼음량: "+Drink._ices[self.ice]\
      +"\t당도:"+Drink._sugars[self.sugar]

  def set_cup(self):
    self.cup = input("컵을 선택하세요(0: 레귤러, 1: 점보)\t")
    if self.cup == "":  #사용자가 엔터만 치면 기본값 0을 넣자
      self.cup = 0
    else:
      self.cup = int(self.cup)

    #점보면 300원 추가
    if self.cup == 1:
      self.price += 300

  def set_ice(self):
    self.ice = input("얼음량을 선택하세요.(0: 0%, 1: 50%, 2: 100, 3: 150%)\t")
    if self.ice =="":
      self.ice = 2
    else:
      self.ice = int(self.ice)

  def set_sugar(self):
    self.sugar= input("당도를 선택하세요.(0: 0%, 1: 50%, 2: 100, 3: 150%)\t")
    if self.sugar=="":
      self.sugar = 2
    else:
      self.sugar = int(self.sugar)

  def order(self):
    self.set_cup()    #앞에 self. 꼭 붙여주기
    self.set_ice()
    self.set_sugar()


class Coffee(Drink):
  pass

class Bubbletea(Drink):
  _pearls=["타피오카", "코코", "젤리", "알로에"]

  def __init__(self, name, price):
    super().__init__(name, price)
    self.pearl = 0

  def set_pearl(self):
    self.pearl = input("펄을 선택하세요(0:타피오카, 1:코코, 2:젤리, 3:알로에)\t")
    if self.pearl == "":
      self.pearl = 0
    else:
      self.pearl = int(self.pearl)

  def __str__(self):
    return super().__str__() + "\t펄: " +Bubbletea._pearls[self.pearl]
  
  def order(self):
    super().order()
    self.set_pearl()

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
