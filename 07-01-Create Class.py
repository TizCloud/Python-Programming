# Demo 07-01
class Car:
    # attributes
    color = "Unknow"
    brand = "Unknow"
    numberofseats = 4
    numberofwheels = 4
    maxSpeed = 0
    regnumber = 0

    def __init__(self, color, brand, numberofseats, numberofwheels, maxSpeed):
        self.color = color
        self.brand = brand
        self.numberofseats = numberofseats
        self.numberofwheels = numberofwheels
        self.maxSpeed = maxSpeed
        self.regnumber += 1

    # methods
    def setColor(self, x):
        self.Color = x

    def setBrand(self, x):
        self.brand = x

    def setNumberOfSeats(self, x):
        self.numberofseats = x

    def setNumberOfWeels(self, x):
        self.numberofwheels = x

    def setMaxSpeed(self, x):
        self.maxSpeed = x

    def printInfo(self):
        print("The color of this car is :", self.color)
        print("The car was brand by :", self.brand)
        print("The number of seats is :", self.numberofseats, "seats.")
        print("The number of wheels is :", self.numberofwheels, "wheels.")
        print("The maximum speed is :", self.maxSpeed, "km/hour")
        print("The registration number is :", self.regnumber)
        print("=============================================================")

# Creating instance and use it
mycar1 = Car('Black','Toyota',4,4,150)
mycar1.printInfo()
mycar1.color = 'Blue'
mycar1.printInfo()

mycar2 = Car('Silver','Honda',4,4,170)
mycar2.printInfo()



