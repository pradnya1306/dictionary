# A Python Dictionary contains List as value. Write a Python program to clear 
# the list values in the said dictionary. 

# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

dict={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for x in dict:
    for y in dict[x]:
        dict[x].clear()
        
        
print(dict)
