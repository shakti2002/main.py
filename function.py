
# def printer():
#     print("printer running")
#     print("printer over")

# printer()

'''def sum(x,y):
     print(x+y)
 sum(2,5)'''
'''def sum(x,y):
    z=x+y
    print(z)
sum(2,5)'''
# x=5
# def sum(x,y):
#     print(x+y)
#     return x+y
# z= sum(2,5)
# def add(x,y):
#     return x+y
# z= add(2,4)
# print(z)

'''def changer (x,y): #isme global x define nhi ho pa raaha***********
    x=10
    y=5
    print("Infunction", x,y)
x=5
y=10
print("before function", x,y)
changer(x,y)
print("after function",x,y)'''


# RECURSION'''

'''def fac(x):
    if x==0:
        return 1
    else:
        return x*fac(x-1)
z=int(input("enter a num"))
print(fac(z))'''


# LAMBDA FUNCTION

'''sum= lambda a,b: a+b
print(sum(2,3))'''


'''ARGUMENTS'''
# variable arguments

# def add(*arg):
#     sum=0
#     for value in arg:
#         sum+=value
#     return sum
# print(add(2,3))
# print(add(2,3,5))
# print(add(8,9,7,6))

# KWARGS ARGUMENTS

'''def add(**kwargs):
    sum=0
    for key,value in kwargs.items():
        sum+=value
        print(key)
    return sum
print(add( num1=3 , num2=6))'''

'''postion arguments'''

# def printer(x,y):
#     print(x)
#     print(y.lower())
# print(2 ,"HELLO")

# DEFAULT ARGUMENT
'''def add(first, sec, third=5):
    print(first+sec+third)
add(2,3,4)
add(2,3)'''
# def add(x,y=5,z=6):
#     print(x+y+z)
# add(3)

# NAME ARGUMENTS
'''def add(x,y):
    print(x+y)
add(y=5,x=2)'''

'''COMMAND ARGUMENT'''
# import sys
# if "activate" in sys.argv:
#     print("cheats activated")
# else:
#     print("cheats not activated")

