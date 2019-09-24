#class MyError(Exception):
#    pass

class OddError(Exception):
    def __init__(self, message):
        self.message=message

    def __str__(self):
        return self.message

n = 10
try:
    if n % 2 != 0:
        raise OddError

    else:
        print(n,", n/2=",n/2)
except OddError as e:
    print("에러 발생", e)