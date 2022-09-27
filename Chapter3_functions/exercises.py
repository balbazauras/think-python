'''
Exercise 1
Write a function named right_justify that takes a string named
s as a parameter and prints the string with enough leading
spaces so that the last letter of the string is in column
70 of the display.
'''
def right_justify(s):
    num=70-len(s)
    print(" "*num+s)
right_justify('monty')


'''
Execercise 2
 A function object is a value you can assign to a variable or 
 pass as an argument. For example, do_twice is a function that 
 takes a function object as an argument and calls it twice
'''


def do_twice(f,a):
    f(a)
    f(a)

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(function, argurment):
    do_twice(function,argurment)
    do_twice(function,argurment)

do_four(print,'Labas as krabas')
'''
Exercise 3
This exercise should be done using only the 
Statements and other features we have learned so far.
'''

def print_dashes_for2x2(char):
    print(char," "*4,char," "*4,char)

def print_dashes_for4x4(char):
    print(char," "*4,char," "*4,char," "*4,char," "*4,char)
def print_grid2x2():
    print("+","-"*4,"+","-"*4,"+")
    do_four(print_dashes_for2x2,"/")
    print("+","-"*4,"+","-"*4,"+")
    do_four(print_dashes_for2x2,"/")
    print("+","-"*4,"+","-"*4,"+")
print_grid2x2()

def print_grid4x4():
    print("+","-"*4,"+","-"*4,"+","-"*4,"+","-"*4,"+")
    do_four(print_dashes_for4x4,"/")
    print("+","-"*4,"+","-"*4,"+","-"*4,"+","-"*4,"+")
    do_four(print_dashes_for4x4,"/")
    print("+","-"*4,"+","-"*4,"+","-"*4,"+","-"*4,"+")
    do_four(print_dashes_for4x4,"/")
    print("+","-"*4,"+","-"*4,"+","-"*4,"+","-"*4,"+")
    do_four(print_dashes_for4x4,"/")    
    print("+","-"*4,"+","-"*4,"+","-"*4,"+","-"*4,"+")    
print_grid4x4()


