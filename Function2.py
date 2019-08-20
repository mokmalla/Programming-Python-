input("현재의 input() 함수는 사용자 정의 합수입니다.")

def input(s):
    print(s)
input("현재의 input() 함수는 사용자 정의 합수입니다.")

import random


# n= random.randrage(1, 6+1)  #1<= x <^+1 랜덤수 x 리턴
def rolling_dice():
  n=random.randint(1, 6)  #1<= x <=6 랜덤수 x 리턴
  print("6면 주사위 굴린 결과 : ",n)
  
rolling_dice()
rolling_dice()
rolling_dice()

#star 함수 정의
def star():
  print("*****")
  star() #*****
  star() #*****
  star() #*****

def rolling_dice(pip):
  n = random.randint(1, pip)
  print(pip,"면 주사위 굴린 결과: ", n)

#rolling_dice() #자바와 달n리 오버라이딩이 안됨
rolling_dice(4)
rolling_dice(6)
rolling_dice(8)
rolling_dice(10)
rolling_dice(12)
rolling_dice(14)

def rolling_dice(pip, repeat):
  for r in range(1, repeat+1):
    n=random.randint(1,pip)
    print(pip, "면 주사위 굴린 결과: ",r," : ", n)

# rolling_dice(2) 새로 정의됐기 때문에 위에 있던 정의함수는 먹지X
rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(12, 0) # 실행X
rolling_dice(20, -3) #실행X

#가변인수
print("가변인수---------------------------")
print("♡")
print("♡", "♪")
print("♡", "♪", "♣")
print("♡", "♪", "♣", "♠")
print("♡", "♪", "♣", "♠", "★")

def p(*args): #args :매개변수가 몇개가 들어와도 OK
  string = ""
  for a in args:
    string+=a
  print(string)
p("♡")
p("♡","♪", "♣","♥")

#안녕()함수를 만들고,
def 안녕(*args):
  for a in args:
    print("안녕", a)

안녕("가연아","수빈아","정윤아","채린아")
#안녕, 가연아
#안녕, 수빈아
#안녕, 정윤아

# def p( *args, space, space_num): #가변수 *args는 앞에 있을 수 없음
def p(space, space_num, *args): 
  string = args[0]
  for i in range(1, len(args)):
    string += (space * space_num)+ args[i]
    print(string)

#p(",",3)    #에러
p(",",3,"♡")    #♡만 출력
p(",",3,"♡","♪")     #핱,,,,음
p(",",3,"♡","♪","♣")    #핱,,음,,클
p(",",3,"♡","♪","♣","♠")

def star(moonza, *args):
  for i in args:
    print(moonza*i)

star("음",3)
#음음음
star("핱",1,2,3)     
#핱
#핱핱
#핱핱핱 

#116 키워드 인자를 
def fn(a,b,c,d,e):
  print(a,b,c,d,e)

fn(1,2,3,4,5)
fn(10,20,30,40,50)
fn(5,6,7,8,9)
fn(a=1,b=2,c=3,d=4,e=5) # 1 2 3 4 5
fn(e=5,d=4,c=3,b=2,a=1) # 1 2 3 4 5
fn(1,2,c=3,e=5,d=4)     # 1 2 3 4 5 
# fn(d=4, e=5, 1, 2, 3) # 에러 처음부터 이름 붙여주면 안대

def fn(a,b,c,*d):
  print(a,b,c,d)

# fn(c=3,b=2,a=1,4,5)   #error
# fn(1,2,c=3,4,5)       #error 중간 끼어들기 안돼 이름 쓰기 시작한 순간부터 끝까지 써주어야함
# fn(4,5,a=1,b=2,c=3)   #error 중복지칭 안돼

def star(mark, repeat, space, space_repeat, line):
  for i in range(1, line):
    string=(mark * repeat)
    for j in range(2, repeat):
      string = string + (space * space_repeat) + (mark * repeat)
    print(string)

star("*",2,"+",3, 5)
print("--------------------------")
# star(mark="*",repeat=2,space="+",space_repeat=3,line=5)

def star2(mark, repeat, space, space_repeat, line):
  string = (mark*repeat)+(space*space_repeat)+(mark*repeat)
  for n in range(line):
    print(string)

star2("※", 3, "_", 2, 3)
print("-------------------------")
star2(mark="※", repeat= 3,space= "_",space_repeat= 2,line= 3)

#199p
def hello(msg="안녕하세요"):
  print(msg+"!")

hello("오랜만이에요")
hello("강은서")
hello()

def hello2(name="무명", msg="안녕하세요"):
  print(name+"님, "+msg+"!")

hello2("곽가연", "오랜만이에요")
hello2()
hello2("김민지") #김민지님, 안녕하세요!
hello2(msg="오랜만이에요") #무명님, 오랜만이에요!

def hello3(name, msg="안녕하세요"):
  print(name+"님, "+msg+"!")

hello3("김봄이", "오랜만이에요")
hello3("김소현")
# hello3()  #error name을 줘야한다

def fn2(a,b=[]):
  b.append(a)
  print(b)

fn2(3) #[3]
fn2(5) #[3,5]
fn2(10)  #[3,5,10] 
fn2(7,[1])  #[3, 5, 10, 1, 7]:X vvs [1, 7]:O

#p123
def gugudan(first=2):
  for i in range(1, 9+1):
    print("{} X {} = {}".format(first, i, first*i))

gugudan(3)  #3단 출력
gugudan()   #2단 출력

#p125
def sum(*numbers):
  sum_value=0
  for number in numbers:
    sum_value += number

  return sum_value

result = sum(1,3)
print("1 + 3 =",result)
print("1 + 3 + 5 + 7 =",sum(1, 3, 5, 7))

#p126
def min(*numbers):
  min_value = numbers[0]
  for number in numbers:
    if min_value > number:
        min_value = number
  return min_value

print("min(1, 3) = ",min(1, 3))
print("min(0, 3, -11) = ",min(0, 3, -11))

def max(*numbers):
  max_value = numbers[0]
  for number in numbers:
    if max_value < number:
      max_value = number
  return max_value

print("max(1, 2 ,3) = ", max(1, 2, 3) )
print("max(8, 56 ,12) = ", max(8, 56, 12) )

#127p 나누어 떨어지는 수 구하기
def multi_num(multi, start, end):
  result = []
  for n in range(start, end):
    if n % multi ==0:
      result.append(n)
  return result

print("multi_num(17, 1, 200) = ", multi_num(17, 1 ,200))
print("multi_num(3, 1, 100) = ", multi_num(3, 1 ,100))
#128p
def min_max(*args):
  min = args[0]
  max = args[0]
  for arg in args:
    if min > arg:
      min = arg 
    if max < arg:
      max= arg
  
  return min, max

print("min_max(52, -3, 23, 89 -21)")
min_value, max_value, = min_max(52,-3,23, 89,-21)
print("최솟값: ", min_value, "최댓값 : ", max_value)