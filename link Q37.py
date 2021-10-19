dic={"a":20,"b":40,"c":{"p":50,"r":30,"d":{"v":20,"m":40}}}
sum=0
for i in dic.values():
    if type(i)==dict:
        
        for j in i.values():
            if type(j)==dict:
                
                for k in j.values():
                    sum=sum+k
            else:
                sum=sum+j
    else:
        sum=sum+i
print(sum)

