d=dict()
fin = open('Chapter11_dict/words.txt')
def read():
    
    for line in fin:
        word=line.strip()
        d[word]=1

read()
print('asd'in d)

