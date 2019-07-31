
from utils import *
import random


class GameInfo:
    level: int
    score: int
    blinks: int

    def __init__(self):
        self.level = 0
        self.score = 0
        self.blinks = 0

    def level_to_string(self) -> str:
        if self.level <= 0:
            return ' '
        else:
            return str(self.level)


class IngameData:
    width: int
    height: int
    player: tuple
    enemies: list
    trash_piles: list

    def __init__(self) -> None:
        self.width = 30
        self.height = 22
        self.enemies = []
        self.trash_piles = []
        self.player = (-1, -1)
        self.randomly_place_player()
        self.randomly_place_enemies(15)

    def get_random_position(self) -> tuple:
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return x, y

    def player_is_at_position(self, pos: tuple) -> bool:
        if pos == self.player:
            return False

    def any_enemy_is_at_position(self, pos: tuple) -> bool:
        return pos in self.enemies

    def any_trash_pile_is_at_position(self, pos: tuple) -> bool:
        return pos in self.trash_piles

    def position_is_empty(self, pos: tuple) -> bool:
        if self.player_is_at_position(pos):
            return False
        elif self.any_enemy_is_at_position(pos):
            return False
        elif self.any_trash_pile_is_at_position(pos):
            return False
        else:
            return True

    def get_random_empty_position(self) -> tuple:
        pos = self.get_random_position()
        while not self.position_is_empty(pos):
            pos = self.get_random_position()
        return pos

    def randomly_place_player(self) -> None:
        self.player = self.get_random_empty_position()

    def randomly_place_enemies(self, num_enemies: int) -> None:
        for x in range(num_enemies):
            pos = self.get_random_empty_position()
            self.enemies.append(pos)

    def is_position_within_bounds(self, pos) -> bool:
        x = pos[0]
        y = pos[1]
        return 0 <= x < self.width and 0 <= y < self.height

    def player_move(self, dx, dy) -> None:
        new_position = (self.player[0] + dx, self.player[1] + dy)
        if self.is_position_within_bounds(new_position) and self.position_is_empty(new_position):
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

    def blink(self) -> None:
        self.player = self.get_random_empty_position()

    def move_all_enemies(self) -> None:
        for index in range(len(self.enemies)):
            self.move_enemy(index)

    def move_enemy(self, index) -> None:
        enemy_pos = self.enemies[index]
        dx = self.player[0] - enemy_pos[0]
        dy = self.player[1] - enemy_pos[1]
        self.enemies[index] = (enemy_pos[0] + sign(dx), enemy_pos[1] + sign(dy))

    def spawn_trash_piles(self) -> None:
        for enemy in self.enemies:
            count = self.enemies.count(enemy)
            if count >= 2:
                self.spawn_trash_pile_at(enemy)

    def spawn_trash_pile_at(self, pos: tuple) -> None:
        if not (pos in self.trash_piles):
            self.trash_piles.append(pos)

    def kill_enemies(self) -> int:
        num_kills: int = 0
        enemy_positions = list(self.enemies)
        for enemy in enemy_positions:
            if enemy in self.trash_piles:
                self.enemies.remove(enemy)
                num_kills += 1
        return num_kills

    def overlaps_any_enemy(self, pos: tuple) -> bool:
        return pos in self.enemies

    def player_died(self) -> bool:
        return self.overlaps_any_enemy(self.player)

    def level_complete(self) -> bool:
        return len(self.enemies) == 0
