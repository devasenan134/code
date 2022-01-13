'''num = input("Enter a number: ")
n = num.split(",")
flag = False
for i in n:
    i = int(i)
    while i>9:
        dig1 = i%10
        i = i//10
        dig2 = i%10
        print(dig1, dig2, str(i))
        if dig1-dig2 == 1 or dig2-dig1 == 1:
            flag = True
    if flag == False:
        break
if flag == True:
    print("The given number is a stepping number")
else:
    print("The given number is not a stepping number")
'''

num = input("Enter a number: ")
n = num.split(",")
flag = False
for i in n:
    while len(i)>=2:
        temp = int(i)
        
        dig1 = temp%10
        temp = temp//10
        dig2 = temp%10
        
        i = i[:-1]
        print(dig1, dig2, i, temp)
        if dig1-dig2 == 1 or dig2-dig1 == 1:
            flag = True
        else:
            flag = False
    if flag == False:
        break
    
if flag == True:
    print("The given number is a stepping number")
else:
    print("The given number is not a stepping number")

