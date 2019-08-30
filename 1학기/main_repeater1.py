#153p
#import 하는 방법 4가지
#import repeater
#from repeater imort repeat, once
#from repeater import *
from repeater import re #가져온 것의 이름바꾸기
s=input("반복할 문자를 입력하세요: ")
n = input("반복 횟수를 입력하세요: ")
#repeater.repeat(s, int(n))
#repeater.repeat(s)
#repeater.once(s)
re.repeat(s, int(n))
re.repeat(s)
re.once(s)