'''
Write a function called chop that takes a list, 
modifies it by removing the first and last elements, 
and returns None. For example:
'''

num_list=[1,2,3,4,5,6,7,8,9]

def chop(num_list):
    del num_list[0]
    del num_list[len(num_list)-1]
    return None

chop(num_list)
print(num_list)