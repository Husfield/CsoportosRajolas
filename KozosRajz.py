#lámpatest
import turtle

turtle.width(3)

hossz=100
szog=90


#hatter
turtle.bgcolor("lightblue")

i=0
turtle.begin_fill()
while i<2:
    turtle.forward(60)
    turtle.left(szog)
    turtle.forward(210)
    turtle.left(szog)
    turtle.forward(60)
    i += 1

turtle.fillcolor("black")
turtle.end_fill()

#lampa korok es hatter

#zold
turtle.penup()
turtle.goto(0,15)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.circle(25)
turtle.fillcolor("green")
turtle.end_fill()

#sarga
turtle.penup()
turtle.goto(0,75)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(25)
turtle.fillcolor("yellow")
turtle.end_fill()

#piros
turtle.penup()
turtle.goto(0,135)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(25)
turtle.fillcolor("red")
turtle.end_fill()

turtle.done()