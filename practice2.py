# username= "shakti_110"
# passwd= "shakti@123"

# username_input= input("enter your username:")
# passwd_input= input("enter your password:")

# if username == username_input and passwd== passwd_input:
#     print("login successfull")
# else:
#     if username != username_input:
#         print("username and passwd incorrect")


# MINICALCULATOR


print("\t\t\t\t\nWELCOME TO CALCULATOR \n")
num1 =int(input("enter first num:"))
num2 =int(input("enter second num:"))

print("\n choose the option \n1. +\n2. -\n3. *\n4. /\n")
choice = input("enter your choice:")

if  choice== '+':
    print(f"the addition of {num1} and {num2} is:", num1+num2)
elif choice== '-':
    print(f"the subtraction of {num1} and {num2} is:", num1-num2)

elif choice== '*':
    print(f"the multiplication of {num1} and {num2} is:", num1*num2)
    
elif choice== '/':
    print(f"the division of {num1} and {num2} is:", num1/num2)
else:
    print("this choice is not available")
    print("thankyou")


# x= int(input("enter a num:"))
# if x>5:
#     print("x is greater")
# else:
#     print("x is smaller")

# x= int (input("enter a num \n"))
# if x>=5 and x<=10:
#     print("x is in the range")
# else:
#     print("x is not in the range")



# amt =0
# units= int(input("Enter the number of electric units consumed \n"))

# if units <=100:
#     amt=0
# if 100< units <=200:
#     amt= (units-100)*5
# if units> 200:
#     amt= 500 + (units-200)*10
# print("total electricity bill is", amt)


# year = int(input("Enter a year"))
# if year % 100 ==0:
#     if year % 400 ==0:
#         print("this year is a leap year.")
#     else:
#         print("the year is not a leap year")
# else:
#     if year % 4 ==0:
#         print("the year is a leap year.")
#     else:
#         print("the year is not a leap year")


# tax =0
# cp = int(input("enter the price of  the vehicle"))
# if cp > 100000:
#    tax = 15/100*cp
# elif 50000<cp<100000:
#     tax = 10/100*cp
# else:
#     tax = 5/100*cp
# print("the road tax is:", tax)       