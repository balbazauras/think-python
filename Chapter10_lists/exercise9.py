def word_list1(fin):
    word_list = []

    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def word_list2(fin):
    word_list = []
    for line in fin:
        word = line.strip()
        word_list = word_list + [word]
    return word_list

fin = open('Chapter10_lists/words.txt')
word_list1(fin)
word_list2(fin)


