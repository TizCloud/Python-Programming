# Demo 02-44

count = 1
sum = 0.0

print("Exit this program, please type 0 or 0.0 :")

mynum = float(input("Enter a number : "))
while mynum != 0 or mynum != 0.0:
    sum += mynum
    avg = sum / count
    count += 1
    print("Average of number is : ", avg)
    mynum = float(input("Enter a number :"))