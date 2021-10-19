# Write a Python program to map two lists into a dictionary.
mydic=['a','b','c','d']
value=[1,2,3,4]
j={}
for i in range(len(mydic)):
    j.update({mydic[i]:value[i]})
print(j)