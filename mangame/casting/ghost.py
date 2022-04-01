import constants
from mangame.casting.actor import Actor
from mangame.shared.point import Point


class Ghost(Actor):
    def __init__(self):
        super().__init__()
        self._can_eat_man = True

        self.set_text('g')
        self.set_color(constants.RED)
        self.set_position(Point(650, 300))
        self.set_velocity(Point(0,0))

    def turn_head(self, velocity):
        self.set_velocity(velocity)

    def can_eat_man(self, boolean):
        self._can_eat_man = boolean

    def stop_move(self):
        self.set_velocity(Point(0,0))
    
    def start_move(self, velocity):
        self.set_velocity(velocity)
    
    def take_step(self, velocity):
        velocity_coords = [velocity.get_x(), velocity.get_y()]
        self._position = Point(self._position.get_x() + velocity_coords[0], self._position.get_y() + velocity_coords[1])