# Exercise 1
# Write a script that reads the current time and converts it to a time 
# of day in hours, minutes, and seconds, 
# plus the number of days since the epoch.

import time
seconds_left_in_day= time.time()%86400
current_hour=seconds_left_in_day//3600
current_minute=(seconds_left_in_day-(current_hour)*3600)//60
curret_second=seconds_left_in_day-current_hour*3600-current_minute*60
since_epoch= time.time()//86400
print("Current time: Hours: "+str(current_hour)+
" Minutes: "+str(current_minute)+
" Seconds: "+str(curret_second)+"\n")
print("Number of days since epoch: "+str(since_epoch))

# Exercise 2
# Write a function named check_fermat that takes four parameters—
# a, b, c and n—and checks to see if Fermat’s theorem holds. 
# If n is greater than 2 and
def check_fermat(a,b,c,n):
    if a**n+b**n==c**n:
        print("Holy smokes, Fermat was wrong!")
    else:    
        print("No, that dosen't work.")


# Excercise 3
# Write a function named is_triangle that takes three 
# integers as arguments, and that prints either “Yes” or “No”, 
# depending on whether you can or cannot form a triangle from 
# sticks with the given lengths.


#a=input("Please enter a: ")
#b=input("Please enter b: ")
#c=input("Please enter c: ")
#n=input("Please enter n: ")
#check_fermat(int(a),int(b),int(c),int(n))

def is_triangle(a,b,c):
    if(a+b<c or a+c<b or c+b<a):
        print("No")
    else:
        print("yes")



#a=input("Please enter a: ")
#b=input("Please enter b: ")
#c=input("Please enter c: ")
#is_triangle(int(a),int(b),int(c))



# Excercise 4
# What is the output of the following program? 
# Draw a stack diagram that shows the state of the program 
# when it prints the result.
'''
Adds n to s until n reaches 0
n: iterable number
s: number to add to
'''
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)


