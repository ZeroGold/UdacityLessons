import math

e = math.e

def sigmoid(x):
    val = 1 /(1 + e**-x)
    return val


def Answer(*args):
    for arg in args:
        x = arg[0]
        y = arg[1]
    score = (4*x) + (5*y) - 9
    if sigmoid(score) == 0.5:
        print(x,y)


vals = [(1,1),(2,4),(5,-5),(-4,5)]

for items in vals:
    Answer(items)


