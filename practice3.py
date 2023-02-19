# for i in range(1,6):
#     print(i)
    
#     k=1
# while k<=5:
#     print(k)
#     k+=1
    
# for i in range(35,47):
#     print(i)
    
# for j in range(1,11,2):
#     print(j)
    
# for k in range(10,0,-1):
#     print(k)

# i=10
# while i>=1:
#     print (i)
#     i=i-1
    
# for j in range(1,11):
#     print(j*2)
    
# row = int(input("enter the num of rows:"))
# for i in range(1, row+1):
#     print('*'*i)
    
# row= int(input("enter the num of row")) ********************************
# for i in range(1,row+1):
#    for j in range(1,i+1):
#     print('*')
#     print(" *",end=" ")
# print( )

n= int(input("enter number of rows:"))
for i in range(0,n):
    for j in range(i,-1,-1):
       print(j+1,end=" ")
       print( )