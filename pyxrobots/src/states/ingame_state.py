
from states.pyx_state import *
from keybinder import *
from ingame_data import *


class IngameState(PyxState):
    data: IngameData

    def __init__(self):
        super().__init__()
        self.data = IngameData()
        self.data.player = (2, 0)
        self.data.enemies = [(0, 0)]

    def enter(self):
        print('entering ' + self.__class__.__name__)

    def exit(self):
        print('exiting ' + self.__class__.__name__)

    def update(self):
        # ingame_data.move_player_according_to_keypress(key)
        # ingame_data.move_all_enemies()
        pass

    def render(self) -> str:
        return "IngameState"
        # window_ui.display(m.map_string)

