def ispalindrome(string):
    x=string.lower()
    x=x.replace(" ","")
    x=x.replace("'",'')
    if x==reverse(x):
        return string + " is a palindrome!"
    else:
        return string + " is not a palindrome"


def reverse(string):
    revlist=[]
    for i in range(len(string)):
        revlist.append(string[-1-i])
        revstring=''.join(revlist)
    return revstring


def main():
    x=input('Enter a string: ')
    print(ispalindrome(x))
    again=input("Continue? (y/n): ")
    while again!="n":
        x=input('Enter a string: ')
        print(ispalindrome(x))
        again=input("Continue? (y/n): ")

if __name__ == '__main__':
    main()
