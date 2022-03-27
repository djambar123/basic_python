from object import Vehicles

class Train(Vehicles):
    def __init__(self, color, model, wheels_num, carts_num):
        super().__init__(color, model, wheels_num)
        self.__carts_num = carts_num

    def getcarts_num(self):
        return self.__carts_num

    def setmanufacturerAt(self,carts_num):
        self.__carts_num = carts_num

    def __str__(self):
         return super().__str__()+' '+str(self.__carts_num)