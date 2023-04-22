# Demo 02-48

mynum = int(input("Enter integer number(odd) : "))
flag = False
num = 1
for i in range(3, mynum+2, 2):
    if flag == False:
        num = num-1 / i
        flag = True
    else:
        num = num + 1 / i
        flag = False
print ("Result of PI/4 = %.4f" %num)


