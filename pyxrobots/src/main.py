
from map import *
from ui import *


m = Map(16, 9)
m.player_position = (5, 5)
output = ConsoleOutput()
# output = WindowUI()


output.display(m.map_string)

keypress = wait_for_keypress()

player_action = input_mapper.get_action(keypress)
player_action.execute(map)

output.display(m.map_string)



