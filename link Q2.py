# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}


string='w3resource'
dic={}
for i in range(len(string)):
    count=0
    for j in range(len(string)):
        if string[i]==string[j]:
            count=count+1
            # key=string[i]
            # value=count
            dic.update({string[i]:count})
print(dic)
#       dic.update({string[i]:i})
# print(dic)
