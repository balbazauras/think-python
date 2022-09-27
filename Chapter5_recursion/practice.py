# 5.9 Task:write a function called do_n that takes a 
# function object and a number, n, as arguments, 
# and that calls the given function n times.
def do_n(function,n):
    for i in range(n):
        function()

def printing_name():
    print("liudas")

do_n(printing_name,10)

name=input("what is your name\n")

print(name)