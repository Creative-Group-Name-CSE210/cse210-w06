import constants
from mangame.casting.actor import Actor
from mangame.shared.color import Color
from mangame.shared.point import Point

class Wall(Actor):

    def __init__(self):
        super().__init__()
        self._color = constants.BLUE
        self._text = "#"