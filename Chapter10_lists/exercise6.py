
def is_anagram(word1,word2):
    w1=list(word1) #makes a list of of string
    w2=list(word2)
    w1.sort() # orders elements in string
    w2.sort()
    print(w1)
    print(w2)
    if w1 == w2:
        return True
    else:
        return False
word1='labas'
word2='basla'
print(str(is_anagram(word1,word2)))