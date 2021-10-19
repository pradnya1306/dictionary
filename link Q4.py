# Write a Python program to sum all the items in a dictionary.
mydic={'a':1,'b':2,'c':3,'d':4,'e':8}
sum=0
for i in mydic:
    sum=sum+mydic[i]
print(sum)