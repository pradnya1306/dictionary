#  Write a Python program to create a key-value list pairings in a given dictionary. 
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 
# 5: 'Zachary Simon'}]


dic={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 
4: ['Lynne Foster'], 5: ['Zachary Simon']}
newdic={}
newlist=[]
for x,y in dic.items():
    if type(y)==list:
        for j in y:
            newdic.update({x:j})
newlist.append(newdic)
print(newlist)


