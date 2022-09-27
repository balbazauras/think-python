
def has_duplicates2(ls):
    inverse = dict()
    for value in ls:
        if value not in inverse:
            inverse[value] = [1]
        else:
            return True
    return False

print(str(has_duplicates2('123asdf1')))
