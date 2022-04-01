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
        self._direction1 = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)
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
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction1 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction1 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction1 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction1 = Point(0, constants.CELL_SIZE)
        
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)
        
        if self._stop_man:
            self._direction1 = Point(0, 0)
            self._stop_man = False
        
        if self._stop_ghost:
            self._direction2 = Point(0, 0)
            self._stop_man = False


        man = cast.get_first_actor("players")
        ghost = cast.get_second_actor("players")

        man.turn_head(self._direction1)
        ghost.turn_head(self._direction2)