
# take user input make nested dictionary .
length=int(input("enter the length"))
p={}
j={}
for i in range(length):
    key=int(input("enter the key"))
    value=int(input("enter the value"))
    key1=int(input("enter the key1"))
    p={key:value}
    j.update({key1:p})
print(j)
