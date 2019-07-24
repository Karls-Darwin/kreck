import random

def craps():
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    initialroll=(r1,r2)
    print("Print the initial roll is: ", initialroll)
    if (r1+r2==7 or r1+r2==11):
        print("You win!")

    elif r1+r2==2 or r1+r2==3 or r1+r2==12:
        print("Craps! Sorry you lose")

    else:
        r3=0
        r4=0
        while r1+r2==(3,7) or r1+r2==(8,11):
            r3=random.randint(1,6)
            r4=random.randint(1,6)
            print("Roll is: [",a,",",b"]")
        if r3+r4==7 or r3+r4==r1+r2:
            print("You win")
        elif r3+r4==(3,7) or r3+r4==(8,11):
            print("You lose")

def main():
    craps()

if __name__ == '__main__':
    main()
