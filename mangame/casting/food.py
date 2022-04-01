from mangame.casting.actor import Actor
from mangame.casting.wall import Wall
import constants

class Food(Actor):

    """Creates the food that Man will "eat" to gain points"""
    """call the set_text function in points and power-up so 
    display can be different"""
    not_eaten = True 

    def __init__(self, position):
        
        super().__init__()
        self._points = 0
        self._font_size = 15
        self.set_text(".")
        self.set_color(constants.WHITE)
        # self.reset()
        self._position = position
 
    """def reset_food(self):"""

    def get_eaten(self):
        self.set_color(constants.BLACK)
