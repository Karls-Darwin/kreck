def perfect(n):
    total = 0
    divisor = 1
    while divisor <= n//2:
        if n % divisor==0:
            total += divisor
        divisor+=1
    if total == n:
        return True
    else:
        return False


def main():
    lower_bound=int(input("Enter lower bound: "))
    upper_bound=int(input("Enter upper bound: "))
    for n in range(lower_bound, upper_bound+1):
        if perfect(n) == True:
            print(n)


if __name__ == '__main__':
    main()
