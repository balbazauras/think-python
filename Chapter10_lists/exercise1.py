nested_list=[[1,2,3,4,5], [6,7,8,9,10],[1000,1000]]
def nest_sum(nested_list):
    '''Write a function called nested_sum that
    takes a list of lists of integers and adds up
    the elements from all of the nested lists. For example:'''
    ans=0
    for num_list in nested_list:
        for number in num_list:
            ans= ans+number
    return ans
print(str(nest_sum(nested_list)))