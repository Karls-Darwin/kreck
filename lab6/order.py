from matrix import matrix

def order(m):
    order=len(m)

    return order

def main():
    n=int(input("Enter order of matrix: "))
    init=int(input("Enter initial value: "))
    print(order(matrix(n,init)))

if __name__ == '__main__':
    main()
