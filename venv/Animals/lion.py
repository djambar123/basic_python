from prdetors import predators

class Lion(predators):
    def __init__(self,name, gender, fertile):
        super().__init__(name,gender,fertile)

    def voice(self):
        print('whorrr')

    def __str__(self):
        return super().__str__()



