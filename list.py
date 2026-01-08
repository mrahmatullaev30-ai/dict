ids = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
scores = [85, 98, 89, 92]

result = [
    {i: {n: s}}
    for i, n, s in zip(ids, names, scores)
]

print(result) # list


ids = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
scores = [85, 98, 89, 92]

result = []

for i in range(len(ids)):
    result.append({
        ids[i]: {names[i]: scores[i]}
    })

print(result)

