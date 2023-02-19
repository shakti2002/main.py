'''file=open("a.txt",'r')
print(file.read())
file.close()

file=open("a.txt",'w')
print(file.read().splitlines())
print(file.readlines())
file.write("I am in new line")
file.writelines(["hello\n","hii"])
file.close()

file= open("a.txt",'a')
file.write("new line")
file.close()'''


# try:
#     x=int(input("enter a num "))
#     print("num is:",x)
# except ValueError:
#     print("please input int valuee only")

# try:
#     x=int(input("enter a num "))
#     # print("num is:",x)
#     print("DIV is:",x/0)
# except ValueError:
    # print("please input int valuee only")
    # pehle uper wale ko bss peint krne firr baad me poore ko
# except ZeroDivisionError:
#     print("cannot be divided by zero")  

'''try:
    x=int(input("enter a num "))
    print("DIV is:",x/0)
except:
    print("error occurred")'''

'''try:
    x=int(input("enter a num "))
    print("num is:",x)
    print("me to chalunga")
except ValueError:
    print("error occurred")
    print("me to chalunga")
'''
'''try:
    x=int(input("enter a num "))
    print("num is:",x)
except ValueError:
    print("me to chalunga")'''

# kam- try me bhi or except me bhi chale

# try: 
#     x= int(input("enter a num:"))
#     print("DIV is:", x/0)
#     print("valueerror, zerodivisionerror")
# except (ValueError, ZeroDivisionError):
#     print("error occurred")
# finally:
#     print("me to chaalunga")

# raise ValueError

# raise hii
#  assert 2==2
# assert 2==4, "barbar nhi hai"