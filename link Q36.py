# Write a Python program to convert a given dictionary into a list of lists. 
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
m=[]
for x,y in dic.items():
       k=[x,y]
       m.append(k)
print(m)
