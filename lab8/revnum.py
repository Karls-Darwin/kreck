from math import log10
def reverseNum(n):
    if n<10:
        return n
    else:
        ones=n%10
        rest=n//10
        return ones*10**int(log10(rest)+1)+ reverseNum(rest)

def main():
    print(reverseNum(123))

if __name__ == '__main__':
    main()
