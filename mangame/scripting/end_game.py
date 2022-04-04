from mangame.scripting.action import Action
from mangame.shared.point import Point
from mangame.casting.actor import Actor
import constants

class EndGame(Action):
    def __init__(self):
        self._is_game_over = False

    def execute(self, cast, script):
        lives = cast.get_first_actor('lives')
        life = lives.get_life()

        if life > 0:
            pass
            print(life)
        elif life == 0:
            self._handle_game_over(cast)
            print('game_over')

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        man = cast.get_first_actor("players")
        ghost = cast.get_second_actor("players")

        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)

        message = Actor()
        message.set_text("Game Over!")
        message.set_position(position)
        cast.add_actor("messages", message)

        man.set_color(constants.WHITE)

        ghost.set_color(constants.WHITE)
