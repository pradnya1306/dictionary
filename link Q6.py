# Write a Python program to iterate over dictionaries using for loops.
# dic={"a":1,"b":2,"c":3,"d":4,"f":5}
# for i in dic:
#     print(i)
#     print(dic[i])

a={"a":{'p':9,'y':8,'t':5},"b":{'v':4,'m':7,'r':9}}
for i in a:
    print("key",i)
    # print(a[i])
    for j in a[i]:
        print("dic key",j)
        print("values",a[i][j])
