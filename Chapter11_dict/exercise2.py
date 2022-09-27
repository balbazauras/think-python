def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key) # If the key does not exist, insert the key, with the specified value,
    return inverse
my_dict = dict([(1,'apple'), (2,'ball')])
print(invert_dict(my_dict))