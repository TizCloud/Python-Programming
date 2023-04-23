# Demo 07-03
class Car:
    def __init__(self, color='red', speed=100):
        self.color = color
        self.speed = speed

    # Destructor method
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "object has destroyed")

mycar1 = Car()
mycar2 = mycar1
mycar3 = mycar1

print ("ID[mycar1]=",id(mycar1),", ID[mycar2]=",id(mycar2),", ID[mycar3]=",id(mycar3))

del mycar1
del mycar2
del mycar3

