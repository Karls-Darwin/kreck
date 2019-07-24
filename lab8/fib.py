def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        nums=fibonacci(n-1)+fibonacci(n-2)
        return nums

def main():
    n=int(input("Enter number: "))
    print(fibonacci(n))

if __name__ == '__main__':
    main()
