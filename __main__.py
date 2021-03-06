import constants
from mangame.casting.cast import Cast
from mangame.casting.score import Score
from mangame.casting.man import Man
from mangame.casting.ghost import Ghost
from mangame.scripting.script import Script
from mangame.scripting.control_actors import ControlActorsAction
from mangame.scripting.move_actors import MoveActorsAction
from mangame.scripting.handle_collisions import HandleCollisionsAction
from mangame.scripting.draw_actors import DrawActorsAction
from mangame.scripting.construct_maze import ConstructMazeAction
from mangame.scripting.spawn_food import SpawnFoodAction
from mangame.directing.director import Director
from mangame.services.keyboard_service import KeyboardService
from mangame.services.video_service import VideoService
from mangame.casting.lives import Lives
from mangame.scripting.end_game import EndGame
def main():

    cast = Cast()
    cast.add_actor("players", Man())
    cast.add_actor("players", Ghost())
    cast.add_actor('lives', Lives())
    cast.add_actor('score', Score())

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

    food_spawner = SpawnFoodAction()
    food = food_spawner.spawn_food()
    for list in food:
        for item in list:
            cast.add_actor("food", item)

    # cast.add_actor("scores", Score())
    
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction(script))
    script.add_action('update', EndGame())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()