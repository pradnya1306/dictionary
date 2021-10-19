dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 

         'David': ['subj1', 'subj2']}
   
count=0
for x,y in dict.items():
   for j in y:
      count=count+1
      # print(j)
print(count)