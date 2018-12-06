class Car:
    wheelNum = 2
    __color = 'red'

    @classmethod
    def showName(cls):
        print('my name is lwx')

    def __init__(self, num, color):
        self.wheelNum = num
        self.__color = color

    def showNum(self):
        print(self.wheelNum)

    def getCarInfo(self, age):
        print('color is ',self.__color, 'the age is',age)

print(Car.wheelNum)
BMW = Car(1, 'yellow')
print(Car.wheelNum)
BMW.getCarInfo(4)
print(Car.wheelNum)

BENZ = Car(2, 'orange')
BENZ.getCarInfo(3)

class Bike(Car):
    def __init__(self):
        super().__init__(44, 'black')

    def showSpeed():
        print('the speed is 40km/h')
    
    def getCarInfo(self):
        super().getCarInfo(12)
        print('the color is e')
bike = Bike()
bike.getCarInfo()


BMW.showNum()
print(Car.wheelNum)
del BMW.wheelNum
Car.wheelNum = 5
BMW.showNum()
print(Car.wheelNum)
BMW.wheelNum = 6
BMW.showNum()
print(Car.wheelNum)
