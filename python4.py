lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dct = {}
for i in lst:
    if i[0] not in dct:
        dct[i[0]]=[i[1]]
    else:
        dct[i[0]].append(i[1])
print(dct)
