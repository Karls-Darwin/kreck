def passwordCheck(password):
    digits=0
    if len(password)<8:
        return password, "is not a valid pasword"
    while len(password)>=8:
        i=0
        upper=0
        digit=0
        nonalpha=0
        for i in password:
            if i.isupper()==True:
                upper=True
            elif not i.isalpha==True and not i.isnumeric()==True:
                nonalpha=True
            elif i.isnumeric:
                digit+=1

        if upper==True and digit>=2 and nonalpha==True:
            return password, "is a valid password"
        else:
            return password, "is not a valid password"



def main():
    password=input("Enter a password: ")
    print (passwordCheck(password))


if __name__ == '__main__':
    main()
