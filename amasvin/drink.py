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