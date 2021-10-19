dic={'bijender':45,'deepak':60,'param':20,
'anjili':30,'roshini':50}


#desending
# mydic={}
# for i in range (len(dic)):
#     max=0
#     for i in dic:
#         if dic[i]>max:
#             max=dic[i]
#             h=i
#     mydic.update({h:max})
#     dic.pop(h)
# print(mydic)

# asending
mydic={}
for i in range (len(dic)):
    mini=dic['bijender']
    for i in dic:
        if dic[i]<mini:
            mini=dic[i]
            h=i
    mydic.update({h:mini})
    dic.pop(h)
print(mydic)

# n=[20,30,45,50,60]
# for i in n:
#     for j in dic:
#         if dic[j]==i:










# Asending ordre
# a={}
# for  key, value in sorted(dic.items(),key=lambda item: item[1]):
#     a.update({key: value})
# print(a)

#descending order
# a={}
# for key, value in sorted( dic.items(), key=lambda item: item[1],
#                             reverse=True):
#     a.update({key:value})
# print(a)