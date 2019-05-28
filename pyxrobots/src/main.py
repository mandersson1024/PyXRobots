
from map import *
from ui import *


m = Map(16, 9)
m.player_position = (2, 5)
output = ConsoleOutput()
# output = WindowUI()


running = True
while running:
    output.display(m.map_string)
    keypress = wait_for_keypress()
    if keypress == chr(27):  # 27 is ESC
        running = False
    elif keypress == 'q':
        m.player_move_up_left()
    elif keypress == 'w':
        m.player_move_up()
    if keypress == 'e':
        m.player_move_up_right()
    elif keypress == 'a':
        m.player_move_left()
    elif keypress == 's':
        m.player_dont_move()
    if keypress == 'd':
        m.player_move_right()
    elif keypress == 'z':
        m.player_move_down_left()
    if keypress == 'x':
        m.player_move_down()
    elif keypress == 'c':
        m.player_move_down_right()


# TODO
# - implement undo

