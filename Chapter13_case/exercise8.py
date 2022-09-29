import pprint, string
from random import randrange
file_name="Chapter13_case/emma.txt"

def read_to_list(file_name):
    word_list=list()
    fin=open(file_name)
    for line in fin:
        words=line.split() #split line into words    
        for word in words: # traverse through words in list
        
          word_list.append(word.translate(str.maketrans('', '', string.punctuation)))
    return word_list

def markov(word_list):
    markov_dict=dict()
    for i in range(len(word_list)-1): #create empty dict
        markov_dict[word_list[i]]={}

    for i in range(len(word_list)-1):
        next_word=word_list[i+1] 
        current_word=word_list[i]
        if(next_word in markov_dict[current_word]):
            markov_dict[current_word][next_word]+=1
        else:
            markov_dict[current_word][next_word]=1
    return markov_dict
                
def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key   

def return_word(key,markov_dict):
    occurance_sum=0
    for ls in markov_dict[key].keys():
        occurance_sum+=markov_dict[key][ls] #sums all possible word occurances to calculate probability
    random_value_occurance=randrange(occurance_sum) # create random number in range from 0 to number occurance sum
    counter=0
    for i in range(random_value_occurance):
        occurance_sum+=markov_dict[key][ls]
        counter+=1
        return markov_dict[key].key()


markov_dict=markov(read_to_list(file_name))
random_value=randrange(len(markov_dict))
key=get_nth_key(markov_dict,random_value)
print(return_word(key,markov_dict))






