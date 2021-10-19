# Take a list having dictionary elements as shown below (Sample Data) 
# and then store all the unique values into a list and print.

# [2', '7', '9', '5', '1'] 


dic=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, 
{"five":"5"},{"six":"9"},{"seven":"7"}]
    
# mylist=[]
# for x in range(len(dic)):
#     for j in dic[x]:

#         if dic[x][j] not in mylist:
#              mylist.append(dic[x][j])
# print(mylist)

b=[]
for i in dic:
    for j in i.values():
        if j not in b:
            b.append(j)
print(b)