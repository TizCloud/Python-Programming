# Demo 02-39

myscore = float(input("Enter your score : "))
mymsg = "Your grade is "

if myscore >= 80:
    print(mymsg + "A")
elif myscore >= 70:
    print(mymsg + "B")
elif myscore >= 60:
    print(mymsg + "C")
elif myscore >= 50:
    print(mymsg + "D")
else:
    print(mymsg + "F")

print("End of Program.")
