from object import Vehicles

class Airplane(Vehicles):
    def __init__(self,color,model,wheels_num,manufacturerAt):
        super().__init__(color,model,wheels_num)
        self.__manufacturerAt = manufacturerAt

    def getmanufacturerAt(self):
        return self.__manufacturerAt

    def setmanufacturerAt(self,manufacturerAt):
        self.__manufacturerAt = manufacturerAt

    def __str__(self):
         return super().__str__()+' '+str(self.__manufacturerAt)