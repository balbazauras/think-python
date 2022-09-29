import random

file_name="Chapter13_case/emma.txt"




def read_to_dict(file_name):
    word_dict=dict()
    fin=open(file_name)
    for line in fin:
        words=line.split() #split line into words    
        for word in words: # traverse through words in list
          if word not in word_dict: # checks if word is in dictionary
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

def build_list(word_dict):
    counter_list=list(word_dict.values())
    counter_sum=0
    cumulative_list=list()
    for counter in counter_list:
        counter_sum=counter_sum+counter
        cumulative_list.append(counter_sum)
    return cumulative_list






def binary_search(cumulative_list,random_value):
 
    index=round(len(cumulative_list)/2) # divides number of items in list into two halfs
    print("Number of items in list:" +str(len(cumulative_list)))
    index_ans=0
    while True:
        if cumulative_list[index] >random_value:
            cumulative_list=cumulative_list[:index]
        else:
            cumulative_list=cumulative_list[index:]
        index=round(len(cumulative_list)/2)
        print("index:"+str(index))
        print("value:"+str(cumulative_list[index]))
        index_ans=index_ans+index
        if( cumulative_list[index-1] < random_value and random_value <= cumulative_list[index]):
            return index_ans

word_dict=read_to_dict(file_name)
cumulative_list=build_list(word_dict)
random_value=(random.uniform(0,len(word_dict)))
indexas =binary_search(cumulative_list,random_value)
key_list=list(word_dict.keys())
print(key_list[indexas])


