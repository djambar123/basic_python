class Mammals():
    def __init__(self,name,gender,fertile):
        self.name = name
        self.gender = gender
        self.fertile = fertile

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name

    def getgender(self):
        return self.gender

    def setgender(self, gender):
        self.gender = gender

    def getfertile(self):
        return self.fertile

    def setfertile(self,fertile):
        self.fertile = fertile

    def __str__(self):
        return self.name+' '+str(self.gender)+' '+str(self.fertile)





