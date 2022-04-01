from mangame.shared.point import Point
from mangame.scripting.action import Action
from mangame.scripting.control_actors import ControlActorsAction
import math

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, script):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.script = script

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_wall_collision(cast, self.script)
            #self._handle_segment_collision(cast)
            #self._handle_game_over(cast)
            self._handle_player_collision(cast)

    def calculate_distance(self, x1, y1, x2, y2):
        x_distance = abs(x1 - x2)
        y_distance = abs(y1 - y2)
        distance = math.sqrt((x_distance * x_distance) + (y_distance * y_distance))
        return distance

    def _handle_food_collision(self, cast):
        foods = cast.get_actors("food")
        man = cast.get_first_actor('players')

        for food in foods:
            man_pos = man.get_position()
            food_pos = food.get_position()
            man_coords = [man_pos.get_x(), man_pos.get_y()]
            food_coord = [food_pos.get_x(), food_pos.get_y()]

            man_food_distance = self.calculate_distance(man_coords[0], man_coords[1], food_coord[0], food_coord[1])

            if man_food_distance < 8:
                food.get_eaten()
                print("man has eaten")


    def _handle_wall_collision(self, cast, script):
        walls = cast.get_actors('walls')
        man = cast.get_first_actor('players')
        ghost = cast.get_second_actor('players')

        for wall in walls:
            """
            Collision can be handled by only turning players once they're in line with the grid, or
            have the actors based off of the same grid as the maze and check collision based off of
            the grid, or get the distance between the two positions and if it's less than x have them
            collide.
            Below doesn't work yet because the player position and wall position are never equal.
            """
            man_pos = man.get_position()
            ghost_pos = ghost.get_position()
            wall_pos = wall.get_position()
            man_coords = [man_pos.get_x(), man_pos.get_y()]
            ghost_coords = [ghost_pos.get_x(), ghost_pos.get_y()]
            wall_coord = [wall_pos.get_x(), wall_pos.get_y()]

            man_wall_distance = self.calculate_distance(man_coords[0], man_coords[1], wall_coord[0], wall_coord[1])
            ghost_wall_distance = self.calculate_distance(ghost_coords[0], ghost_coords[1], wall_coord[0], wall_coord[1])

            # this doesn't work because control_actors.py is constantly updating the velocity
            if man_wall_distance < 8:
                actions = script.get_actions("input")
                for action in actions:
                    action.stop_man(True)
                
                print("man has collided")

            if ghost_wall_distance < 8:
                ghost.set_velocity(Point(0,0))
                print("ghost has collided")

    def _handle_player_collision(self, cast):   
        man = cast.get_first_actor('players')
        ghost = cast.get_second_actor('players')
        lives = cast.get_first_actor('lives')

        man_pos = man.get_position()
        ghost_pos = ghost.get_position()
        man_coords = [man_pos.get_x(), man_pos.get_y()]
        ghost_coords = [ghost_pos.get_x(), ghost_pos.get_y()]
        man_ghost_distance = self.calculate_distance(man_coords[0], man_coords[1], ghost_coords[0], ghost_coords[1])

        if man_ghost_distance <= 5:
            if ghost._can_eat_man == True:
                if lives._lives > 0:
                    lives.lose_life()
                    man.set_position(Point(250, 300))
                    ghost.set_position(Point(650, 300))

            elif man._can_eat_ghost == True:
                ghost.set_position(Point(650,300))


    