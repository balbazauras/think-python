import string


file_name1="Chapter13_case/emma.txt"
file_name2="Chapter13_case/words.txt"


def read_to_set(file_name):
    s=set()
    fin=open(file_name)
    for line in fin:
        words=line.split()
        for word in words:
            word=word.translate(str.maketrans('', '', string.punctuation)) #remove all charakters found in string.punctuation
            word=word.lower()
 
            s.add(word)
    
    return s
set1=read_to_set(file_name1)
set2=read_to_set(file_name2)
print(set1.difference(set2))
print(string.punctuation)

