def reverse(string):
    revlist=[]
    for i in range(len(string)):
        revlist.append(string[-1-i])
        revstring=''.join(revlist)
    return revstring



def main():
    x=input('Enter a string: ')
    print(reverse(x))

if __name__ == '__main__':
    main()
