from mangame.casting.actor import Actor

class Lives(Actor):
    def __init__(self):
        super().__init__()
        self._lives = 3
        self.set_text(f'Lives: {self._lives}')

    def lose_life(self):
        if self._lives > 0:
            self._lives -= 1

    def get_life(self):
        return self._lives