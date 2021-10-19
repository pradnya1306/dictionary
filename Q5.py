list1=["one","two","three","four","five"]


list2=[1,2,3,4,5] 
# final=zip(list1,list2)
# final=dict(final)
# print(final)
mydic={}
for i in range (len(list1)):
    mydic.update({list1[i]:list2[i]})
print(mydic)

# mydic={}
# for i in range (len(list1)):
#     mydic[list1[i]]=list2[i]
#     print(mydic)


        
