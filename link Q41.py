mylist=[[2,"'pradnya","poonam"],[3,"rutuja","rushi"]]
dic=[]
for i in range(len(mylist)):
    for j in range(len(mylist[i]-2)):
        key=mylist[i][j]
        value=(mylist[i][j+1],mylist[i][j+2])
        dic.update({key:value})
print(dic)
