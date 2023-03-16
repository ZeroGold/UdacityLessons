from random import randint
x = [0.5,1,2,0]
y = [1,2,4,0]
def hypothesis(x, theta0, theta1):
    return (theta0 + (theta1*x))




theta0 = randint(0, max(y))
theta1 = randint(0,max(y))



def ans(l1,l2,theta0, theta1, out = []):
    if len(l1) > 1:
        a = hypothesis(l1[0], theta0, theta1)
        if a != l2[0]:
            if a > l2[0]:
                theta0-=0.1
            if a > l2[0]:
                theta0+=0.1
            return ans(l1,l2,theta0,theta1)
        else:
            return ans(l1[1:],l2[1:],theta0,theta1)
        
       
        
     

print(ans(x, y, theta0, theta1))
