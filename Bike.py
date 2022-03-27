from object import Vehicles

class Bike(Vehicles):
    def __init__(self,color,model,wheels_num,type):
        super().__init__(color,model,wheels_num)
        self.__type = type

    def gettype(self):
        return self.__type

    def settype(self,type):
        self.__type = type

    def __str__(self):
         return super().__str__()+' '+str(self.__type)