from FromPerseusHorseshoe import FromPerseusHorseshoe


class Horse(FromPerseusHorseshoe):
    def __init__(self, name, gender, fertile):
        super().__init__(name, gender, fertile, kind='From Perseus Horse shoe')

    def __str__(self):
        return super().__str__()