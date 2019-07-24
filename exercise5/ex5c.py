def insertString(alist,newword):
    i=0
    newlist=[]
    found=False
    while i < len(alist)+1 and found==False:
        if i==len(alist) and found==False:
            newlist.append(newword)
        else:
            if alist[i]<newword:
                newlist.append(alist[i])
            elif alist[i]>newword:
                newlist.append(newword)
                newlist+=alist[i:]
                found=True
        i+=1
    return newlist

def main():
    somelist=[]
    newword=input("Enter word: ")
    while newword!="":
        somelist=insertString(somelist,newword)
        newword=input("Enter word: ")
    print(somelist)



if __name__ == '__main__':
    main()
