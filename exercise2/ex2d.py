
def slope(x1,y1,x2,y2):
  if x1==x2:
    m=0
  elif y1==y2:
    m="Slope Undefined"
  else:
    m=(y2-y1)/(x2-x1)
  return m


def main():
  xcor1=int(input('Enter first x value: '))
  ycor1=int(input('Enter first y value: '))
  xcor2=int(input('Enter second x value: '))
  ycor2=int(input('Enter second y value: '))
  b=ycor1-(slope(xcor1,ycor1,xcor2,ycor2))*xcor1
  print("y=",slope(xcor1,ycor1,xcor2,ycor2), "x+",b)


if __name__ == '__main__':
    main()
