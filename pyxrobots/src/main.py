
from map import *
from ui import *


m = Map(16, 9)
m.player_position = (5, 5)

ui = ConsoleUI()
# ui = WindowUI()
ui.display(m.map_string)
ui.hold()
