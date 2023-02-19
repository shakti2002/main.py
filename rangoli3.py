import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.width(3)
t.speed("fastest")
col = ("magenta","purple","pink")
for i in range(220):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)
turtle.done()