import turtle
import math


def sun():
    t1=turtle.Turtle()
    t1.hideturtle()
    t1.speed(0)
    t1.penup()
    t1.goto(0,-40)
    t1.pendown()
    t1.pencolor('yellow')
    t1.begin_fill()
    t1.circle(40)
    t1.fillcolor('yellow')
    t1.end_fill()

def planet():
    deg=0
    t2=turtle.Turtle()
    t2.color("green")
    t2.shape("circle")
    t2.pu()
    t2.goto(150,0)

    while deg<1080:
        deg+=1
        t2.goto(150*math.cos(deg*math.pi/180),150*math.sin(deg*math.pi/180))

def main():
    sun()
    planet()


if __name__ == '__main__':
    main()
