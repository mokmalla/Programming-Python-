import hello_func
import greeting_func

def main():
  print("insa_func 모듈입니다")
  print("__name__:",__name__) #__main__으로 출력
  hello_func.hello()
  greeting_func.greeting()  #greeting_func로 출력


main()