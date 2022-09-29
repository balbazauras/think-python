import random

t=['a','a','b']

def choose_from_hist():
    val=round(random.uniform(0,len(t)))
    print(val)
    return t[val]

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
print(choose_from_hist())
