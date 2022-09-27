word='gmegmeiovrnoieifhwofejwmqdmpqmdvmpamvwrvpe'
def most_frequent(word):
    d=dict()
    for char in word:
        d[char]=word.count(char)
    return d


def sort(d):
    sorted_keys = sorted(d, key=d.get) 
    sorted_dict = {}
    for w in sorted_keys:
        sorted_dict[w] = d[w]
    return sorted_dict



d=most_frequent(word)
sort(d)
print(d)