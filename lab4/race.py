import turtle
import random
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
turtle.setworldcoordinates(-150,-150,150,150)
t1.pu()
t2.pu()
t3.pu()
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t1.color("red")
t2.color("green")
t3.color("blue")
t1.shapesize(1,1,2)
t2.shapesize(1,1,2)
t3.shapesize(1,1,2)
t1.goto(-149,15)
t2.goto(-149,0)
t3.goto(-149,-15)


for xcor in range(300):
  t1.fd(random.randint(1,15))
  t2.fd(random.randint(1,15))
  t3.fd(random.randint(1,15))
