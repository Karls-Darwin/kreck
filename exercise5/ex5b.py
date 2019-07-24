def matrixSum(A,B):
    AplusB=[]
    for i in range(len(A)):
        x = []
        for j in range(len(A[0])):
            x+=[A[i][j]+B[i][j]]
        AplusB+=[x]
    return AplusB

def sizeMatch(A,B):
    rowsA=len(A)
    rowsB=len(B)
    colsA=len(A[0])
    colsB=len(B[0])
    if rowsA==rowsB and colsA==colsB:
        return True
    else:
        return False


def getMatrix():
    matrix=[]
    r=input("Matrix enter values separated by commas: ")
    while r!="":
        row=eval(r)
        rowdata=list(row)
        matrix.append(rowdata)
        r=input("Matrix enter values separated by commas: ")
    print("Matrix B: ")
    return matrix



def printMatrix(matrix):
    for row in matrix:
        for value in row:
            print(value,end="   ")
        print()

def main():
    a = getMatrix()
    b = getMatrix()
    if sizeMatch(a,b):
        printMatrix(matrixSum(a,b))
    else:
        print("Error: cannot sum matrices of different sizes")


if __name__ == '__main__':
    main()
