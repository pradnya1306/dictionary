# Python: Print a dictionary line by line
# Sample Output:

# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 

students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for i in students:
    print(i)
    for x,y in students[i].items():
        print(x,":",y)
    