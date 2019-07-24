def ltrcount(string):
    alphas=0
    for x in string:
        if x.isalpha():
            alphas+=1
    return alphas

def main():
    x=input("Enter string: ")
    print(ltrcount(x))

if __name__ == '__main__':
    main()
