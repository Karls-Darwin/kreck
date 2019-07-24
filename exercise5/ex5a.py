
def getMatrix():
    matrix=[]
    r=input("Matrix enter values separated by commas: ")
    while r!="":
        row=eval(r)
        rowdata=list(row)
        matrix.append(rowdata)
        r=input("Matrix enter values separated by commas: ")
    return matrix


def printMatrix(matrix):
    for row in matrix:
        for value in row:
            print(value,end="   ")
        print()

def main():
    printMatrix(getMatrix())

if __name__ == '__main__':
    main()
