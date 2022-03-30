import constants

from mangame.casting.cast import Cast
# from mangame.casting.score import Score
from mangame.casting.man import Man
from mangame.casting.ghost import Ghost
from mangame.scripting.script import Script
from mangame.scripting.control_actors import ControlActorsAction
from mangame.scripting.move_actors import MoveActorsAction
from mangame.scripting.handle_collisions import HandleCollisionsAction
from mangame.scripting.draw_actors import DrawActorsAction
from mangame.directing.director import Director
from mangame.services.keyboard_service import KeyboardService
from mangame.services.video_service import VideoService

def main():

    cast = Cast()
    cast.add_actor("players", Man())
    cast.add_actor("players", Ghost())
    # cast.add_actor("scores", Score())

    # Start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())



if __name__ == "__main__":
    main()