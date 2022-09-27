
'''
Write a function called is_sorted that takes a list 
as a parameter and returns True if the list is sorted 
in ascending order and False otherwise. For example:
'''
num_list=[1,2,3,4,3,6,7,8,9]
letter_list=['a','b,','c','d','a']
def is_sorted(list_to_check):
    continiuos=True
    for i in range(len(list_to_check)-1):
        if not list_to_check[i]<list_to_check[i+1]:
            continiuos=False
    return continiuos

print(str(is_sorted(letter_list)))

