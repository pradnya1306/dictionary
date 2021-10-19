# Write a Python program to convert more than one list to nested dictionary. 
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]


p=['S001', 'S002', 'S003', 'S004']
l=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
m=[85, 98, 89, 92]
# i=0
# k=[]
# while i <(len(p)):
#     n=({l[i]:m[i]})
#     z=({p[i]:n})
#     k.append(z)
#     i=i+1
# print(k)
k=[]
for i in range(len(p)):

    n=({l[i]:m[i]})

    z=({p[i]:n})
    k.append(z)
print(k)
