def reverse(string):
    x=""
    i=-1
    while abs(i)<len(string)+1:
        x+=string[i]
        i-=1
    return x


def main():
    x=input('Enter a string: ')
    print(reverse(x))

if __name__ == '__main__':
    main()
