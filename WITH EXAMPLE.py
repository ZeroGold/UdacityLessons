from random import randint

### the with operator calls the __enter__ and __exit__ blocks of a class

class Wither:
    def __init__(self):
        self.x = 0
    def __enter__(self):
        self.x = randint(1,100)

     # StackOverflow says self type value and traceback need to be passed in?   
    def __exit__(self,type,value,traceback):
        print(self.x + 10, type, value, traceback)



#### When writing code in the future, think about how to craft enter and exit blocks to accomodate this
x = Wither()
print(x.x)
with x:
    print(x.x)
