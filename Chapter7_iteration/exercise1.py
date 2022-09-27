import math

def mysqrt(a,x):
    return (x + a/x) / 2


def printit(a,x=2):
        for i in range(a):
            print("'a' value: "+str(i)+" mysqrt(a) "+str(mysqrt(i,x))+" math.sqrt "+str(math.sqrt(i))+" diff"+str(mysqrt(i,x)-math.sqrt(i)))
            x=mysqrt(i,x)
printit(10)
