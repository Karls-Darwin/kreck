import random

def matrix(n,init):
    mymatrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(init)
        mymatrix.append(row)
    return mymatrix

def populate(m,n,value):
    for i in range(n):
        j=random.randint(0,len(m)-1)
        k=random.randint(0,len(m)-1)
        m[j][k]=value
    return(m)

def main():
    print(populate(matrix(5,0),5,1))


if __name__ == '__main__':
    main()
