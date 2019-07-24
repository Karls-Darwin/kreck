import turtle
import math
import random
turtle.xcor=random.uniform(-1,1)
turtle.ycor=random.uniform(-1,1)
xcor=turtle.xcor*150
ycor=turtle.ycor*150
turtle.setworldcoordinates(-150,-150,150,150)
turtle.penup()
turtle.speed(1000)
i=0
g=0
r=0

while i<=1000:
  i=i+1
  xcor=random.uniform(-1,1)*150
  ycor=random.uniform(-1,1)*150
  turtle.goto(xcor,ycor)
  if math.sqrt((xcor)**2+(ycor)**2)<=150:
      turtle.dot(5,"green")
      g = g+1
  elif math.sqrt((xcor)**2+(ycor)**2)>150:
      turtle.dot(5,"red")
      r = r+1

totaldots=g+r
circle = totaldots - g

turtle.write(g/circle, True, align="center", font=("Arial",16,"normal"))
