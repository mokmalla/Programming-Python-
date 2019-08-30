#from foods.drinks import milk #import 뒤에 파일.모듈이름
#milk.drink()

#from foods.drinks.milk import drink
#drink()

#import foods.drinks.milk
#foods.drinks.milk.drink()

#import의 끝이 폴더이면 안됨. 반드시 모듈이거나 모듈 안에있는 함수를 써야함
#from은 됨

from foods.drinks.milk import drink
drink()

#import foods.drinks 
#foods.drinks.milk.drink()

# foods.drinks.mil.drink()      #error

#from : 폴더 or 모듈
#import : 모듈 or 함수
#from은 항상 import와 같이 써줘야함

from foods.drinks import milk as m
m.drink()