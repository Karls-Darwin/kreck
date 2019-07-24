import turtle
from sparse import matrix

screen=turtle.getscreen()
screen.tracer(0)


def showMatrix(turtle_object,m):
    screen.setworldcoordinates(0,0,len(m)-1,len(m)-1)
    turtle_object=turtle.Turtle()

    turtle_object.penup()
    turtle_object.color("red")

    for i in range(len(m)-1):
        for j in range(len(m)-1):
            if m[i][j]!=0:
                turtle_object.goto(i,j)
                turtle_object.dot()


    screen.update()

def main():
    Fred=0
    showMatrix(Fred,matrix(5,4))

if __name__ == '__main__':
    main()
