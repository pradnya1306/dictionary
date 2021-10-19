# Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
data={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for k in range(3):

    max=0
    for i in data:
        # print(i)
        if data[i]>max:
            max=data[i]
            h=i
    data.pop(h)
            
    print(h,max)