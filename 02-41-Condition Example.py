# Demo 02-41

mynum1 = float(input("Enter first number : "))
mynum2 = float(input("Enter second number : "))
mynum3 = float(input("Enter third number : "))

if mynum1 < mynum2:
    if mynum1 < mynum3:
        minnum = mynum1
    else:
        minnum = mynum3
elif mynum2 < mynum3:
    minnum = mynum2
else:
    minnum = mynum3

print("Minimum Number is : ",minnum)