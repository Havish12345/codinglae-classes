import turtle #importing library 
my_wn = turtle.Screen()
my_wn.bgcolor("light blue") #screen
my_wn.title("Turtle") #title
my_pen = turtle.Turtle() #turtle object
my_pen.color("red") #color
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
for i in range(0,10) :
   for i in range(4): 
     my_pen.fd(size + 1)
     my_pen.left(90)
     size = size - 5
     size = size + 1
