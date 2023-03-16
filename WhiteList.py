### WHITELIST



whitelist = ["bob@home", "alice@work", "dave@boat"]



def search(x,y):
    if x == y:
        return whitelist.index(x)
    else:
        return -1




x = []

## SETTING THINGS EQUAL TO THE OLD THING MAKES A POINTER TO THAT THING
for i in whitelist:
    x.append(i)
x.append("larry@job")
x.append("carrie@gym")
x.append("barry@junkyard")

#for i in x:
    #for j in whitelist:
        #if search(i,j) != -1:
            #print(whitelist[search(i,j)])


#sequential search
#check each array, if it doesn't match return -1
# if it does, you return the index of that thing.


def sample(key, x):
    for i in range(len(x)):
        if x[i] == key:
                   return i
        return -1
y = len(x)
for i in x:
    if sample(i, whitelist) != -1:
        print(whitelist[sample(i,whitelist)])

### ABOVE IMPLEMENTATION WILL COMPARE REFERENCES, AND YOU WON'T GET YOUR FULL ANSWER


### Implementation 2
### using compare to might give us matches
def compareTo(x,y):
    if x == y:
        return 0
    else:
        return -1
def sample2(key, x):
    for i in range(len(x)):
        if compareTo(x[i],key) == 0:
            return i
        return -1


for i in range(len(x)):
    if sample2(x[i],whitelist) != -1:
        print(whitelist[sample2(x[i],whitelist)])
