s=input("enter you introduction:")
characterCount=0
wordCount=1
for i in s :
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordCount+1
print("no of words:",wordCount)
print("no of characters:",characterCount)