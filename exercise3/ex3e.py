def gcd(a,b):
    if b==0:
        return a
    elif a==0:
        return b
    while abs(a)%abs(b)!=0:
        r=a%b
        a=b
        b=r
    if abs(a)%abs(b)==0:
        return b



def main():
    while True:
        a=(input("Enter first value: "))
        if a==str(""):
            print()
            break

        else:
            a=int(a)
            b=int(input("Enter second value: "))
            print ('The GCD of ',a,'and ',b,' is', gcd(a,b))



if __name__ == '__main__':
    main()
