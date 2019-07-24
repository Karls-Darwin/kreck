def compound_interest(amount,target,interest):
    years=0
    total=amount
    while total<target:
        years+=1
        total=total+(total*interest)
    return years


def main():
    amount=float(input("Enter starting amount: "))
    target=float(input("Enter target amount: "))
    interest=float(input("Enter interest rate: "))
    print(compound_interest(amount,target,interest), "year(s)")

if __name__ == '__main__':
    main()
