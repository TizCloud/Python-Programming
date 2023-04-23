# Demo 07-04
class ClassicCar:
    regnumber = 0
    color = 'white'

    def __init__(self):
        ClassicCar.regnumber += 1
        print("ClassicCar: Constructor")

    def ClassicCarGetReg(self):
        print("ClassicCar: Register number is ",self.regnumber)

    def ClassicCarSetColor(self, color):
        self.color = color
        print("ClassicCar: Set color")

    def ClassicCarGetColor(self):
        print("ClassicCar: Get color is ", ClassicCar.color)

    def __del__(self):
        class_name = self.__class__.__name__
        print("ClassicCar: ", class_name, "object has destroyed")

class ToyotaCar(ClassicCar):
    def __init__(self):
        self.color = 'gold blond'
        print("Toyota Car: Constructor")

    def ToyotaCarGetColor(self):
        print('Toyota Car: Get color is ', self.color)

class HondaCar(ClassicCar):
    def __init__(self):
        self.color = 'black'

    def HondaCarGetColor(self):
        print('Honda Car: Get color is ', self.color)

mycar1 = ToyotaCar()
mycar1.ClassicCarGetReg()
mycar1.ClassicCarGetColor()
mycar1.ClassicCarSetColor('green')
mycar1.ClassicCarGetColor()
mycar1.ToyotaCarGetColor()

print("----------------------------------")

mycar2 = HondaCar()
mycar2.ClassicCarGetReg()
mycar2.ClassicCarGetColor()
mycar2.ClassicCarSetColor('yello')
mycar2.ClassicCarGetColor()
mycar2.HondaCarGetColor()

print("----------------------------------")

del mycar1
del mycar2

