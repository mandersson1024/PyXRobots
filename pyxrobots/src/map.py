from utils import *


class Map:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.player_position = (0, 0)
        self.enemy_positions = []

    def is_position_within_bounds(self, pos) -> bool:
        x = pos[0]
        y = pos[1]
        return 0 <= x < self.width and 0 <= y < self.height

    def player_move(self, dx, dy) -> None:
        new_position = (self.player_position[0] + dx, self.player_position[1] + dy)
        if self.is_position_within_bounds(new_position):
            self.player_position = new_position

    def player_move_up_left(self) -> None:
        self.player_move(-1, -1)

    def player_move_up(self) -> None:
        self.player_move(0, -1)

    def player_move_up_right(self) -> None:
        self.player_move(1, -1)

    def player_move_left(self) -> None:
        self.player_move(-1, 0)

    def player_dont_move(self) -> None:
        self.player_move(0, 0)

    def player_move_right(self) -> None:
        self.player_move(1, 0)

    def player_move_down_left(self) -> None:
        self.player_move(-1, 1)

    def player_move_down(self) -> None:
        self.player_move(0, 1)

    def player_move_down_right(self) -> None:
        self.player_move(1, 1)

    def move_all_enemies(self) -> None:
        for index in range(len(self.enemy_positions)):
            self.move_enemy(index)

    def move_enemy(self, index):
        enemy_pos = self.enemy_positions[index]
        dx = self.player_position[0] - enemy_pos[0]
        dy = self.player_position[1] - enemy_pos[1]
        self.enemy_positions[index] = (enemy_pos[0] + sign(dx), enemy_pos[1] + sign(dy))

    @property
    def map_string(self) -> str:
        s = ""

        for y in range(0, self.height):
            for x in range(0, self.width):
                if (x, y) == self.player_position:
                    s += '@'
                elif (x, y) in self.enemy_positions:
                    s += 'X'
                else:
                    s += '·'
            s += '\n'

        s = s.strip("\n")
        return s
