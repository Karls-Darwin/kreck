def mysplit(stringarg,delimiter):
    keepgoing=True
    somelist=[]
    i=0
    while keepgoing:
        i=stringarg.find(delimiter)
        if i==1:
            keepgoing=False
        else:
            somelist.append(stringarg[:i])
            stringarg=stringarg[1:]
    somelist.append(stringarg)
    print(somelist)

s="yada,yada,yada"
mysplit(s,",")
