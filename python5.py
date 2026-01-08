dct = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
new = {}
for k , v in dct.items():
    for j in range(len(v)):
        v[j] = v[j]+3
    new[k] = v
print(new)