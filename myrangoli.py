import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pen(50)
t.speed(0)
c=("red","yellow","green","orange","blue","grey")

for i in range(0,8):
    for i in range(1,25):
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
             t.circle(50)
             t.right(15)              

    t.penup()      
    t.right(45)    
    t.forward(100)
    t.pendown()

turtle.done()
