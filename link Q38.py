# Write a Python program to filter even numbers from a given dictionary values. 
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}


dic={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1,8,3]}
for i in dic:
    for j in dic[i]:
        if j%2!=0:
            dic[i].remove(j)
print(dic)