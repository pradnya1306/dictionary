# Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
k=[]
for i in range (len(student)):
    # print(student[i])
    # sum=0
    for m,j in student[i].items():
        if m=="id":
            sum=sum+j
print({m:sum})



