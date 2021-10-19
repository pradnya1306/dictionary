


# unique Values
dic=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
unique=[]
for i in range(len(dic)):
    for j in dic[i]:
    
         if (dic [i][j]) not in unique:
             unique.append(dic[i][j])
print(unique)