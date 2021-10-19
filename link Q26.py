# Write a Python program to combine values in python list of dictionaries. 
# Expected Output: Counter({'item1': 1150, 'item2': 300})

data=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, 
{'item': 'item1', 'amount': 750}]
mydic={}
for i in range (len(data)):
    # print(i)
    for j in data[i]:
        key=data[i][j]
        value=data[i][j+1]
        mydic.update({key:value})
print(mydic)