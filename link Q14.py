# Write a Python program to find the highest 3 values of corresponding 
# keys in a dictionary.
mydic={'a':1,'b':2,'c':3,'d':4,'e':8}

newdic=[]
for m in range (3):
    max=0
    for i in mydic:
        if mydic[i]>max:
            max=mydic[i]
            k=i
    newdic.append(mydic[k])
    mydic.pop(k)

print(newdic)
