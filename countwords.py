intro= input("enter your introduction?: ")
print(intro)
charactercount=0
wordcount=1
for i in intro:
    charactercount+=1
    if i==" ":
        wordcount+=1
print("number of words= ",wordcount)
print("number of characters= ",charactercount)