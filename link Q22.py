
# Write a Python program to find the length of a given dictionary values. 
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}

dictionary={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
newdic={}
for i in dictionary:
    length=len(dictionary[i])
    newdic.update({dictionary[i]:length})
print(newdic)



