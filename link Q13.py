name=["pradnya"]
i=0
mydic={}
while i<len(name):
    j=0
    while j<len(name[i]):
        
        mydic.update({name[i][j]:j})
        j=j+1
    i=i+1
print(mydic)

# new={}
# for i in range(len(name)):
#     # print(name[i])
#     for j in range(len(name[i])):
#         # print(name[i][j])
#         new.update({name[i][j]:j})
# print(new)



