

class Player():
    def __init__(self, white):
        self.white = white


class Human(Player):
    def __init__(self, white):
        super().__init__(white)


class Ia(Player):
    def __init__(self, white):
        super().__init__(white)
