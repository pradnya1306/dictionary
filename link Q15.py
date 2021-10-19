d={"t":{"A":20,"B":40},"C":{"P":50,"R":30,"D":40}}


for x in d:
    sum=0
    for j in d[x]:
        sum=sum+d[x][j]
print(sum)


a=["aaa","ssss","ddddd"]
b=[]
i=0
length=0
while i <len(a):
    # print(len(a[i]))
    if len(a[i])>length:
        length=len(a[i])
        k=a[i]
    # print(length)
    i=i+1
# print(length)
b.append(k)
print(b)
