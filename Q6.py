# Write a program to remove duplicate keys``.
# output= {“ball”:”red”,”bat”:4,”wickets”:8}


ic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}

mydic={}
for x in ic:
    mydic.update(x)
print(ic)

mydic={}
for x,y in ic.items():
    
    mydic.update({x:y})
if x not in mydic:
    mydic.update({x:y})
print(mydic)