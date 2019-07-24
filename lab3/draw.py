import turtle
turtle.speed(5)
def drawsquarefunc(length):
  turtle.fd(length)
  turtle.left(90)
  turtle.fd(length)
  turtle.left(90)
  turtle.fd(length)
  turtle.left(90)
  turtle.fd(length)
  turtle.left(90)


def main():
  for i in range(1,11):
    drawsquarefunc(100)
    turtle.left(36)

if __name__ == '__main__':
    main()
