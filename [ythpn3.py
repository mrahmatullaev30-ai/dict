import os
os.system("cls")

number = ['S001', 'S002', 'S003', 'S004']
ism = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
num = [85, 98, 89, 92]
lst = []
for i in range(len(number)):
    lst.append({number[i]: {ism[i]: num[i]}})
print(lst)
