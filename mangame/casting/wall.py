import constants
from mangame.casting.actor import Actor
from mangame.shared.color import Color
from mangame.shared.point import Point

class Wall(Actor):

    def __init__(self, position):
        super().__init__()
        self._color = constants.BLUE
        self._text = "#"
        self._position = position