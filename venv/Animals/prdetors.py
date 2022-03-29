from Animals import Mammals


class predators(Mammals):
    def __init__(self, name, gender, fertile):
        super().__init__(name, gender, fertile)
        # self.kind = kind

    # def voice(self):
    #     print()

    # def setkind(self, kind):
    #     self.kind = kind

    def __str__(self):
        return super().__str__()