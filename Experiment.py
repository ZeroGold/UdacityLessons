from random import randint
e = 2.71828
data = {}
final = []
def sigmoid(x):
    var = 1 /(1 + e**-x)
    return var


for i in range(100):
    x = randint(1,50)
    data[x] = sigmoid(x)



for key in data:
    if data[key] == 1:
        final.append(key)
        print("Value : {}, Result: {}".format(key, data[key]))


print(min(final))

print(data)
