#  Write a Python program to drop empty Items from a given Dictionary. 
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
for x,y in dict(dic).items():
    if y==None:
        dic.pop(x)
print(dic)