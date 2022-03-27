from prdetors import predators

class lion(predators):
    def __init__(self,name, gender, fertile):
        super().__init__(name,gender,fertile,kind ='predators')

    def __str__(self):
        return super().__str__()



