def sieve(n):
    mylist=[]
    for number in range(2,n+1):
        mylist.append(number)
    p=2
    while p<len(mylist):
        for i in range(2,len(mylist)-1):
            product=p*i
            for j in mylist:
                if j==product:
                    j=0
                    print(True)

        p+=1

    return mylist


def main():
    n=int(input("Enter a number: "))
    print(sieve(n))

if __name__ == '__main__':
    main()
