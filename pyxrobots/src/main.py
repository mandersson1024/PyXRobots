
from map import *
from ui import *


m = Map(16, 9)
m.player_position = (2, 5)
m.enemy_positions = [(1, 1), (8, 8)]
output = ConsoleOutput()
# output = WindowUI()


def move_player_according_to_keypress(key: str) -> None:
    if key == 'q':
        m.player_move_up_left()
    elif key == 'w':
        m.player_move_up()
    if key == 'e':
        m.player_move_up_right()
    elif key == 'a':
        m.player_move_left()
    elif key == 's':
        m.player_dont_move()
    if key == 'd':
        m.player_move_right()
    elif key == 'z':
        m.player_move_down_left()
    if key == 'x':
        m.player_move_down()
    elif key == 'c':
        m.player_move_down_right()


running = True
while running:
    output.display(m.map_string)
    keypress = wait_for_keypress()
    if keypress == chr(27):  # 27 is ESC
        running = False
    else:
        move_player_according_to_keypress(keypress)
    m.move_all_enemies()


# TODO
# - implement trash piles
# - implement random start positions
# - refactor to implement undo by Command pattern

