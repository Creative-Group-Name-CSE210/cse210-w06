from mangame.casting.food import Food

class Powerup(Food):

    """Get random spots on the screen where walls are NOT
    to put powerups, only display up to 5 per round"""
    """Must be called before points class"""

    def __init__(self):
        self.points = 30
        self.set_text(".")
        self._font_size = 50


