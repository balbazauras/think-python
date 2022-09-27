import math
def compare(x,y):
    if(x>y):
        return 1
    if(x==y):
        return 0
    if(x<y):
        return -1
print(str(compare(10,10)))

def hypotenuse(a,b):
    asquared=a**2
    bsquared=b**2
    sumoflegs=asquared+bsquared
    return math.sqrt(sumoflegs)

print (str(hypotenuse(6,10)))

def is_between(x,y,z):
    if x<=y<=z:
        return True
    else: 
        return False
print(str(is_between(3,2,3)))