
file_name="Chapter13_case/emma.txt"

def read_to_list(file_name):
    word_list=list()
    fin=open(file_name)
    for line in fin:
        words=line.split() #split line into words    
        for word in words: # traverse through words in list
          word_list.append(word)
    return word_list

def markov(word_list):
    markov_dict=dict()
    suff_dict=dict()
    for i in range(len(word_list)-1):

        key = markov_dict[word_list[i]]
        if key in markov_dict:
            markov_dict[key].append(word_list[i])
        else:
            markov_dict[key] = [word_list[i]]
        index += 1


markov(read_to_list(file_name))


   

#print(markov(read_to_list(file_name)))
