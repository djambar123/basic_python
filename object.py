# class Car:
#     def __init__(self, wheels, model,year,price):
#         self.__model = model
#         self.__yaer = year
#         self.__price = price
#         if wheels < 4:
#             print("imposible")
#             self.__wheels = 4
#         else:
#             self.__wheels = wheels
#     def getwheels(self):
#         return self.__wheels
#
#     def setwheels(self,wheels):
#         if wheels < 4:
#             print("imposible")
#             self.__wheels = 4
#         else:
#             self.__wheels = wheels
#
#     def getmodel(self):
#         return self.__model
#
#     def setmodel(self,model):
#          self.__model = model
#
#     def getyear(self):
#         return self.__yaer
#
#     def setyear(self,year):
#         self.__yaer = year
#
#     def getprice(self):
#         return self.__price
#
#     def setprice(self,price):
#         self.__price = price
#
#     def __str__(self):
#         return str(self.__wheels)+" "+self.__model+""+str(self.__yaer)+" "+str(self.__price)
#
# car1 = Car(4,"gti","2020",41000)
# car2 = Car(3,"bmw","2008",89000)
# car3 = Car(3,"Honda","2017",21000)
#
# print(car1)
# print(car2)
# print(car3)
# print(max(car1.getprice(),car2.getprice(),car3.getprice()))


# class Circle:
#     def __init__(self,color,area=0):
#         self.__color = color
#         self.__area = area
#         self.__radius = 2
#     def getArea(self):
#         self.__area = 3.14**2*self.__radius
#         return self.__area
#
# circl1 = Circle("yellow")
# print(Circle.getArea(circl1))
#
# class Squer:
#     def __init__(self, color, area=0):
#         self.__color = color
#         self.__area = area
#         self.__radius = 3
#
#     def getArea(self):
#         self.__area = 3.14 ** 2 * self.__radius
#         return self.__area
# squer1 = Squer("red")
# print(squer1.getArea())

# class Appartment:
#     def __init__(self,adress,homenum,buyprice,rent):
#         self.__adress = adress
#         self.__homenum = homenum
#         self.__buyprice = buyprice
#         self.__rent = rent
#
#     def yieldd(self):
#         return (self.__rent * 12 / self.__buyprice) * 100
#
# apprt = Appartment("hadera",13,1000000,4000)
#
# print(apprt.yieldd())
#
# class Cat:
#     def __init__(self,name,age,colorOfhair):
#         self.__name = name
#         self.__age = age
#         self.__colorOfhair = colorOfhair
#
#     def getname(self):
#         return self.__name
#
#     def setname(self,name):
#         self.__name = name
#
#     def getage(self):
#         return self.__age
#
#     def setage(self,age):
#         self.__age = age
#
#     def getcolor(self):
#         self.__colorOfhair
#
#     def setcolor(self,colorOfhair):
#         self.__colorOfhair = colorOfhair
#
#     def sound(self):
#         sound = 'miyou'
#         return sound
#
#     def mustech(self):
#         mus = 'yes'
#         return mus
#
#     def __str__(self):
#         return self.__name+' '+str(self.__age)+' '+self.__colorOfhair
#
# class Dog:
#     def __init__(self, name, age, colorOfhair):
#                 self.__name = name
#                 self.__age = age
#                 self.__colorOfhair = colorOfhair
#
#     def getname(self):
#         return self.__name
#
#     def setname(self, name):
#         self.__name = name
#
#     def getage(self):
#         return self.__age
#
#     def setage(self, age):
#         self.__age = age
#
#     def getcolor(self):
#         self.__colorOfhair
#
#     def setcolor(self, colorOfhair):
#         self.__colorOfhair = colorOfhair
#
#     def sound(self):
#         sound = 'hwoo hwoo'
#         return sound
#
#     def mustech(self):
#         mus = 'yes'
#         return mus
#
#     def __str__(self):
#         return self.__name+' '+str(self.__age)+' '+self.__colorOfhair
#
#
# cat1 = Cat('aviav',12,'red')
# cat2 = Cat("betty",10,'black')
# dog1 = Dog('sali',8,'yellow')
# dog2 = Dog('daniel',21,'black')
#
# cat1.city = 'hadera'
#
# del cat1.city

class Cars:
    def __init__(self,model,color,price):
        self.__model = model
        self.__color = color
        self.__price = price

    def getmodel(self):
        return self.__model

    def setmodel(self, model):
        self.__model = model

    def getcolor(self):
        return self.__color

    def setcolor(self, color):
        self.__color = color

    def getprice(self):
        return self.__price

    def setprice(self, price):
        self.__price = price

    def __str__(self):
        return self.__model+' '+str(self.__color)+' '+str(self.__price)

car1 = Cars("SUV","black",47000)
car2 = Cars("BMW","white",69000)
car3 = Cars("Honda","Yellow",37000)
car4 = Cars("Mersedes","rad",80000)

pric = [car1,car2,car3,car4]

def maxPrice():
    max = 0
    for i in range(len(pric)-1):
        if pric[i].getprice() > pric[i+1].getprice():
            max = pric[i]
    return max

print(Cars.__str__(maxPrice()))







