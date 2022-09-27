import pprint
import string
file_name1="Chapter13_case/arthur.txt"
file_name2="Chapter13_case/words.txt"

def read_to_dict(file_name):
    d=dict()
    fin=open(file_name)
    for line in fin:
        words=line.split() #split line into words    
        for word in words: # traverse through words in list
          if word not in d: # checks if word is in dictionary
            d[word] = 1
        else:
            d[word] += 1
    return d

def count_total(d):
    counters=d.values() #get a list of values from dict
    total=0
    for number in counters: # iterates through numbers in list
        total=total+number
    return total

def compare_lists(list1,list2):
    result=set()
    for word in list1:
        if word not in list2:
            result.add(word)

    return result

def read_to_list(file_name):
    l=list()
    fin=open(file_name)
    for line in fin:
        words=line.split()
        for word in words:
            word= word.translate(str.maketrans('', '', string.punctuation)) #remove all charakters found in string.punctuation
            word=word.lower()
            l.append(word)
    return l


dict_of_words1=read_to_dict(file_name1)
ditc_of_words2=read_to_dict(file_name2)
list_of_words1=read_to_list(file_name1)
list_of_words2=read_to_list(file_name2)
#sorted_dict=sorted(dict_of_words1.items(), key=lambda x: x[1]) #????
#pprint.pprint(sorted_dict)
#print("Total number of words: "+str(count_total(dict_of_words1)))
result=compare_lists(list_of_words1,list_of_words2)
print(result)
#for word in result[:20]:
 #   print(word)