import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,300)
t = turtle.Turtle()
t.speed(0)
no_of_sides = 8
side_length = 70
angle = 360.0 / no_of_sides
for i in range(no_of_sides):
    t.forward(side_length)
    t.right(angle)
turtle.done()





