def matrix(n,init):
    mymatrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(init)
        mymatrix.append(row)

    return mymatrix


def main():
    n=int(input("Enter order of matrix: "))
    init=int(input("Enter initial value: "))
    print(matrix(n,init))


if __name__ == '__main__':
    main()
