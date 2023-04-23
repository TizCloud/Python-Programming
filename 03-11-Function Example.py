# Demo 03-11
def menu():
    print("Welcome to Calculator Program")
    print("Your options are :")
    print("****************************")
    print("1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Division")
    print("5-Exit Program")
    print("****************************")
    return int(input("Choose your option : "))

def add(mynum1, mynum2):
    print("You chose the Addition")
    print("Result of ", mynum1, "+", mynum2, "=", mynum1 + mynum2)
    return mynum1 + mynum2

def sub(mynum1, mynum2):
    print("You chose the Subtraction")
    print("Result of ", mynum1, "-", mynum2, "=", mynum1 - mynum2)
    return mynum1 - mynum2

def mul(mynum1, mynum2):
    print("You chose the Multiplication")
    print("Result of ", mynum1, "*", mynum2, "=", mynum1 * mynum2)
    return mynum1 * mynum2

def div(mynum1, mynum2):
    print("You chose the Division")
    if mynum2 != 0:
        print("Result of ", mynum1, "/", mynum2, "=", mynum1 / mynum2)
        return mynum1 / mynum2
    else:
        print("Can't divide by zero !!!")
        return False

def main():
    loop = 1
    choice = 0
    while loop == 1:
        choice = menu()
        if choice == 1:
            add(int(input("Number 1 : ")), int(input("Number 2 : ")))
        elif choice == 2:
            sub(int(input("Number 1 : ")), int(input("Number 2 : ")))
        elif choice == 3:
            mul(int(input("Number 1 : ")), int(input("Number 2 : ")))
        elif choice == 4:
            div(int(input("Number 1 : ")), int(input("Number 2 : ")))
        elif choice == 5:
            loop = 0
    else:
        print("The End of Program.")

if __name__ == "__main__":
    main()

