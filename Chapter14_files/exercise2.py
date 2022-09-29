from anagrams_sets  import all_anagrams, signature
import shelve
def store_anagrams(filename, anagram_map):
    '''
    stores the anagram dictionary in a “shelf”
    '''
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()

def read_anagrams(filename, word):
    '''
    look up a word and return a list of its anagrams
    '''
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []

anagram_map = all_anagrams('Chapter14_files/words.txt')
store_anagrams('anagrams.db',anagram_map)
anagrams=read_anagrams('anagrams.db', 'asd')
print(anagrams)