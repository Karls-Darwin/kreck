def emul(a,b):
    if a==0 or b==0:
        product=0
    elif a>b and (a<0 or b<0):
        product = 0
        while abs(b)>=1:
            if abs(b)%2==1:
                product+=a
            a=abs(a)*2
            b=abs(b)//2
            finalprod = product
            finalprod = finalprod * (-1)

    
    elif a>b and (a<0 and b<0):
        product = 0
        while abs(b)>=1:
            if abs(b)%2==1:
                product+=a
            a=abs(a)*2
            b=abs(b)//2
            finalprod = product
            finalprod = abs(finalprod)

    elif b>=a and (a<0 or b<0):
        product=0
        while abs(a)>=1:
            if abs(a)%2==1:
                product+=b
            b=abs(b)*2
            a=abs(a)//2
            finalprod = product
            finalprod = finalprod * (-1)


    return finalprod



def main():
  a=int(input("Enter a value for a: "))
  b=int(input("Enter a value for b: "))
  print(emul(a,b))

if __name__ == '__main__':
  main()
