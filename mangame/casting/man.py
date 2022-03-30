import constants
from mangame.casting.actor import Actor
from mangame.shared.point import Point

class Man(Actor):
    def __init__(self):
        super().__init__()
        self._can_eat_ghost = False

        self.set_text('c')
        self.set_color(constants.YELLOW)
        self.set_position(Point(250, 300))
        self.set_velocity(Point(0,0))

    def turn_head(self, velocity):
        self.set_velocity(velocity)

    def eat_ghost(self, boolean):
        self._can_eat_ghost = boolean

    def stop_move(self):
        self.set_velocity(Point(0,0))
    
    def start_move(self, velocity):
        self.set_velocity(velocity)

    
