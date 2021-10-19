# Write a Python program to remove duplicates from Dictionary.
student_data = {
   'id1':  {'name': ['Sara'], 
      'class': ['V'], 
      'subject_integration': ['english, math, science']},
   'id2': 
       {'name': ['David'], 
      'class': ['V'], 
      'subject_integration': ['english, math, science'] },
   'id3': 
      {'name': ['Sara'], 
      'class': ['V'], 
      'subject_integration': ['english, math, science']},
   'id4': 
         {'name': ['Surya'], 
         'class': ['V'], 
         'subject_integration': ['english, math, science']}}


a={}
for i in range(len(student_data)):
   for j in student_data:
      if (student_data[j]) not in a:
          a.update({j:student_data[j]})
#    # for j in student_data[i]:
print(a)
         

      


