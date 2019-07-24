def binaryToInt(binarystring):
    i=0
    total=0
    j=len(binarystring)-1
    while i<len(binarystring):
        if int(binarystring[i])==1:
            value=2**j
            total+=value
        j-=1
        i+=1
    return total


def main():
    binary=input("Enter a binary value: ")
    binarylist=list(binary)
    print("Value is:",binaryToInt(binarylist))
    again=input("Continue? (y/n): ")
    while again=="y":
        binary=input("Enter a binary value: ")
        binarylist=list(binary)
        print("Value is:",binaryToInt(binarylist))
        again=input("Continue? (y/n): ")


if __name__ == '__main__':
    main()
