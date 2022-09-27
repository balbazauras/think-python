'''
Write a function called middle that takes a list and 
returns a new list that contains all but the first and 
last elements. For example:
'''

num_list=[1,2,3,4,5,6,7,8,9]
print(num_list)
def middle(num_list):
    del num_list[0]
    del num_list[len(num_list)-1]

middle(num_list)
print(num_list)