def identity(n):
  mymatrix=[]
  for i in range(n):
    row=[]
    for j in range(n):
        if i==j:
            row.append(1)
        else:
            row.append(0)
    mymatrix.append(row)

    print(mymatrix)



def main():
    n=int(input("Enter a number: "))
    identity(n)

if __name__ == '__main__':
    main()
