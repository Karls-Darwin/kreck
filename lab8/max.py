def maxValue(vals):
    if len(vals)==1:
        return vals[0]
    else:
        if vals[0]>vals[-1]:
            del vals[-1]
        elif vals[0]<=vals[-1]:
            del vals[0]
        return maxValue(vals)


def main():
    vals=input("Enter values separated by commas: ")
    vals=vals.split(",")
    print(maxValue(vals))

if __name__ == '__main__':
    main()
