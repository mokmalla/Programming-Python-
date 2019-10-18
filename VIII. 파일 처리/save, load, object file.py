#230

import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return("이름 : "+self.name + "\n나이 : "+str(self.age))

per1 = Person("정유경",18)
print(per1)

f = open("Object.bin", "wb")
pickle.dump(per1, f) #per1 객체를 f 파일에 저장
f.close()

#Load
#247

f = open("object.bin", "rb")
person = pickle.load(f)
f.close()

print(person)

# object list
p1 = Person("정유경", 18)
p2 = Person("정재현", 23)
p3 = Person("강하늘", 31)
people1 = [p1,p2,p3]

f= open("people.bin", "wb")
pickle.dump(people1, f)
f.close()

f = open("people.bin", "rb")
people2 = pickle.load(f)
f.close()
for item in people2:
    print(item)