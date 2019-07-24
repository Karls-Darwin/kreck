import turtle
def drawstar(sidelength):
  turtle.left(36)
  turtle.fd(sidelength)
  turtle.left(144)
  turtle.fd(sidelength)
  turtle.left(144)
  turtle.fd(sidelength)
  turtle.left(144)
  turtle.fd(sidelength)
  turtle.left(144)
  turtle.fd(sidelength)
  turtle.left(144)

def main():
  sidelength=turtle.numinput("","Enter sidelength: ")
  drawstar(sidelength)

if __name__ == '__main__':
     main()
