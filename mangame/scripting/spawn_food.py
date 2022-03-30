import constants
import csv

from mangame.casting.food import Food
from mangame.shared.point import Point

class SpawnFoodAction():
    def __init__(self):
        self.width = constants.MAX_X # 900
        self.height = constants.MAX_Y # 600
        self.interval = 12
        self.maze_list = [] # [0,0] is in the top left

    def spawn_food(self):
        for y in range(0, self.height, self.interval):
            list_of_food = []
            for x in range(0, self.width, self.interval):
                food = Food(Point(x, y))
                list_of_food.append(food)
            self.maze_list.append(list_of_food)
        self.cut_out_maze()
        return self.maze_list
    
    def parse_csv(self):
        map = open("byui_python_map.csv")
        csv_map = csv.reader(map)
        list_of_lists = []
        for row in csv_map:
            list_of_chars = []
            for char in row:
                list_of_chars.append(char)
            list_of_lists.append(list_of_chars)
        return list_of_lists

    def cut_out_maze(self):
        parsed_csv = self.parse_csv()
        len_parsed_csv = len(parsed_csv)
        len_csv_line = len(parsed_csv[0])
        items_to_delete = []
        for x in range(0, len_csv_line):
            for y in range(0, len_parsed_csv):
                if parsed_csv[y][x] != "o":
                    items_to_delete.append([y,x])
        for item in reversed(items_to_delete):
            y = item[0]
            x = item[1]
            self.maze_list[y].pop(x)