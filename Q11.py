# Write a program to print the top 3 highest values of a 
# given dictionary.


my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
list=[]
for j in range (3):
    max=0
    for i in my_dict:
        if my_dict[i]>max:
            max=my_dict[i]
            m=i
    list.append(my_dict[m])
    my_dict.pop(m)
print(list)
        

# max=0
# for i in my_dict:
#     if my_dict[i]>max:
#         max=my_dict[i]
# print(max)