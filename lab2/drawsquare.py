import turtle
turtle.speed(15)
squares=turtle.numinput('',"Enter a number")
def drawsquarefunc(length):
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)


def main():
    i=1
    while i<=squares:
        i=i+1
        drawsquarefunc(100)
        turtle.left(360/squares)



if __name__ == '__main__':
    main()
