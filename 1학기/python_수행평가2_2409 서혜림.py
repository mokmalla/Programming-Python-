#2409 서혜림
#피시방 자리 예약 + 시간 충전 프로그램

#피시방 선택하기
#로그인 하기
#좌석 선택 후 예약하기
#충전 할 시간 선택하기
#금액 계산하기 

from random import *

class User:
  #변수들
  _PCrooms= ["퍼플PC방", "샹떼PC방", "애플PC방", "그린PC방", "네오넷PC방"]
  _moneys = [1000, 2000, 3000, 5000, 9000]
  _times = [1, 2, 3, 5, 11]
  leaveHour = randint(0, 6)
  leaveMinute = randint(0, 60)
  money_charging = 0
  colum= None
  row= None

  #좌석 랜덤으로 채우기
  _seats = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
  for i in range(5):
      for j in range(5):
        _seats[i][j] = randint(0,1)



  def __Time__(self):
    #시간 출력 함수
    #1의 자리 밖에 없을 땐 앞에 0붙여주기
    if(self.leaveMinute < 10):
      if(self.leaveHour < 10):
        print("잔여 시간 : 0"+str(self.leaveHour)+":0"+str(self.leaveMinute))
      else:
        print("잔여 시간 : "+str(self.leaveHour)+":0"+str(self.leaveMinute))
      
    else:
      if(self.leaveHour < 10):
        print("잔여 시간 : 0"+str(self.leaveHour)+":"+str(self.leaveMinute))
      
      else:
        print("잔여 시간 : "+str(self.leaveHour)+":"+str(self.leaveMinute))




  def __showPCroom__(self):
    #피시방 선택하는 함수
    print("PC방을 선택해주십시오.")
    self.PCroom = input("0.퍼플PC방 / 1.샹떼PC방 / 2.애플PC방 / 3.그린PC방 / 4.네오넷PC방")

    while(1): #번호 입력 안했을 시에 무한 반복해서 물어봄
      if self.PCroom == '':
        print("PC방을 선택해주셔야 합니다.")
        self.PCroom = input("0.퍼플PC방 / 1.샹떼PC방 / 2.애플PC방 / 3.그린PC방 / 4.네오넷PC방")
        
      else:
        self.PCroom = int(self.PCroom) #선택한 피시방 변수에 집어넣기
        break




  def __showLogin__(self):
    #로그인하는 함수
    print(self._PCrooms[self.PCroom]+"의 회원 아이디와 패스워드를 입력해주십시오.")

    #ID
    self.user_ID = input("ID : ")
    while(1): #ID 입력 안했을 시에 무한반복
      if self.user_ID == '':
        self.user_ID = input("아이디를 입력해주십시오!!!!\nID : ")
      else:
        break


    #pwd
    self.user_pwd = input("pwd : ")
    while(1): #pwd 입력 안했을 시에 무한반복
      if self.user_pwd == '':
        self.user_pwd = input("패스워드를 입력해주십시오!!!!!\npwd : ")
      else:
        break

    print("반갑습니다, "+self.user_ID+"님!\n") #로그인 성공적
    



  def __showTime__(self):
    #잔여시간 보여주는 함수
    print(self.user_ID+"님의 ", end='')
    self.__Time__()

    #만약 회원님의 남은 시간이 30분이하라면 선불 결제화면을 먼저 보여주고
    #아니라면 자리 예약화면을 먼저 보여줌
    if(self.leaveHour == 0 and self.leaveMinute <= 30):
      print("잔여 정액 시간이 30분 이하입니다.")
      self.__set_Time__()
      
    else:
      self.__set_Seat__()
      


  def __set_Seat__(self):
    #자리 예약 함수
    print("좌석을 선택하여 주십시오. ( □ : 예약 가능한 자리 / ■ : 이미 예약된 자리 )")
    print("   0 1 2 3 4 ")

    for i in range(5):
      print (i," ", end='')
      for j in range(5):
        if(self._seats[i][j] == 0):
          print ("□ ", end='')
        else:
          print ("■ ", end='')
      print("")

    self.colum = input("행 >>  ")
    self.row = input("열 >>   ")

    #예약된 좌석을 선택했을 시에 다시한번 선택할 수 있도록 함
    if(self._seats[int(self.colum)][int(self.row)] == 1):
      print("이미 예약된 좌석입니다.")
      self.__set_Seat__()
      
      
    else:
      print("예약되었습니다! (※ 예약이 완료된 시점부터 잔여 시간이 차감됩니다.)")
      yesoryes1 = input("시간을 더 충전하시겠습니까?(1.예 / 2.아니오)")
    
      if(yesoryes1 == '1'): #예를 선택하면 시간 충전 화면으로 감
        self.__set_Time__()
        
      else:
        return 0


  def __set_Time__(self):
    #시간 충전하는 함수

    while(1):
      print("충전할 시간을 선택해주십시오")
      print("0. 1시간 : 1000원 \n1. 2시간 : 2000원 \n2. 3시간 : 3000원 \n3. 5시간 : 5000원 \n4. 11시간 : 9000원")
      self.choose_time = input()

      #돈과 시간을 충전해줌
      self.money_charging = self.money_charging + self._moneys[int(self.choose_time)]
      self.leaveHour = self.leaveHour + self._times[int(self.choose_time)]

      

      print(str(self._times[int(self.choose_time)])+"시간 충전되었습니다")
      self.__Time__()
      print("결제 금액 : "+str(self.money_charging)+"원")

      self.yesoryes2 = input("더 충전하시겠습니까? (1. 예 / 2.아니오) ")

      if(self.yesoryes2 == '2'):
        if(self.colum is None or self.row is None): #아직 자리 예약을 하지 않은 상태라면 자리예약 화면으로 이동
          self.__set_Seat__()
          break
        else:
          break
  

  def __show_Total__(self):
    #총 결제 내역을 보여주는 함수
    print("\n--------------"+self.user_ID+"님의 총 결제 내역"+"--------------")
    print("예약하신 좌석의 행,열 : ("+str(self.colum)+", "+str(self.row)+")")
    self.__Time__()
    print("총 결제 금액 :"+str(self.money_charging)+"원")

    

연습용 = User()
연습용.__showPCroom__()
연습용.__showLogin__()
연습용.__showTime__()
연습용.__show_Total__()