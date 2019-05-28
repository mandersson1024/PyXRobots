
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
    if keypress == ' ':
        running = False
    else:
        m.execute_player_action(keypress)


