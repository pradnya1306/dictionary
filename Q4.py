


dic= {1: 'NAVGURUKUL',
        2: 'IN',  
          3:{    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'}}



# del dic[3]["A"]
# print(dic)

for x in dic:
  if type(dic [x])==dict:
    for j in dic[x]:
      if dic[x][j]=="WELCOME":
        c=j
        del dic[c]
  
print(dic)
     

# for x in dic:
#   if type(dic [x])==dict:
#     for j in dic[x]:
#         print(dic[x][j])
#   else:
#     print(dic[x])

# a={1:{2:"two",3:"three"},2:{4:"four",5:"five"},3:{6:"six",7:"seven"}}
# for x in a:
#   for j in a[x]:
#     print(a[x][j])
#     # print(a[j])