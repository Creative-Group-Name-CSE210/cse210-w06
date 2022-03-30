import constants

from mangame.casting.cast import Cast
# from mangame.casting.score import Score
from mangame.casting.man import Man
from mangame.casting.ghost import Ghost
from mangame.casting.wall import Wall
from mangame.scripting.script import Script
from mangame.scripting.control_actors import ControlActorsAction
from mangame.scripting.move_actors import MoveActorsAction
from mangame.scripting.handle_collisions import HandleCollisionsAction
from mangame.scripting.draw_actors import DrawActorsAction
from mangame.scripting.construct_maze import ConstructMazeAction
from mangame.directing.director import Director
from mangame.services.keyboard_service import KeyboardService
from mangame.services.video_service import VideoService

def main():

    cast = Cast()
    cast.add_actor("players", Man())
    cast.add_actor("players", Ghost())

    maze_constructor = ConstructMazeAction()
    maze = maze_constructor.build_maze()
    # x_counter = 0
    # y_counter = 0
    for list in maze:
        # x_counter += 1
        # y_counter = 0
        for wall in list:
            # y_counter += 1
            cast.add_actor("walls", wall)
    # print(x_counter, "across and", y_counter, "down") # 75 across and 50 down (when interval is 12)

    # cast.add_actor("scores", Score())
    
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()