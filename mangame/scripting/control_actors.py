import constants
from mangame.scripting.action import Action
from mangame.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.
    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction1 = Point(0, 0)
        self._direction2 = Point(0, 0)
        self._stop_man = False
        self._stop_ghost = False
    
    def stop_man(self, boolean):
        self._stop_man = boolean
    
    def stop_ghost(self, boolean):
        self._stop_ghost = boolean

    def execute(self, cast, script):
        """Executes the control actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        man = cast.get_first_actor("players")
        ghost = cast.get_second_actor("players")

        direction1_deets = [self._direction1.get_x(), self._direction1.get_y()]
        direction2_deets = [self._direction2.get_x(), self._direction2.get_y()]
        man_pos = man.get_position()
        ghost_pos = ghost.get_position()
        man_coords = [man_pos.get_x(), man_pos.get_y()]
        ghost_coords = [ghost_pos.get_x(), ghost_pos.get_y()]

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction1 = Point(-constants.CELL_SIZE, 0)
            # man.take_step(Point(-constants.CELL_SIZE, 0))
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction1 = Point(constants.CELL_SIZE, 0)
            # man.take_step(Point(constants.CELL_SIZE, 0))
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction1 = Point(0, -constants.CELL_SIZE)
            # man.take_step(Point(0, -constants.CELL_SIZE))
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction1 = Point(0, constants.CELL_SIZE)
            # man.take_step(Point(0, constants.CELL_SIZE))
        
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
            # ghost.take_step(Point(-constants.CELL_SIZE, 0))
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
            # ghost.take_step(Point(constants.CELL_SIZE, 0))
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
            # ghost.take_step(Point(0, -constants.CELL_SIZE))
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)
            # ghost.take_step(Point(0, constants.CELL_SIZE))
        
        

        if self._stop_man:
            self._direction1 = Point(0, 0)
            if direction1_deets[0] != 0:
                man.set_position(Point(man_coords[0] - direction1_deets[0], man_coords[1]))
            elif direction1_deets[1] != 0:
                man.set_position(Point(man_coords[0], man_coords[1] - direction1_deets[1]))
            self._stop_man = False
        
        if self._stop_ghost:
            self._direction2 = Point(0, 0)
            if direction2_deets[0] != 0:
                ghost.set_position(Point(ghost_coords[0] - direction2_deets[0], ghost_coords[1]))
            elif direction2_deets[1] != 0:
                ghost.set_position(Point(ghost_coords[0], ghost_coords[1] - direction2_deets[1]))
            self._stop_ghost = False


        man.turn_head(self._direction1)
        ghost.turn_head(self._direction2)