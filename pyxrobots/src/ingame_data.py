
from utils import *


keys_up_left = ['q', '7']
keys_up = ['w', '8']
keys_up_right = ['e', '9']
keys_left = ['a', '4']
keys_pass = ['s', '5']
keys_right = ['d', '6']
keys_down_left = ['z', '1']
keys_down = ['x', '2']
keys_down_right = ['c', '3']


class IngameData:
    width: int
    height: int
    player: tuple
    enemies: list
    trash_piles: list

    def __init__(self) -> None:
        self.width = 30
        self.height = 22
        self.player = (0, 0)
        self.enemies = []
        self.trash_piles = []

    def clone(self):
        state = IngameData()
        state.width = self.width
        state.height = self.height
        state.player = self.player
        state.enemies = self.enemies.copy()
        state.trash_piles = self.trash_piles.copy()
        return state

    def is_position_within_bounds(self, pos) -> bool:
        x = pos[0]
        y = pos[1]
        return 0 <= x < self.width and 0 <= y < self.height

    def player_move(self, dx, dy) -> None:
        new_position = (self.player[0] + dx, self.player[1] + dy)
        if self.is_position_within_bounds(new_position):
            self.player = new_position

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
        for index in range(len(self.enemies)):
            self.move_enemy(index)

    def move_enemy(self, index):
        enemy_pos = self.enemies[index]
        dx = self.player[0] - enemy_pos[0]
        dy = self.player[1] - enemy_pos[1]
        self.enemies[index] = (enemy_pos[0] + sign(dx), enemy_pos[1] + sign(dy))

    def move_player_according_to_keypress(self, key: str) -> None:
        if key in keys_up_left:
            self.player_move_up_left()
        elif key in keys_up:
            self.player_move_up()
        if key in keys_up_right:
            self.player_move_up_right()
        elif key in keys_left:
            self.player_move_left()
        elif key in keys_pass:
            self.player_dont_move()
        if key in keys_right:
            self.player_move_right()
        elif key in keys_down_left:
            self.player_move_down_left()
        if key in keys_down:
            self.player_move_down()
        elif key in keys_down_right:
            self.player_move_down_right()
