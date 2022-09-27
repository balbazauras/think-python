fin = open('words.txt')
fin1= open('words.txt')
#for line in fin:
#   word=line.strip()
#    if(len(word)>=15):
#        print(word)

def has_no_e():
    counter=0
    for line in fin1:
        word=line.strip()
        contains=False
        for symbol in word:
            if(symbol=='e'):
                contains=True
        if not(contains):
            counter+=1
    fin.close()
    return counter
    
#num_lines = sum(1 for line in fin)
#print(str(num_lines/has_no_e()))

#Exercise 3  
#Write a function named avoids that takes a word and a 
# string of forbidden letters, and that returns True 
# if the word doesn’t use any of the forbidden letters.
def avoids(word,forbidden):
    for symbol in word:
        for f in forbidden:
            if(symbol==f):
                return True
    return False
'''
forbidden=input("Enter forbidden letters: ")
counter=0

for line in fin:
    word=line.strip()
    if not(avoids(word,forbidden)):
        counter+=1
print(str(counter))
'''


#Exercise 5
#Write a function named uses_all that takes a word and a 
# string of required letters, and that returns True if t
# he word uses all the required letters at least once. 
# How many words are there that use all the vowels aeiou? 
# How about aeiouy?

def count_unique_symbols(word):
    unique = []
    for char in word[::]:
        if char not in unique: 
            unique.append(char)
    return (len(unique))

def uses_all(word,letters):
    contains=""
    for symbol in word:
        for letter in letters:
            if symbol==letter:
                if contains.count(letter)==0:
                    contains = letter + contains
       
        if len(contains)==count_unique_symbols(letters):
            return True
'''
letters=input("Enter letters: ")
counter=0
for line in fin:
    word=line.strip()
    if (uses_all(word,letters)):
        counter+=1
print(str(counter))
'''


# Exercise 6:
"""
Write a function called is_abecedarian that returns 
True if the letters in a word appear in alphabetical order 
(double letters are ok). 
How many abecedarian words are there?
"""

def is_abecedarian(word):
    continiuos=True
    number=0
    while number <len(word)-1: 
        first_letter_number=ord(word[number])
        second_letters_number=ord(word[number+1])
        if not(second_letters_number-first_letter_number==1 or second_letters_number-first_letter_number==0):
            continiuos=False
            break
        number+=1
    return continiuos

to_check=input("Enter word: ")
print(is_abecedarian(to_check))
    
