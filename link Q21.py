# Write a Python program to check all values are same in a dictionary. 
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
dictionary={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12,
 'Pierre Cox': 12}
for i in dictionary:
    if dictionary[i]==10:
        print(False)
    else:
        print(True)