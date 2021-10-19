# 39.Write a Python program to filter a dictionary based on values. 
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
dictionary={'Cierra Vega': 175, 'Alden Cantrell': 180, 
'Kierra Gentry': 165, 'Pierre Cox': 190}
newdic={}
for i in dictionary:
    if dictionary[i]>170:
        newdic.update({i:dictionary[i]})
print(newdic)

