import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pensize(2)
t.speed(15)

t.color("white","blue")
t.begin_fill()
for i in range(0,12):
    for i in range(0,3):
        t.forward(200)      
        t.right(90)
        t.right(40)
t.end_fill()
t.left(150)
c=("blue","white","blue","white","blue","white")
t.penup()
t.left(90)
t.forward(200)
t.right(90)
t.pendown()

for i in range(0,8):
    for i in range(0,24):
        if i%6==0:
            t.pencolor(c[0])
        elif i%6==1:
             t.pencolor(c[1]) 
        elif i%6==2:
             t.pencolor(c[2])
        elif i%6==3:
             t.pencolor(c[3])
        elif i%6==4:
             t.pencolor(c[4])
        elif i%6==5:
             t.pencolor(c[5])                   

        for i in range(0,3):
             t. forward(120)
             t.right(90)
             t.right(15)              

    t.penup()      
    t.right(45)    
    t.forward(190)
    t.pendown()

turtle.done()