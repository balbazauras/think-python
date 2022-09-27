
import pprint

fin = open('Chapter12_tuples/words.txt')
d=dict()

def read():
    for line in fin:
        word=line.strip()
        d[word]=''.join(sorted(word))


def invert_dict(sorted_dict):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def metathesis_pair():
    for list in invert_dict(d):
        if(len(list)>=2):
            print(list)
            for i in range(len(list)-1):
               
                count = 0
                for c1, c2 in zip(list[i], list[i+1]):
                    if c1 != c2:
                        count += 1
                        if count>2:
                            print(list[i]+list[i+1])
read()
metathesis_pair()