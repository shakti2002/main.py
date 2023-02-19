# import turtle

# t=turtle.Turtle()
# s=turtle.Screen()
# s.bgcolor("black")
# t.speed(10)
# t.color("blue","yellow")
# t.begin_fill()
# for i in range(0,24):
#     for i in range(0,4):
#         t.forward(100)
#         t.right(90)
#         t.right(15)
# t.end_fill()
# turtle.done()
    
# import turtle

# t=turtle.Turtle()
# s=turtle.Screen()
# s.bgcolor("black")
# t.speed(10)
# t.color("blue","yellow")
# t.begin_fill()
# for i in range(0,24):
#     t.circle(100)
#     t.right(15)
# t.end_fill()
# turtle.done()
    
# import turtle

# t=turtle.Turtle()
# s=turtle.Screen()
# s.bgcolor("black")
# t.speed(10)
# colors=("red","yellow","green","orange","white","blue","pink")
# for i in range(1,25):
#     if i%7==0:
#         t.pencolor(colors[5])
#     elif i%7==1:
#         t.pencolor(colors[0])
#     elif i%7==2:
#         t.pencolor(colors[1])
#     elif i%7==3:
#         t.pencolor(colors[2])
#     elif i%7==4:
#         t.pencolor(colors[3])
#     elif i%7==5:
#         t.pencolor(colors[4])
#     elif i%7==5:
#         t.pencolor(colors[5])
       
#     t.circle(100)    
#     t.right(15)
# turtle.done()
    

import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pen(100)
t.speed(12)

t.color("blue","orange")
t.begin_fill()
for i in range(0,12):
    for i in range(0,3):
        t.forward(200)      
        t.right(90)
        t.right(40)
t.end_fill()
t.left(150)

t.color("blue","yellow")
t.begin_fill()
for i in range(0,12):
    for i in range(0,3):
        t.forward(200)
        t.right(90)
        
        t.right(40)
t.end_fill()
turtle.done()


