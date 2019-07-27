
from utils import *


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

    def overlaps_any_enemy(self, pos: tuple) -> bool:
        for enemy in self.enemies:
            if enemy == pos:
                return True
            else:
                return False

    def check_for_death(self) -> bool:
        return self.overlaps_any_enemy(self.player)

