# Write a Python program to get the maximum and minimum value in a dictionary.
mydic={'a':9,'b':2,'c':3,'d':4,'e':8}
# max=0
# for i in mydic:
#     if [i]>max:
#         max=[i]
# print(max)

mini=mydic["a"]
for i in mydic:
    if mydic[i]<mini:
        mini=mydic[i]
print(mini)
