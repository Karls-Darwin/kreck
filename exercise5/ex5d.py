def shortestDist(alist):
    difx=alist[0][0]-alist[1][0]
    dify=alist[0][1]-alist[1][1]
    shortest=((difx**2)+(dify**2))**0.5
    outer=0
    while outer<len(alist)-1:
        inner=outer+1
        while inner<len(alist):
            x=alist[outer][0]-alist[inner][0]
            y=alist[outer][1]-alist[inner][1]
            distance=((x**2+y**2)**0.5)
            if shortest>distance:
                shortest=distance
            inner+1
        outer+=1
    return shortest


def getMatrix():
    matrix=[]
    r=input("Matrix enter values separated by commas: ")
    while r!="":
        row=eval(r)
        rowdata=list(row)
        matrix.append(rowdata)
        r=input("Matrix enter values separated by commas: ")
    return matrix


def main():
    a=getMatrix()
    print(shortestDist(a))

if __name__ == '__main__':
    main()
