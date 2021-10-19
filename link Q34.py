# .Write a Python program to match key values in two dictionaries. 
# Expected output: key1: 1 is present in both x and y

dicx={'key1': 1, 'key2': 3, 'key3': 2} 
dicy={'key1': 1, 'key2': 2}

key=input("enter the key")
if key in dicx and key in dicy:
    print("exist")
else:
    print("not exist")