from mangame.casting.actor import Actor

class Lives(Actor):
    def __init__(self):
        super().__init__()
        self._lives = 3
        self.set_text(f'lives: {self.get_life()}')

    def get_life(self):
        return self._lives

    def set_life(self, number):
        self._lives = number
        self.set_text(f'lives: {self.get_life()}')