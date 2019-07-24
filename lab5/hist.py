import random

def roll():
  i=1
  hist=[0,0,0,0,0,0,0,0,0,0,0] #hist = [0]*11
  while i<10000:
      r1=random.randint(1,6)
      r2=random.randint(1,6)
      total=r1+r2
      hist(total-2)+=1
      i=+1

  return hist


def main():
    print(roll())

if __name__ == '__main__':
    main()
