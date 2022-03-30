import constants
from mangame.casting.actor import Actor
from mangame.shared.point import Point


class Ghost(Actor):
    def __init__(self):
        super().__init__()
        self._can_eat_man = True

        self.set_text('c')
        self.set_color(constants.YELLOW)
        self.set_position(Point(400, 200))
        self.set_velocity(Point(0,0))

    def turn_head(self, velocity):
        self._text.set_velocity(velocity)

    def can_eat_man(self, boolean):
        self._can_eat_man = boolean

    def stop_move(self):
        self.set_velocity(Point(0,0))
    
    def start_move(self, velocity):
        self.set_velocity(velocity)