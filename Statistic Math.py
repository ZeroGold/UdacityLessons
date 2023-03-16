### Linear Relationship Calculator
## Edit the numbers as you see fit.
## It compares two sets of related data
## For example Square Footage to House Cost

print("Due to some decimal errors. Smaller numbers may produce inaccurate results.")
           ##Solve decimal problem

## FUTURE NOTES: PLOT POINTS?
def Linear():
    houseCost = []
    squareFootage = []
    fixed = []
    isFixed = bool()
    findConst = []
    def houseAVG():
        return sum(houseCost)/len(houseCost)
    def sqftAVG():
        return sum(squareFootage)/len(squareFootage)


    def homeCost():
        calculateAVG = True
        print("Please Enter Home Costs")
        while calculateAVG:
            this = input()
            try:
                houseCost.append(int(this))
            except:
                calculateAVG = False


    def sqft():
        calculateSQFT = True
        print("Please Enter Square Footage")
        while calculateSQFT:
            this = input()
            try:
                squareFootage.append(int(this))
            except:
                calculateSQFT = False

                
    def findConstant():
        for i in range(len(houseCost)):
            constant = houseCost[i] - (squareFootage[i]*round(fixed[i],-1))
            findConst.append(constant)
        print("Co-efficient is : {}".format(sum(findConst)/len(findConst)))



    def finalC():
        if len(houseCost) == len(squareFootage):
            x = houseAVG()
            y = sqftAVG()
            z = x / y
            print("Average square footage: {} Average cost: {} Average cost per square foot: {}".format(y,x,z))
        else:
            print("There are more values in one list than the other.")





    homeCost()
    sqft()
    finalC()
    while len(houseCost) > len(squareFootage):
            squareFootage.clear()
            sqft()
            finalC()
    while len(squareFootage) > len(houseCost):
            houseCost.clear()
            homeCost()
            finalC()

        
    for i in range(len(houseCost)):
        x = houseCost[i]/squareFootage[i]
        fixed.append(x)
        print("Cost per square foot {}: {}".format(i+1,x))
    findConstant()
    print(findConst)

    isFixed = ((sum(fixed)/len(fixed)) == fixed[0])
    if isFixed == False:
        print("The Square Footage is not a fixed rate.")
    isConstant = ((sum(findConst)/len(findConst))== findConst[0])
    if isConstant == False:
        print("Constant is not a fixed rate.")

    if isConstant & isFixed == False:
        print("Non-linear relationship.")
    
grow = bool()

##### Next Part
def Trend():
    midPoints = []
    growth = 0
    linear = bool()
    print("How many groups of data?")
    this = input()
    def Bar():
        print("To find the halfway point between two non-linear values. Input those two values")
        findCO = []
        higher = 0
        lower = 0
        co1 = 0
        co2 = 0
        co3 = 0
        co4 = 0
        while len(findCO) < 2:
            this = input()
            try:
                findCO.append(int(this))
            except:
                print("Caught an error.")
        for items in findCO:
            higher = max(findCO)
            lower = min(findCO)
        for i in range(higher):
            co1 = higher - i
            co2 = lower + i
            if co2 == co1:
                co3 = co1
                co4 = i
                midPoints.append(co3)
        print("Half way number = {}  with a co-efficient of {}".format(co3,co4))
    for i in range(int(this)):
        Bar()
    if len(midPoints) > 2:
        for i in range(len(midPoints)):
            if midPoints[i] > midPoints[i-1]:
                growth = midPoints[i]
    else:
        if midPoints[0] < midPoints[1]:
            growth = midPoints[1]
    if growth == max(midPoints):
        print("Linear growth between data groups.")
    else:
        print("Total non-linear relationship.")

    
        


def frequency():
    solve = True
    data = []
    print("Input your points")
    while solve:
        this = input()
        try:
            data.append(int(this))
        except:
            break
    print("There are {} points.".format(len(data)))
    print("How many ranges to set?")
    this = input()
    
    def ranges(x):
        print("Range {}".format(x+1))
        count = 0
        print("Set your lower range.")
        lower = input()
        print("Set your upper range.")
        upper = input()
        for items in data:
            if items >=int(lower) and items <=int(upper):
                count+=1
        print("There are {} numbers between {} and {}".format(count,lower,upper))
        
    for i in range(int(this)):
                   ranges(i)


        
    

