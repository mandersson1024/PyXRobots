
from map import *
from ui import *


m = Map(16, 9)
ui = ConsoleUI()
# ui = WindowUI()
ui.display(m.map_string)
ui.hold()
