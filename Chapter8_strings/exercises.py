#Exercise2
word= "banana"
print(str(word.count('a'))) # count the occurances of 'a' in 'word'

#Exercise 3
print(word[::-1]) # print word backwards
def is_palindrome(word1): # function to check if string is palindrome
    return word1==word1[::-1]
print(str(is_palindrome("able was I ere I saw elba")))
long_word="Pneumonoultramicroscopicsilicovolcanoconiosis"
print(long_word[0:25:3]) # print every thrid symbol of the given string starting from symbol 0 upto symbol 24

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(str(any_lowercase5("asdawdadwdqad")))


def rotate_word(word,number):
    new_string=""
    for letter in word:
        new_string=new_string+ chr(ord(letter)+number)
    return new_string
print(rotate_word("labas",5))