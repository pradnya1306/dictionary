# Write a Python program to count the number of items in a dictionary value that is a list.

# Sample output: 5

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for x,y in dict.items():
    for j in y:
        
        count+=1
print(count)