
import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(1000,1000)
t = turtle.Turtle()
t.speed(0)
no_of_sides =4
side_length = 100
angle = 360.0 / no_of_sides
for i in range(no_of_sides):
    t.forward(side_length)
    t.right(angle)
turtle.done()










