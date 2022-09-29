num_list=[1,2,3,4,5,6,7,8,9]
def cumsum(num_list):
    '''Write a function called cumsum that takes a list of
    numbers and returns the cumulative sum; that is, a new list
    where the ith element is the sum of the first i+1 elements from
    the original list. For example:
    '''
    ans=0
    cumulative_sum=num_list
    for number in num_list:
        ans=ans+number
    cumulative_sum.append(ans)
    return cumulative_sum
print(str(cumsum(num_list)))
