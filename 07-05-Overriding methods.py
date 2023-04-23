#Demo 07-05
class ClassicCar:
    def brake(self):
        print("ClassicCar: Normal brake!")

class ToyotaCar(ClassicCar):
    def brake(self):
        print("ToyotaCar: Disk brake pad!")

class HondaCar(ClassicCar):
    def brake(self):
        print ("HondaCar: Drum brake pad!")

mycar1 = ToyotaCar()
mycar1.brake()

mycar2 = HondaCar()
mycar2.brake()

