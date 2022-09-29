def word_list1(fin):
    word_list = [] # instanciates empty list

    for line in fin: # divides file in lines
        word = line.strip() #removes whitespaces from lines
        word_list.append(word) # adds words to list
    return word_list


def word_list2(fin):
    word_list = []
    for line in fin:
        word = line.strip()
        word_list = word_list + [word]
    return word_list

fin = open('Chapter10_lists/words.txt') #opens file stream
word_list1(fin)
word_list2(fin)


