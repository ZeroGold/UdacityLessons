import numpy as np
import math
e = math.e
# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    n = []
    m = []
    for items in L:
        m.append(e**items)
    for items in m:
        n.append(items / (sum(m)))
    return n
