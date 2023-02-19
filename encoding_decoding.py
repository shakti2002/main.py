'''startsmall=97
startBig = 65
temp = " "
alphalist =[]
for i in range(1,53):
    if startsmall >=97 and startsmall<= 122:
        temp = chr(startsmall)+":00"+ str(i)+"\n"
        startsmall+=1
    else:
        temp =chr(startBig)+":00"+str(i)+"\n"
        startBig+=1
        alphalist.append(temp)
file=open("hash.txt",'w')
file.writelines(alphalist)
file.close()'''

# NOW WE MAKE AN ENCRYPITER

'''orig= input("enter your password:")
print("you entered:",orig)
alphaDict ={}
file = open("hash.txt",'r')
for i in file.read().splitlines():
    temp= i.split(":")
    alphaDict[temp[0]]=temp[1]
    newPass = ""
for i in orig:
    newPass+= alphaDict[i]+ "_"
print("encode pass :",newPass)'''



'''startsmall=97
startBig = 65
temp = ""
alphalist =[]
for i in range(1,53):
    if  startBig>=65 and startsmall<= 90:
        temp ="00"+str(i)+ chr(startsmall)+"\n"
        startsmall+=1
    
    else:
        startBig>=65 and startsmall<= 90
        temp ="00"+str(i)+ chr(startBig)+"\n"
        startBig+=1
        alphalist.append(temp)
file=open("hash1.txt",'w')
file.writelines(alphalist)
file.close()'''

orig= input("enter your password number: ")
print("you entered:",orig)
numDict ={}
file= open("hash1.txt",'r')
for i in file.read().splitlines():
    temp= i.split(":")
    numDict[temp[0]]=temp[1]
newpass=""
for i in orig:
    newpass+= numDict[i]
print("decoded pass:",newpass)