from object import Vehicles

class Cars(Vehicles):
    def __init__(self,color,model,wheels_num,company):
        super().__init__(color,model,wheels_num)
        self.__company = company

    def getcompany(self):
        return self.__company

    def setcompany(self,company):
        self.__company = company

    def __str__(self):
         return super().__str__()+' '+str(self.__company)
