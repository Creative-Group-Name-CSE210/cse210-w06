from mangame.shared.point import Point
from mangame.scripting.action import Action

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            """self._handle_food_collision(cast)"""
            self._handle_trail_collision(cast)
            #self._handle_segment_collision(cast)
            #self._handle_game_over(cast)

    def _handle_trail_collision(self, cast):
        """Updates the score and moves the food if the man collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

    def _handle_wall_collision(self, cast):
        walls = cast.get_actors('walls')
        man = cast.get_first_actor('players')
        ghost = cast.get_second_actor('players')

        for wall in walls:
            if man.get_position() == wall.get_position():
                man.set_velocity(Point(0,0))

            if ghost.get_position() == wall.get_position():
                man.set_velocity(Point(0,0))
      
    