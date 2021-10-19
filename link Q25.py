a=[1,2,3,4,5,6]
b={}
for i in a[::-1]:
    b={i:b}
print(b)