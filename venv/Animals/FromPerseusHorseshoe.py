from Animals import Mammals

class FromPerseusHorseshoe(Mammals):
    def __init__(self,name,gender,fertile,kind):
        super().__init__(name,gender,fertile)
        self.kind = kind
    def getkind(self):
        return self.kind

    def setkind(self, kind):
        self.kind = kind

    def __str__(self):
        return super().__str__()+" "+self.kind