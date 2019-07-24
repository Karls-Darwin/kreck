def altSum(values):
    total=0
    i=0
    while i<len(values):
        if i%2==1:
            total-=values[i]
        else:
            total+=values[i]
        i+=1
    return total


def main():
    values=[]
    number=input("Enter a floating point value: ")
    if number!='':
        number=float(number)
    while number!="":
        values.append(number)
        number=input("Enter a floating point value: ")
        if number!="":
            number=float(number)
    print(altSum(values))

if __name__ == '__main__':
    main()
