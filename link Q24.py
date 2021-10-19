# Write a Python program to create and display all combinations of letters,
#  selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
data ={'1':['a','b'], '2':['c','d']}
for i in data:
    for n in range(len(data[i])):
         print(data[i][n],data[i][n]+1)