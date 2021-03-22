def revword(word):
    l=len(word)-1
    newword=''
    for letter in word:
        w=word[l]
        l=l-1
        newword=newword+w       
    return newword.lower()

def countword():
    text=open('text.txt')
    word=text.readline().rstrip()
    count=1
    for line in text:
         newline=''
         words=line.split()
         for i in words:
             new=revword(i)
             if new==word:
                 count=count+1
             newline=newline+' '+new
         #print(newline.rstrip())
    return count           


  