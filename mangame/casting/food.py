from mangame.casting.actor import Actor
from mangame.casting.wall import Wall
from mangame.casting.man import man 
from constants import constants

class Food(Actor):

    """Creates the food that Man will "eat" to gain points"""
    """call the set_text function in points and power-up so 
    display can be different"""
    not_eaten = True 

    def __init__(self):
        
        super().__init__()
        self._points = 0
        self._font_size = 15
        self.set_text()
        self.set_color(constants.WHITE)
        self.reset()

    def display_food(self):
        """fills in the spots that there is no wall with food"""
        
        
    def reset_food(self):
        if not_eaten == True:
            display_food() 

