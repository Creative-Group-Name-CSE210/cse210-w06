from mangame.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        man = cast.get_first_actor("players")
        ghost = cast.get_second_actor("players")
        walls = cast.get_actors("walls")
        food = cast.get_actors("food")
        messages = cast.get_actors("messages")
        lives = cast.get_first_actor('lives')

        self._video_service.clear_buffer()
        self._video_service.draw_actor(man)
        self._video_service.draw_actor(ghost)
        # self._video_service.draw_actor(score) # uncomment this after score is finished
        self._video_service.draw_actors(walls, True)
        self._video_service.draw_actors(food, True)
        self._video_service.draw_actor(lives)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()