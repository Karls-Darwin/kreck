def emul(a,b):
    if a==0 or b==0:
        product=0
    elif a>b:
        product=0
        while abs(b)>=1:
            if abs(b)%2==1:
                product+=a
            a=abs(a)*2
            b=abs(b)//2

    elif b>=a:
        product=0
        while abs(a)>=1:
            if abs(a)%2==1:
                product+=b
            b=abs(b)*2
            a=abs(a)//2

    return product



def main():
  a=int(input("Enter a value for a: "))
  b=int(input("Enter a value for b: "))
  print(emul(a,b))

if __name__ == '__main__':
    main()
