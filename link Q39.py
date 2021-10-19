#  Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']
dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 
'h': 8, 'i': 100}
newlist=[]
for j in range (5):
    max=0
    for i in dic:
        if dic[i]>max:
            max=dic[i]
            m=i
    newlist.append(m)
    print(j+1,"maximum value in the dictionary",newlist)
    dic.pop(m)
# print(newlist)