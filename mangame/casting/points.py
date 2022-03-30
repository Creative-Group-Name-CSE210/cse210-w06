# can we rename this so it's not confused with point.py?

from mangame.casting.food import Food

class Points(Food):
    """Get every place within the maze where there isn't a
    power-up or a wall and place food"""

    def __init__(self):
        self.points = 5
        self.set_text(".")
        self._font_size = 25
    

