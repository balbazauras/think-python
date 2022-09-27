def has_duplicates(ls):
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i==j:
                continue
            else:
                if ls[i]==ls[j]:
                    return True
    return False
print(str(has_duplicates('123asdf')))