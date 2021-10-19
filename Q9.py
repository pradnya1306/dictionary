word="MISSISSIPPI"

mydic={}
for i in range(len(word)):
    count=0
    for j in range(len(word)):
        if word[i]==word[j]:
            count+=1

        letter=word[i]
        num=count
        mydic.update({letter:num})
print(mydic)
