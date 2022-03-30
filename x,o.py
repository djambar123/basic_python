class bord:
    def __init__(self):
        self.bord = [' '] * 9

    def to_string(self):
        return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n'.format(*self.bord)
# class player:
#     pass
# class game:
