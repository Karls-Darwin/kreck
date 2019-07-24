import random
import turtle
turtle.speed(50)
turtle.setworldcoordinates(-100,-100,100,100)
i=0
xcor=turtle.xcor()
ycor=turtle.ycor()
while xcor>-100 and xcor<100 and ycor>-100 and ycor<100:
  output=random.randint(1,4)
  heading=(output-1)*90
  turtle.setheading(heading)
  turtle.fd(20)
  i=i+1
  xcor=turtle.xcor()
  ycor=turtle.ycor()
print(i)
turtle.penup()
turtle.goto(0,0)


turtle.write(i,align="right",font=(20))
