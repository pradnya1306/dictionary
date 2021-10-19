rec = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}

id1 = id(rec)

# del rec

rec1 = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA","rollno.":12}

id2 = id(rec1)

print(rec == rec1)
