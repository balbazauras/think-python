
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

read()
pprint.pprint(invert_dict(d))