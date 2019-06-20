
from map import *
from ui import *


m = Map(16, 9)
m.player_position = (2, 5)
m.enemy_positions = [(1, 1), (8, 8)]
m.trash_piles = [(1, 3)]
output = ConsoleOutput()
# output = WindowUI()

keys_up_left = ['q', '7']
keys_up = ['w', '8']
keys_up_right = ['e', '9']
keys_left = ['a', '4']
keys_pass = ['s', '5']
keys_right = ['d', '6']
keys_down_left = ['z', '1']
keys_down = ['x', '2']
keys_down_right = ['c', '3']


def move_player_according_to_keypress(key: str) -> None:
    if key in keys_up_left:
        m.player_move_up_left()
    elif key in keys_up:
        m.player_move_up()
    if key in keys_up_right:
        m.player_move_up_right()
    elif key in keys_left:
        m.player_move_left()
    elif key in keys_pass:
        m.player_dont_move()
    if key in keys_right:
        m.player_move_right()
    elif key in keys_down_left:
        m.player_move_down_left()
    if key in keys_down:
        m.player_move_down()
    elif key in keys_down_right:
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
# - implement undo
#   - test undo by unit testing
# - attempting blocked movement should not trigger enemy movement
# - implement trash piles
#   - trash pile block enemy movement
#   - trash pile kill enemy
#   - enemy-enemy collision creates trash pile
# - implement random start positions
# - implement levels, main menu, instructions

