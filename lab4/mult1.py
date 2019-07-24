def mul(a,b):
  if a==0 or b==0:
    return 0
  elif a>b:
    y=1
    product=0
    while y<=b:
      y=y+1
      product=product+a
    return product
  elif b>=a:
    y=1
    product=0
    while y<=a:
      y=y+1
      product=product+b
    return product


def main():
  a=int(input("Enter a value for a: "))
  b=int(input("Enter a value for b: "))
  print(mul(a,b))

if __name__ == '__main__':
    main()
