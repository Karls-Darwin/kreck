def convert(char):
    if (char == 'I'):
        return 1
    elif (char == 'V'):
        return 5
    elif (char == 'X'):
        return 10
    elif (char == 'L'):
        return 50
    elif (char == 'C'):
        return 100
    elif (char == 'D'):
        return 500
    elif (char == 'M'):
        return 1000
    else:
        return 0


def romanToDecimal(numeral):
    total=0
    i=0
    while i<len(numeral):
        digit1=convert(numeral[i])
        if i<len(numeral)-1:
            digit2=convert(numeral[i+1])
            if digit1>=digit2:
                total+=digit1
                i+=1
            else:
                total-=digit1
                i+=1
        else:
            total+=digit1
            i+=1
    return total




def main():
    numeral=input("Enter a roman numeral: ")
    print(romanToDecimal(numeral))




if __name__ == '__main__':
     main()
