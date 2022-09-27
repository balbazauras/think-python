import random



def choose_from_hist():
    d=histogram(t)
    val=round(random.uniform(0,2))
    for key, value in d.items():
        if value==val:
            return key
t=['a','a','b']
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
print(choose_from_hist())
