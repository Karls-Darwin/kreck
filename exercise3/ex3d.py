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
    t2.pu()
    t2.goto(150,0)
    t2.shapesize(1)
    t2.color("green")
    t2.shape("circle")
    t3=turtle.Turtle()
    t3.shape("circle")
    t3.shapesize(0.5)
    t3.color("grey")
    t3.pu()
    t3.goto(180,0)
    while deg<1080:
        deg+=2
        t2.goto(150*math.cos(deg*math.pi/180),150*math.sin(deg*math.pi/180))
        deg2=0
        while deg2<360:
            x=(150*math.cos(deg*math.pi/180)+(80*math.cos(deg2*math.pi/180)))
            y=(150*math.sin(deg*math.pi/180)+(80*math.sin(deg2*math.pi/180)))
            t3.goto(x,y)
            deg2+=5


def main():
    sun()
    planet()

if __name__ == '__main__':
    main()
